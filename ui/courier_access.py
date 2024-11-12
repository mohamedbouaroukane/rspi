

from PyQt5 import QtCore, QtGui, QtWidgets
from config import assetsURL

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data):
        self.data=data
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 765)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DropParcelBtn_2 = QtWidgets.QFrame(self.centralwidget)
        self.DropParcelBtn_2.setGeometry(QtCore.QRect(300, 210, 201, 251))
        self.DropParcelBtn_2.setAutoFillBackground(False)
        self.DropParcelBtn_2.setStyleSheet("#DropParcelBtn_2{\n"
"border:2px solid;\n"
"    border-color: rgb(47, 95, 171);\n"
"border-radius:15px;\n"
"background-color:none;\n"
"}")
        self.DropParcelBtn_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DropParcelBtn_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DropParcelBtn_2.setObjectName("DropParcelBtn_2")
        self.sendBtn = QtWidgets.QPushButton(self.DropParcelBtn_2)
        self.sendBtn.setGeometry(QtCore.QRect(10, 200, 181, 41))
        self.sendBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendBtn.setStyleSheet("background-color: rgb(250, 169, 25);\n"
"color: rgb(0, 29, 75);\n"
"font: 87 8pt \"Cairo Black\";\n"
"border-radius:7px;\n"
"cursor:pointer")
        self.sendBtn.setObjectName("sendBtn")
        self.label_4 = QtWidgets.QLabel(self.DropParcelBtn_2)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 101, 111))
        self.label_4.setStyleSheet("background-color:none")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(assetsURL+"/send.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.DropParcelBtn_3 = QtWidgets.QFrame(self.centralwidget)
        self.DropParcelBtn_3.setGeometry(QtCore.QRect(60, 210, 201, 251))
        self.DropParcelBtn_3.setAutoFillBackground(False)
        self.DropParcelBtn_3.setStyleSheet("#DropParcelBtn_3{\n"
"border:2px solid;\n"
"    border-color: rgb(47, 95, 171);\n"
"border-radius:15px;\n"
"background-color:none;\n"
"}")
        self.DropParcelBtn_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DropParcelBtn_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DropParcelBtn_3.setObjectName("DropParcelBtn_3")
        self.expiredBtn = QtWidgets.QPushButton(self.DropParcelBtn_3)
        self.expiredBtn.setGeometry(QtCore.QRect(10, 200, 181, 41))
        self.expiredBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.expiredBtn.setStyleSheet("background-color: rgb(250, 169, 25);\n"
"color: rgb(0, 29, 75);\n"
"font: 87 8pt \"Cairo Black\";\n"
"border-radius:7px;\n"
"cursor:pointer")
        self.expiredBtn.setObjectName("expiredBtn")
        self.label_7 = QtWidgets.QLabel(self.DropParcelBtn_3)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 101, 111))
        self.label_7.setStyleSheet("background-color:none")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(assetsURL+"/time.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendBtn.setText(_translate("MainWindow", "Sending parcels"))
        self.expiredBtn.setText(_translate("MainWindow", "Expired Parcels"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
