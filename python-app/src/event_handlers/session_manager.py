"""
Implements a session context that saves the logged in user to simplify the 
code.
"""


class Session:
    current_user = None

    @classmethod
    def set_current_user(cls, username):
        cls.current_user = username

    @classmethod
    def get_current_user(cls):
        return cls.current_user
