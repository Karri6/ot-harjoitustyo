
class User:
    def __init__(self, name, age, username, password, workouts=None):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.workouts = workouts if workouts is not None else []

    def to_json(self):
        return {
            'name': self.name,
            'age': self.age,
            'username': self.username,
            'password': self.password,
            'workouts': self.workouts
        }

    @staticmethod
    def from_json(data):
        return User(data['name'], data['age'], data['username'],
                     data['password'], data.get('workouts', []))
