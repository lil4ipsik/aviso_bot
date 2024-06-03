import json
import os
from ui.main_ui import Ui_MainWindow as MainUI
ui = MainUI()

def create_user_data_file():
    # Determine the user's home directory
    if os.name == 'nt':  # Windows
        home_dir = os.path.expandvars('%APPDATA%')
        folder_name = 'Aviso Bot'
    else:  # Linux
        home_dir = os.path.expanduser('~')
        folder_name = '.aviso-bot'

    # Create the folder if it doesn't exist
    folder_path = os.path.join(home_dir, folder_name)
    file_path = os.path.join(folder_path, 'userdata.json')
    os.makedirs(folder_path, exist_ok=True)

    # Generate the file path
    if os.path.exists(file_path):
        return file_path
    else:
        with open(file_path, 'w') as file:
            json.dump({}, file)
        return file_path

def add_user(username, password, key, site):
    file_path = create_user_data_file()

    # Load existing user data from the JSON file
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Generate a unique ID for the user
    user_id = str(len(user_data) + 1)

    # Check if the user exists for the given site
    if username in user_data and user_data[username]['site'] == site:
        # Remove the user's data
        del user_data[username]

    # Add or update the user's data
    user_data.setdefault(user_id, {})['username'] = username
    user_data.setdefault(user_id, {})['password'] = password
    user_data.setdefault(user_id, {})['key'] = key
    user_data.setdefault(user_id, {})['site'] = site

    # Save the updated user data to the JSON file
    with open(file_path, 'w') as file:
        json.dump(user_data, file)

def delete_user_by_id(user_id):
    file_path = create_user_data_file()

    # Load existing user data from the JSON file
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Check if the user ID exists in the user data
    if user_id in user_data:
        # Remove the user's data
        del user_data[user_id]

        # Save the updated user data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(user_data, file)

def edit_user_by_id(user_id, username, password, key, site):
    file_path = create_user_data_file()

    # Load existing user data from the JSON file
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Check if the user ID exists in the user data
    if user_id in user_data:
        # Update the user's data
        user_data[user_id]['username'] = username
        user_data[user_id]['password'] = password
        user_data[user_id]['key'] = key
        user_data[user_id]['site'] = site

        # Save the updated user data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(user_data, file)

def get_user_data():
    file_path = create_user_data_file()

    # Load existing user data from the JSON file
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    return user_data

def path_to_data():
    if os.name == 'nt':  # Windows
        home_dir = os.path.expandvars('%APPDATA%')
        folder_name = 'Aviso Bot'
    else:  # Linux
        home_dir = os.path.expanduser('~')
        folder_name = '.aviso-bot'

    # Create the folder if it doesn't exist
    folder_path = os.path.join(home_dir, folder_name)

    return folder_path

def path_to_cookies(self):
    user_data = get_user_data()
    id = self.ui.userlist_combo.currentIndex()
    login = user_data.get(str(id+1), {}).get('username')
    site = user_data.get(str(id+1), {}).get('site')
    site = str(site).lower()
    folder_path = path_to_data()
    file_path = os.path.join(folder_path, f'{site}_{login}_cookies')

    return file_path