import json
import uuid

def add_user(username, password, key, site):
    # Load existing user data from the JSON file
    try:
        with open('userdata/userdata.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Generate a unique ID for the user
    user_id = str(uuid.uuid4())

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
    with open('userdata/userdata.json', 'w') as file:
        json.dump(user_data, file)

    return

def delete_user_by_id(user_id):
    # Load existing user data from the JSON file
    try:
        with open('userdata/userdata.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Check if the user ID exists in the user data
    if user_id in user_data:
        # Remove the user's data
        del user_data[user_id]

        # Save the updated user data to the JSON file
        with open('userdata/userdata.json', 'w') as file:
            json.dump(user_data, file)

    return

def edit_user_by_id(user_id, username, password, key, site):
    # Load existing user data from the JSON file
    try:
        with open('userdata/userdata.json', 'r') as file:
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
        with open('userdata/userdata.json', 'w') as file:
            json.dump(user_data, file)

    return