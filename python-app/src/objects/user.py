
class User:
    """
    Implements a User as object that can be stored as a Json file 
    """

    def __init__(self, name, age, username, password, workouts=None):
        """
        Constructs the user

        Args:
            name: users name
            age: users age 
            username: users unique username
            password: users selected password
            workouts: list of existing workouts
        """
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.workouts = workouts if workouts is not None else []

    def to_json(self):
        """
        Handles the formatting for dumping the user to a json file
        """
        return {
            'name': self.name,
            'age': self.age,
            'username': self.username,
            'password': self.password,
            'workouts': self.workouts
        }

    @staticmethod
    def from_json(data):
        """
        Handles creating a user from a json file
        """
        return User(data['name'], data['age'], data['username'],
                     data['password'], data.get('workouts', []))
