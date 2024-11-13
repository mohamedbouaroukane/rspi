# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collect-parcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from config import assetsURL
from PyQt5.QtMultimedia import QSound

from lockercontrol.relay import RelayController
from ui.util.sound import sound_player

class CollectParcelWindow(object):
    def setupUi(self, MainWindow):
        self.sound = sound_player()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 651, 771))
        self.frame.setStyleSheet("#frame{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 210, 191, 81))
        self.label_3.setStyleSheet("#label_3{\n"
"font: 87 14pt \"Cairo Black\";\n"
"    color: rgb(47, 95, 171);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(160, 90, 141, 141))
        self.label_5.setStyleSheet("background-color:none")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(assetsURL+"/barcode.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(60, 310, 331, 3))
        self.line.setStyleSheet("#line{\n"
"background-color: rgb(47, 95, 171);\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 340, 261, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 400, 60, 60))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 400, 60, 60))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 400, 60, 60))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("\n"
"font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 470, 60, 60))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 470, 60, 60))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 470, 60, 60))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 610, 60, 60))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 610, 61, 60))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"background-color: rgb(250, 169, 25);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 540, 60, 60))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 540, 60, 60))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 540, 60, 60))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"    background-color: rgb(47, 95, 171);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(assetsURL+"/back-icon.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.back.setStyleSheet("#back{\n"
"background-color: rgb(47, 95, 171);\n"
"border-radius:10px;\n"
"}")
        self.back.setText("")
        self.back.setObjectName("back")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(140, 610, 60, 60))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("font: 87 12pt \"Cairo Black\";\n"
"background-color: rgb(243, 243, 243);\n"
"color: rgb(47, 95, 171);\n"
"border-radius:7px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.back.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.line.raise_()
        self.plainTextEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.label_4.raise_()
        self.pushButton_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.update_text_field(1))
        self.pushButton_2.clicked.connect(lambda: self.update_text_field(2))
        self.pushButton_3.clicked.connect(lambda: self.update_text_field(3))
        self.pushButton_4.clicked.connect(lambda: self.update_text_field(4))
        self.pushButton_6.clicked.connect(lambda: self.update_text_field(5))
        self.pushButton_5.clicked.connect(lambda: self.update_text_field(6))
        self.pushButton_10.clicked.connect(lambda: self.update_text_field(7))
        self.pushButton_11.clicked.connect(lambda: self.update_text_field(8))
        self.pushButton_7.clicked.connect(lambda: self.update_text_field(9))
        self.pushButton_8.clicked.connect(lambda: self.update_text_field(0))

        self.click_sound = QSound(assetsURL+"/clickSound.wav")
        self.pushButton_9.clicked.connect(self.enter_code)
        self.pushButton_12.clicked.connect(self.delete_last_number)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.relay_controller = RelayController(4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Scanning Barcode"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "0"))
        self.pushButton_9.setText(_translate("MainWindow", "Enter"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
   

    def update_text_field(self, digit):
            current_text = self.plainTextEdit.toPlainText()
            self.plainTextEdit.setPlainText(current_text + str(digit))
            self.sound.play_click_sound()
    def delete_last_number(self):
        current_text = self.plainTextEdit.toPlainText()
        if current_text:
                new_text = current_text[:-1]  # Remove the last character
                self.plainTextEdit.setPlainText(new_text)
                self.sound.play_click_sound()  
    def enter_code(self):
        current_text = self.plainTextEdit.toPlainText()
        if current_text:
                print(current_text)    
                self.relay_controller.turn_on()
                sleep(5)
                self.relay_controller.turn_off()