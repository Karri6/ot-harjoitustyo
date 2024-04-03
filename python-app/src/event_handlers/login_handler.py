"""
handles the login of a user
"""

import json
import os
from objects.user import User

USERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/users/')

current_user = None

def load_user(username):
    filepath = os.path.join(USERS_DIR, f"{username}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            user_data = json.load(f)
            return User.from_json(user_data)
    return None

def login(username, password):
    global current_user
    user = load_user(username)
    if user and user.password == password:
        current_user = user
        return True
    return False

def get_current_user():
    return current_user
