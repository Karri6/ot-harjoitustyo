import unittest
from event_handlers.login_handler import LoginManager


class TestLoginHandler(unittest.TestCase):
    """
     Tests the login handler. 
     Test json file generated manually for these tests
     "masa.json"
    """

    def setUp(self):
        """
        Sets up the test by creating an instance of LoginManager
        """
        self.handler = LoginManager()

    def test_load_user(self):
        """
        tests loading a user
        """
        user = self.handler.load_user("masa")
        self.assertEqual(user.age, "35")

    def test_incorrect_user(self):
        """
        tests loading a nonexistent user
        """
        self.assertEqual(self.handler.load_user("null"), None)

    def test_login_user(self):
        """
        tests if a known user can login
        """
        self.assertEqual(self.handler.login("masa", "1234"), True)

    def test_incorrect_login(self):
        """
        tests if a known user can login with wrong credentials
        """
        self.assertEqual(self.handler.login("masa", "1111"), False)

    def test_get_current_user(self):
        """
        tests if class returns correct user
        """
        self.handler.login("masa", "1234")
        user = self.handler.get_current_user()
        self.assertEqual(user.username, "masa")

    def test_logout(self):
        """
        tests the logout method
        """
        self.handler.login("masa", "1234")
        self.handler.logout()
        logout_result = self.handler.get_current_user()
        self.assertEqual(logout_result, None)
