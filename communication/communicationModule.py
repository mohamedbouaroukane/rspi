import sys
import json
import requests
from PyQt5 import QtWidgets, QtCore
from config import parcelLockerId
from lockercontrol.relay import RelayController
# HttpRequester class definition
class HttpRequester(QtCore.QObject):
    show_courier_access_signal = QtCore.pyqtSignal(object)
    show_collect_parcel_signal = QtCore.pyqtSignal()
    error_signal = QtCore.pyqtSignal(str) 

    def __init__(self, base_url):
   
        super().__init__()
        self.base_url = base_url
        self.relay_controller = RelayController(17)
        

    def courier_access(self, json=None):
        try:
            response = requests.get(f"{self.base_url}parcel-locker/{parcelLockerId}/access", json=json)
            print(f"URL: {response.url}")
            return response.json(), response.status_code
        except Exception as e:
            print(e)
            self.error_signal.emit(str(e))
            return None

    def drop_parcel(self, params=None):
        try:
            response = requests.get(f"{self.base_url}parcel-locker/{parcelLockerId}/parcel?parcelCode=", params=params)
            print(f"URL: {response.url}")
            return response.json(), response.status_code
        except Exception as e:
            print(e)
            self.error_signal.emit(str(e))
            return None

    def collect_parcel(self, params=None):
        try:
            response = requests.get(f"{self.base_url}parcel-locker/{parcelLockerId}/parcel", params=params)
            print(f"URL: {response.url}")
            return response.json(), response.status_code
        except Exception as e:
            print(e)
            self.error_signal.emit(str(e))
            return None

    def send_request(self, data):
        if data.startswith("LNuWRI9ovA"):
             response = self.drop_parcel(params={"parcelCode":data[len("LNuWRI9ovA"):]})
             if response:
                get_response, get_status = response
                if get_status == 200:
                    data = json.loads(response.text)
                    pin = data.get('pin')
                
                else:
                    self.error_signal.emit("Error in courier access")
        elif data.startswith("CA-"):
            response = self.courier_access()
            if response:
                get_response, get_status = response
                if get_status == 200:
                    converted_list = [item["pin"] for item in get_response if "pin" in item]
                    self.show_courier_access_signal.emit(converted_list)
                else:
                    self.error_signal.emit("Error in courier access")
        elif data.startswith("CC-"):
            response = self.collect_parcel()
            if response:
                get_response, get_status = response
                if get_status == 200:
                    self.show_collect_parcel_signal.emit()
                else:
                    self.error_signal.emit("Error in collecting parcel")
        else:
            self.error_signal.emit("Invalid request type")