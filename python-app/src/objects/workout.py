"""
Class implements a workout object that can be then stored as a Json file
"""
import json
from datetime import datetime

class Workout:
    def __init__(self, username, date, content):
        self.username = username
        self.date = date if isinstance(date, datetime) else datetime.strptime(date, '%Y-%m-%d')
        self.content = content

    def to_json(self):
        return json.dumps({
            'username': self.username,
            'date': self.date.strftime('%Y-%m-%d'),
            'content': self.content
        })

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Workout(data['username'], data['date'], data['content'])
