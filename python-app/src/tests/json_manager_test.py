import unittest
from event_handlers import json_manager
from objects.user import User

class TestJsonManager(unittest.TestCase):
    """
    Implements test for json manager.
    Uses testi.json as test file

    TODO: fix test check user
    """

    def setUp(self):
        self.manager = json_manager
        self.user = User

    def test_load_users(self):
        self.assertNotEqual(self.manager.load_users(),True)

    def test_save_and_load_user(self):
        self.user = User("savetest", "1", "savetest", "0202")
        self.manager.save_user(self.user)
        self.assertEqual(self.manager.load_user(self.user.username).name, "savetest")

    #def test_check_user(self):        
     #   self.manager.load_users()
      #  self.assertEqual(self.manager.check_user("testi"), True)

    def test_check_no_user(self):
        self.manager.load_users()
        self.assertEqual(self.manager.check_user("test"), False)


    # TODO: tests for workouts when implemented
    