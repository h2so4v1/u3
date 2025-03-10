import sys
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtGui import QIcon
from widget import Ui_Widget
from capture_screen import capture_window
from yolo_detection import detect_objects, draw_detections, get_closest_detection_center, load_model
from mouse_events import move_mouse, click_mouse
from metinstones_break import text_break
from rotate_screen import rotate_screen, rotate_screen_periodically, check_and_rotate_screen
from activate_skill import activate_skills, activate_skills_periodically
from captcha_solver import capture_captcha_and_solve
from auto_pickup import auto_pickup
import threading
import time
import pygetwindow as gw
from pywinauto import Application

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Üst paneli kaldır
        self.oldPos = None  # Fare konumunu saklamak için değişken

        self.window_title = None

        # Kapatma butonu (❌)
        self.close_button = QPushButton("❌", self)
        self.close_button.setGeometry(self.width() - 40, 0, 30, 30)  # Sağ üst köşe
        self.close_button.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.close_button.clicked.connect(self.close)

        # Küçültme butonu (➖)
        self.minimize_button = QPushButton("➖", self)
        self.minimize_button.setGeometry(self.width() - 80, 0, 30, 30)  # Kapatmanın soluna
        self.minimize_button.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.minimize_button.clicked.connect(self.showMinimized)

        # Başlat butonu
        self.start_button = self.ui.pushButton
        self.start_button.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.start_button.clicked.connect(self.start_main_functionality)

        # Durdurma butonu
        self.stop_button = self.ui.pushButton_2
        self.stop_button.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.stop_button.clicked.connect(self.stop_main_functionality)

        # PID ComboBox
        self.pid_combobox = self.ui.comboBox
        self.pid_combobox.addItem("Select PID")
        self.pid_combobox.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.pid_combobox.currentIndexChanged.connect(self.update_window_title)

        # ACCEPT butonu
        self.accept_button = self.ui.pushButton_5
        self.accept_button.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.accept_button.clicked.connect(self.focus_and_move_window)

        # Metin kırma süresi için LineEdit
        self.text_break_time_edit = self.ui.lineEdit
        self.text_break_time_edit.setValidator(QIntValidator(0, 999))  # Sadece sayı girişine izin ver
        self.text_break_time_edit.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        # Auto Skill LineEdit
        self.auto_skill_time_edit = self.ui.lineEdit_2
        self.auto_skill_time_edit.setValidator(QIntValidator(0, 999))  # Sadece sayı girişine izin ver
        self.auto_skill_time_edit.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.auto_skill_time_edit.setVisible(False)  # Başlangıçta gizli

        self.pause_event = threading.Event()
        self.text_break_event = threading.Event()
        self.text_break_event.set()  # Başlangıçta metin kırma işlemi olmadığını belirtmek için set

        # Uygulamaları listeleyen ve PID combobox'ı güncelleyen bir timer oluştur
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_pid_list)
        self.timer.start(5000)  # Her 5 saniyede bir listeyi güncelle

        # Auto Skill checkbox durumu değiştiğinde lineEdit görünürlüğünü ayarla
        self.ui.checkBox_2.stateChanged.connect(self.toggle_auto_skill_line_edit)

    def toggle_auto_skill_line_edit(self, state):
        if state == Qt.Checked:
            self.auto_skill_time_edit.setVisible(True)
        else:
            self.auto_skill_time_edit.setVisible(False)

    def update_pid_list(self):
        current_pid = self.pid_combobox.currentText()
        self.pid_combobox.clear()
        self.pid_combobox.addItem("Select PID")
        windows = gw.getWindowsWithTitle('')
        for window in windows:
            if window.title:
                self.pid_combobox.addItem(f"{window.title} ({window._hWnd})", window._hWnd)
        
        # Geçerli seçimi koru
        index = self.pid_combobox.findText(current_pid)
        if index != -1:
            self.pid_combobox.setCurrentIndex(index)

    def update_window_title(self):
        selected_pid = self.pid_combobox.currentData()
        if selected_pid:
            self.window_title = selected_pid

    def focus_and_move_window(self):
        if self.window_title and self.window_title != "Select PID":
            try:
                app = Application().connect(handle=self.window_title)
                window = app.window(handle=self.window_title)
                window.set_focus()
                window.move_window(0, 0)
            except Exception as e:
                print(f"Pencere taşınamadı: {e}")
        else:
            print("Lütfen bir pencere seçin.")

    def start_main_functionality(self):
        if not self.window_title or self.window_title == "Select PID":
            print("Lütfen bir pencere seçin.")
            return

        try:
            self.text_break_time = int(self.text_break_time_edit.text())
        except ValueError:
            print("Geçerli bir metin kırma süresi girin.")
            return

        self.skill_activation_interval = 300  # Skilleri aktif hale getirme süresi (saniye olarak)
        self.captcha_check_interval = 0.1  # CAPTCHA kontrol süresi (saniye olarak)

        # YOLO modelini yükle
        self.model = load_model()

        # Bot başlatıldığında ilk olarak skilleri aktif hale getir ve binekten inip tekrar bin
        activate_skills(self.pause_event, self.text_break_event)

        # Skillerin periyodik olarak aktif hale getirilmesi için bir thread oluştur ve hemen çalıştır
        threading.Thread(target=activate_skills_periodically, args=(self.skill_activation_interval, self.pause_event, self.text_break_event), daemon=True).start()

        # Periyodik ekran döndürme işlemi için bir thread oluştur
        threading.Thread(target=rotate_screen_periodically, daemon=True).start()

        self.main_thread = threading.Thread(target=self.main_loop, daemon=True)
        self.main_thread.start()

    def stop_main_functionality(self):
        self.pause_event.set()

    def main_loop(self):
        while not self.pause_event.is_set():
            try:
                print("Ekran görüntüsü alınıyor...")
                # Ekran görüntüsünü al
                image = capture_window(self.window_title)

                print("Nesne tespiti yapılıyor...")
                # Nesne tespiti yap
                results = detect_objects(image, self.model)

                num_detections = sum(1 for result in results for box in result.boxes if self.model.names[int(box.cls[0])] != 'none')
                print(f"{num_detections} nesne tespit edildi.")

                if num_detections > 0:
                    print("Tespit edilen nesneler çiziliyor...")
                    # Tespit edilen nesneleri çiz
                    image_with_detections = draw_detections(image, results, self.model)

                    print("Ekranın ortasına en yakın nesne bulunuyor...")
                    # Ekranın ortasına en yakın tespit edilen nesnenin merkezini al
                    closest_center = get_closest_detection_center(image, results, self.model)

                    if closest_center:
                        print(f"Fare {closest_center} koordinatlarına hareket ettiriliyor...")
                        # Fareyi nesnenin merkezine hareket ettir
                        move_mouse(closest_center[0], closest_center[1])

                        print("Fare tıklanıyor...")
                        # Fareyi tıklama işlemi
                        click_mouse()

                        # Metin kırma süresi sırasında skill açılmasını engelle
                        self.text_break_event.clear()  # Metin kırma işleminin başladığını belirt
                        text_break(self.text_break_time)
                        self.text_break_event.set()  # Metin kırma işleminin bittiğini belirt

                        # Metin kırma süresinin sonunda otomatik eşya toplama fonksiyonunu çağır
                        auto_pickup()
                    else:
                        print("Ekranın ortasına yakın nesne bulunamadı.")

                # Tespit edilen nesnelere göre ekranı döndürme işlemini kontrol et
                check_and_rotate_screen(results, self.model)

            except Exception as e:
                print(f"Hata: {e}")

            # CAPTCHA çözme işlemini periyodik olarak çalıştır
            capture_captcha_and_solve(self.window_title, capture_window, move_mouse, click_mouse)
            time.sleep(self.captcha_check_interval)  # CAPTCHA kontrol süresi

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())