import unittest
from datetime import datetime
from event_handlers.json_manager import JsonManager
from objects.user import User
from objects.workout import Workout


class TestJsonManager(unittest.TestCase):
    """
    Implements test for json manager.
    Uses masa.json as test file

    """

    def setUp(self):
        self.manager = JsonManager()
        self.user = User

    def test_load_users(self):
        self.assertNotEqual(self.manager.load_users(), True)

    def test_save_and_load_user(self):
        self.user = User("savetest", "1", "savetest", "0202")
        self.manager.save_user(self.user)
        self.assertEqual(self.manager.load_user(
            self.user.username).name, "savetest")

    def test_check_no_user(self):
        self.manager.load_users()
        self.assertEqual(self.manager.check_user("test"), False)

    def test_save_workout_json(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        content = "testing information section"
        wod = Workout("masa", current_date, content)
        self.manager.save_workout_json(wod)

        wod_list = self.manager.load_workouts("masa")
        self.assertTrue(wod_list)

    def test_load_categories(self):
        movements = self.manager.load_categories()
        self.assertTrue(movements)

    def test_load_workouts_fail(self):
        empty_list = self.manager.load_workouts("no_user")
        self.assertEqual([], empty_list)
