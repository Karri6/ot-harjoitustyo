import unittest
from event_handlers import login_handler

class TestLoginHandler(unittest.TestCase):
    """
     Tests the login handler. 
     Test json file generated manually for these tests
     "testi.json"
    """
    def setUp(self):
        self.handler = login_handler
    
    def test_load_user(self):
        user = self.handler.load_user("testi")
        self.assertEqual(user.age, "55")
    
    def test_incorrect_user(self):
        self.assertEqual(self.handler.load_user("null"), None)

    def test_login_user(self):
        self.assertEqual(self.handler.login("testi", "0000"), True)

    def test_incorrect_login(self):
        self.assertEqual(self.handler.login("testi", "1111"), False)

    def test_get_current_user(self):
        self.handler.login("testi", "0000")
        user = self.handler.get_current_user()
        self.assertEqual(user.name, "testi")
