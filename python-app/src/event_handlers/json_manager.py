import json
import os
from datetime import datetime
from objects.user import User
from objects.workout import Workout

WORKOUTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/workouts/')
USERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/users/')


class JsonManager():
    """
    Class to handle all Json File events
    """

    def __init__(self):
        """
        Constructor for the class
        """
        self.all_users = []
        self.load_users()

    def load_users(self):
        """
        Loads all users to a directory
        """
        for file in os.listdir(USERS_DIR):
            file_path = os.path.join(USERS_DIR, file)
            with open(file_path, 'r') as f:
                users_data = json.load(f)

            self.all_users.append(users_data['username'])


    def save_user(self, user):
        """
        Saves a user to a json file

        Args:
            user: the user object being saved
        """
        os.makedirs(USERS_DIR, exist_ok=True)
        user_file = os.path.join(USERS_DIR, f"{user.username}.json")
        with open(user_file, 'w') as f:
            json.dump(user.to_json(), f, indent=4)


    def load_user(self, username):
        """
        Loads a user from a json file

        Args:
            username: the unique username of user being loaded

        Returns:
            user object or none if no user found
        """
        filepath = os.path.join(USERS_DIR, f"{username}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                user_data = json.load(f)
            return User.from_json(user_data)
        return None

    

    def save_workout_json(self, workout):
        """
        Saves a workout to a json and updates the user whose workout it is.

        Args: 
            workout: workout object being saved
        """
        workout_data = workout.to_json()
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        workouts_file = os.path.join(
            WORKOUTS_DIR, f"{workout_data['username']}_{current_time}.json")

        with open(workouts_file, 'w') as f:
            json.dump(workout_data, f, indent=4)

        user = self.load_user(workout_data['username'])
        workout_filename = os.path.basename(workouts_file)

        if workout_filename not in user.workouts:
            user.workouts.append(workout_filename)
            self.save_user(user)


    def load_workouts(self, username):
        """
        Loads all workouts of a user and returns them in a list

        Args:
            username: username of the user whose workouts are being loaded

        Returns:
            workouts: a list of user's workouts
        """
        user = self.load_user(username)
        if user is None:
            return []

        workouts = []
        for workout_filename in user.workouts:            
            workout_file = os.path.join(WORKOUTS_DIR, workout_filename)
            if os.path.exists(workout_file):
                with open(workout_file, 'r') as f:
                    workouts.append(Workout.from_json(json.load(f)))

        return workouts
    
    
    def check_user(self, username):
        """
        Checks if a username exists

        Returns:
            bool, if username exist or not
        """
        return username in self.all_users
    

    def load_categories(self):
        """
        Loads the exercise categories from a json file and return them in a dict

        Returns:
            all_movements, dict of all available movements
        """
        all_movements = {}
        file_path = os.path.join("src", "data", "categories", "movements.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                all_movements = json.load(file)

        return all_movements
