import requests
from PyQt6.QtCore import QThread, pyqtSignal

class KeyValidationThread(QThread):
    key_validation_signal = pyqtSignal(bool, str)

    def __init__(self, username, key):
        super().__init__()
        self.username = username
        self.key = key

    def run(self):
        is_valid, valid_to = is_key_valid(self.username, self.key)
        self.key_validation_signal.emit(is_valid, valid_to)
        self.deleteLater()
        

def is_key_valid(username, key):
    if key is None:
        return False, None

    url = "https://aviso.xserv.pp.ua/api/is-key-valid"
    data = {
        "username": username,
        "activationCode": key
    }
    try:
        response = requests.post(url, json=data)
        response_json = response.json()
        is_valid = response_json.get('is_valid', False)
        valid_to = response_json.get('valid_to', None)
    except requests.exceptions.RequestException:
        is_valid = False
        valid_to = None
    return is_valid, valid_to
