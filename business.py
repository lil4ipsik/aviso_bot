from datetime import datetime
import requests


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


def logtime():
    return f'[{datetime.now().replace(microsecond=0)}]'
