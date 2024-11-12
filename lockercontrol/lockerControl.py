import serial
import time

class LockerController:
    def __init__(self, port, baud_rate=9600):
       try:
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2) 
       except Exception as e:
          print(e)
    

    def send_command(self, pin, command):
        command_str = f"{pin}{command}"
        self.ser.write(command_str.encode())
        time.sleep(1) 

    def close(self):
        self.ser.close()