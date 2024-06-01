import hashlib
from datetime import datetime


def calculate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    hashed_string = sha256_hash.hexdigest()

    return hashed_string


def generate_activation_code_by_username(username: str, year_expire: int, month_expire: int, days_expire: int) -> str:
    try:
        datetime(year_expire, month_expire, days_expire)
    except ValueError:
        raise ValueError('Invalid year or month or days')
    if len(str(year_expire)) != 4:
        raise ValueError('year_expire must be 4 characters long')
    key = calculate_sha256_hash(username).upper()[:25]

    year_expire = str(year_expire)
    month_expire = f'0{month_expire}' if len(str(month_expire)) == 1 else str(month_expire)
    days_expire = f'0{days_expire}' if len(str(days_expire)) == 1 else str(days_expire)

    key = (f'{key[0]}{year_expire[2]}{key[2]}{month_expire[0]}{key[4]}-'
           f'{year_expire[1]}{key[6:9]}{days_expire[1]}-'
           f'{key[10:15]}-'
           f'{year_expire[0]}{key[16:19]}{month_expire[1]}-'
           f'{key[20]}{year_expire[3]}{key[22]}{days_expire[0]}{key[24]}')

    return key


def get_date_expire_from_code(code: str) -> dict:
    code = code.replace('-', '')
    year = int(f'{code[15]}{code[5]}{code[1]}{code[21]}')
    month = int(f'{code[3]}{code[19]}')
    day = int(f'{code[23]}{code[9]}')

    try:
        datetime(year, month, day)
    except ValueError:
        raise ValueError('Invalid year or month or days')

    return {
        'year': year,
        'month': month,
        'day': day
    }

def get_current_date() -> dict:
    now = datetime.now()
    return {
        'year': now.year,
        'month': now.month,
        'day': now.day
        }

def is_key_date_expired(key: str) -> bool:
    key = key.replace('-', '')
    try:
        data = get_date_expire_from_code(key)
        expire_date = datetime(year=data['year'], month=data['month'], day=data['day'])
        data = get_current_date()
        current_date = datetime(year=data['year'], month=data['month'], day=data['day'])
    except (ValueError, Exception):
        return False

    if current_date < expire_date:
        return True
    else:
        return False


def is_valid_username_key_hash(username: str, key: str) -> bool:
    key = key.replace('-', '')
    username_hash = f'{key[0]}{key[2]}{key[4]}{key[6:9]}{key[10:15]}{key[16:19]}{key[20]}{key[22]}{key[24]}'
    # calculated_hash
    c_h = calculate_sha256_hash(username).upper()[:25]
    calculated_hash = f'{c_h[0]}{c_h[2]}{c_h[4]}{c_h[6:9]}{c_h[10:15]}{c_h[16:19]}{c_h[20]}{c_h[22]}{c_h[24]}'
    return True if username_hash == calculated_hash else False


def is_key_valid(username, key):
    key = key.replace('-', '')
    if len(key) != 25:
        return False
    elif not is_valid_username_key_hash(username, key):
        return False
    elif not is_key_date_expired(key):
        return False

    return True
