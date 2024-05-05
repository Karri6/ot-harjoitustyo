import unittest
from event_handlers.session_manager import Session


class TestSessionManager(unittest.TestCase):
    """
    Tests the session manager class
    """
    def setUp(self):
        self.session = Session()

    def test_session_manager(self):
        """
        Testing to see if the current user method works
        """
        Session.set_current_user("test")
        result = Session.get_current_user()
        self.assertEqual(result, "test")
