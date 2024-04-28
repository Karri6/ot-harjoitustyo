import os
from event_handlers.json_manager import JsonManager
from event_handlers.session_manager import Session


class LoginManager:
    """
    Class to handle login events
    """

    USERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/users/')

    def __init__(self):
        """
        Constructor for the class
        """
        self.manager = JsonManager()
        self.current_user = None

    def load_user(self, username):
        """
        Uses json manager class to load a user

        Args:
            username: unique username of the user being loaded
        
        Returns:
            user object
        """
        return self.manager.load_user(username)

    def login(self, username, password):
        """
        Handles the login event

        Args:
            username: unique username of the user
            password: user's password

        Returns: 
            bool, was the login succesful
        """
        username = username.lower()
        user = self.load_user(username)
        if user and user.password == password:
            self.current_user = user
            Session.set_current_user(username)
            return True
        return False

    def get_current_user(self):
        """
        Gets the current user

        Returns:
            user object
        """
        return self.current_user

    def logout(self):
        """
        Logs current user out
        """
        self.current_user = None
