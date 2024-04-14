import os
from event_handlers.json_manager import JsonManager
from event_handlers.session_manager import Session


class LoginManager:
    USERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/users/')

    def __init__(self):
        self.manager = JsonManager()
        self.current_user = None

    def load_user(self, username):
        return self.manager.load_user(username)

    def login(self, username, password):
        username = username.lower()
        user = self.load_user(username)
        if user and user.password == password:
            self.current_user = user
            Session.set_current_user(username)
            return True
        return False

    def get_current_user(self):
        return self.current_user

    def logout(self):
        self.current_user = None
