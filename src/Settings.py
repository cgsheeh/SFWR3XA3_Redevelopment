__author__ = 'connor'

class Settings:
    ## Create settings object
    def __init__(self):
        self.something = 1

    # Return user settings
    def get(self):
        return False

    # Change implementation of settings to reflect JSON settings
    def set(self, json_settings):
        return