
class Session:
    """
    Implements a session context that saves the logged in user to simplify the 
    code.
    """
    current_user = None

    @classmethod
    def set_current_user(cls, username):
        """
        Saves the current user

        Args:
            username: unique username of a user
        """
        cls.current_user = username

    @classmethod
    def get_current_user(cls):
        """
        Gets the saved user

        Returns:
            current user's username
        """
        return cls.current_user
