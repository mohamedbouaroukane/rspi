

from PyQt5.QtMultimedia import QSound
from config import assetsURL
class sound_player(object):
    def __init__(self) :
        self.click_sound = QSound(assetsURL+"/clickSound.wav")

    def play_click_sound(self):
     self.click_sound.play()    