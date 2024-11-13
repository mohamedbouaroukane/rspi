from PyQt5 import QtWidgets
from ui.nhome import Ui_MainWindow as HomeWindow
from ui.drop_parcel import Ui_MainWindow as DropParcelWindow
from ui.collect_parcel import  CollectParcelWindow
from ui.courier_access import Ui_MainWindow as CourierAccessWindow
from ui.util.sound import sound_player
from ui.send_parcels import Ui_MainWindow as CourierAccessSendWindow
from functools import partial




class MainApp(QtWidgets.QMainWindow):
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    def __init__(self):
        super().__init__()
        self.sound = sound_player()
        self.home_window = HomeWindow()
        self.drop_parcel_window = DropParcelWindow()
        self.collect_parcel_window = CollectParcelWindow()
        self.courier_access_window = CourierAccessWindow()
        self.courier_access_send_window = CourierAccessSendWindow()
        self.showFullScreen()
        
        self.drop_parcel_window.setupUi(self)
        self.collect_parcel_window.setupUi(self)
        self.showFullScreen()
        self.home_window.setupUi(self)
        self.home_window.pushButton.clicked.connect(self.show_drop_parcel)
        self.home_window.pushButton_2.clicked.connect(self.show_collect_parcel)

       

    def show_home(self):
        self.sound.play_click_sound()
        self.home_window.setupUi(self)
        self.home_window.pushButton.clicked.connect(self.show_drop_parcel)
        self.home_window.pushButton_2.clicked.connect(self.show_collect_parcel)
        self.show()

    def show_drop_parcel(self):
        self.sound.play_click_sound()
        self.drop_parcel_window.setupUi(self)
        self.drop_parcel_window.back.clicked.connect(self.show_home)
        self.show()

    def show_collect_parcel(self):
        self.sound.play_click_sound()
        self.collect_parcel_window.setupUi(self)
        self.collect_parcel_window.back.clicked.connect(self.show_home)
        self.show()
    def show_courier_access(self,data):
        self.sound.play_click_sound()
        self.courier_access_window.setupUi(self)
        self.courier_access_window.sendBtn.clicked.connect(partial(self.show_courier_send_access, data["sending"]))
        self.show()
    def show_courier_send_access(self,data):
        self.sound.play_click_sound()
        self.courier_access_send_window.setupUi(self,data)
        self
        self.show()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())