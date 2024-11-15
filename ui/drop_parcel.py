# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drop-parcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from config import assetsURL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -11, 651, 791))
        self.frame.setStyleSheet("#frame{\n"
"background-color:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 201, 201))
        self.label_4.setStyleSheet("background-color:none")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(assetsURL+"/barcode.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 410, 241, 81))
        self.label.setStyleSheet("#label{\n"
"font: 87 18pt \"Cairo Black\";\n"
"    color: rgb(47, 95, 171);\n"
"}")
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(20, 30, 51, 51))
        self.back.setStyleSheet("#back{\n"
"background-color: rgb(47, 95, 171);\n"
"border-radius:10px;\n"
"}")
        self.back.setText("")
        self.back.setObjectName("back")
        self.back.setIcon(QtGui.QIcon(QtGui.QPixmap(assetsURL+"/back-icon.png")))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Scanning Barcode"))


