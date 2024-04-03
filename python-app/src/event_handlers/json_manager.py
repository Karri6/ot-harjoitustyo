import json
import os
from objects.user import User 
from objects.workout import Workout

USERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data/users.json')
WORKOUTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/workouts/')
USERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data/users/')
all_users = []

def load_users():
    global all_users
    if not os.path.exists(USERS_FILE):
        return False
    
    with open(USERS_FILE, 'r') as f:
        users_data = json.load(f)
    
    all_users = [user['username'] for user in users_data]
    

def save_user(user):
    os.makedirs(USERS_DIR, exist_ok=True)
    user_file = os.path.join(USERS_DIR, f"{user.username}.json")
    with open(user_file, 'w') as f:
        json.dump(user.to_json(), f, indent=4)
                

def load_user(username):
    user_file = os.path.join(USERS_DIR, f"{username}.json")
    if not os.path.exists(user_file):
        return None
    with open(user_file, 'r') as f:
        return User.from_json(json.load(f))

# draft how to save and load workouts based on the logic used for user jsons
def save_workout(workout):
    workouts_file = os.path.join(WORKOUTS_DIR, f"{workout.username}_{workout.date.strftime('%Y-%m-%d')}.json")
    with open(workouts_file, 'w') as f:
        json.dump(workout.to_json(), f, indent=4)
    
    user = load_user(workout.username)
    if user:
        workout_filename = os.path.basename(workouts_file)
        if workout_filename not in user.workouts:
            user.workouts.append(workout_filename)
            save_user(user)

def load_workouts(username):
    user = load_user(username)
    if not user:
        return []
    
    workouts = []
    for workout_filename in user.workouts:
        workout_file = os.path.join(WORKOUTS_DIR, workout_filename)
        if os.path.exists(workout_file):
            with open(workout_file, 'r') as f:
                workouts.append(Workout.from_json(json.load(f)))
    return workouts

def check_user(username):
    if username in all_users:
        return True
    return False