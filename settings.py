import json


class Settings:
    def __init__(self):
        settings_file = open("settings.json")
        self.settings = json.load(settings_file)
        settings_file.close()

    def get_settings(self):
        return self.settings

    def save_settings(self):
        settings_file = open("settings.json")
        settings_file.write(json.dumps(self.settings))
        settings_file.close()
