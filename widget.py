from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QIntValidator, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget, QVBoxLayout, QHBoxLayout)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"MysTBot")
        Widget.setStyleSheet("background-color: #333; color: #fff;")    
        Widget.resize(530, 300)
        Widget.setMinimumSize(QSize(530, 300))
        Widget.setMaximumSize(QSize(530, 300))
        Widget.setAutoFillBackground(False)
        
        self.groupBox_Farm = QGroupBox(Widget)
        self.groupBox_Farm.setObjectName(u"groupBox_Farm")
        self.groupBox_Farm.setGeometry(QRect(20, 40, 240, 121))


        self.pushButton = QPushButton(self.groupBox_Farm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 80, 24))
        self.pushButton.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.pushButton_2 = QPushButton(self.groupBox_Farm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 20, 80, 24))
        self.pushButton_2.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.label = QLabel(self.groupBox_Farm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 55, 60, 15))

        self.lineEdit = QLineEdit(self.groupBox_Farm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 55, 31, 21))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setValidator(QIntValidator(0, 999))  # Sadece sayı girişine izin ver
        self.lineEdit.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.label_2 = QLabel(self.groupBox_Farm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 100, 71, 16))

        self.groupBox_Features = QGroupBox(Widget)
        self.groupBox_Features.setObjectName(u"groupBox_Features")
        self.groupBox_Features.setGeometry(QRect(20, 160, 240, 121))


        self.checkBox = QCheckBox(self.groupBox_Features)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 30, 91, 22))


        self.checkBox_2 = QCheckBox(self.groupBox_Features)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 50, 71, 22))
      

        self.checkBox_3 = QCheckBox(self.groupBox_Features)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 70, 101, 22))


        self.lineEdit_2 = QLineEdit(self.groupBox_Features)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 50, 70, 20))
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla
        self.lineEdit_2.setVisible(False)  # Başlangıçta gizli

        self.groupBox_Farm_2 = QGroupBox(Widget)
        self.groupBox_Farm_2.setObjectName(u"groupBox_Farm_2")
        self.groupBox_Farm_2.setGeometry(QRect(270, 40, 240, 121))


        self.pushButton_5 = QPushButton(self.groupBox_Farm_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 55, 71, 21))
        self.pushButton_5.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.comboBox = QComboBox(self.groupBox_Farm_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 55, 141, 21))
        self.comboBox.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.label_5 = QLabel(self.groupBox_Farm_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 35, 141, 16))

        self.label_6 = QLabel(self.groupBox_Farm_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 80, 141, 16))

        self.groupBox_Farm_3 = QGroupBox(Widget)
        self.groupBox_Farm_3.setObjectName(u"groupBox_Farm_3")
        self.groupBox_Farm_3.setGeometry(QRect(270, 160, 240, 121))


        self.comboBox_2 = QComboBox(self.groupBox_Farm_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 30, 221, 21))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setStyleSheet("background-color: #555; color: #fff;") # Arka plan rengi ayarla

        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 0, 101, 31))
        font = QFont()
        font.setFamilies([u"Iceland"])
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"MysTBot", None))
        Widget.setWindowIcon(QIcon(u"acs.ico"))
        self.groupBox_Farm.setTitle(QCoreApplication.translate("Widget", u"Farm", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"START", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"STOP", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Metin sec:", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Killed Stones:", None))
        self.groupBox_Features.setTitle(QCoreApplication.translate("Widget", u"Features", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"Auto Pickup", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"Auto Skill", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"Captcha Solver", None))
        self.lineEdit_2.setText("")
        self.groupBox_Farm_2.setTitle(QCoreApplication.translate("Widget", u"Client 1024x768", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"ACCEPT", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Refreshes every 5 seconds", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"1024x768 Client PID input", None))
        self.groupBox_Farm_3.setTitle(QCoreApplication.translate("Widget", u"Select Metinstones", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"MysTBot", None))
    # retranslateUi