from datetime import datetime

class Workout:
    """
    Class implements a workout object that can be then stored as a Json file
    """
    def __init__(self, username, date, content):
        """
        Constructor for the class
        
        Args:
            username: unique username, whose workout this object is
            date: day of the workout
            content: the entries the workout consists of
        """
        self.username = username
        self.date = date if isinstance(
            date, datetime) else datetime.strptime(date, '%Y-%m-%d')
        self.content = content


    def to_json(self):
        """
        Handles the formatting for dumping the workout to a json file
        """
        return {
            'username': self.username,
            'date': self.date.strftime('%Y-%m-%d'),
            'content': self.content
        }


    @staticmethod
    def from_json(json_dict):
        """
        Handles creating a workout from a json file
        """
        return Workout(json_dict['username'], json_dict['date'], json_dict['content'])
