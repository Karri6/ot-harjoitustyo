import tkinter as tk
from gui.login_view import LoginView
from gui.signup_view import SignupView
from gui.main_view import MainView
from gui.workout_view import WorkoutView


class MainApp:
    """
    Class runs/manages the interface of the app by updating the new view
    to the same window.
    """

    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.root.geometry("680x620")
        self.show_login_view()

    def show_login_view(self):
        self.change_view(LoginView, self.show_signup_view, self.show_main_view)

    def show_signup_view(self):
        self.change_view(SignupView, self.show_main_view, self.show_login_view)

    def show_main_view(self):
        self.change_view(MainView)

    def show_workout_view(self):
        self.change_view(WorkoutView, self.show_main_view)

    def change_view(self, view_class, *args):
        if self.current_view is not None:
            self.current_view.destroy()
        if view_class == MainView:
            self.current_view = view_class(
                self.root, self.show_workout_view, *args)
        elif view_class == SignupView:
            self.current_view = view_class(
                self.root, self.show_login_view, self.show_main_view)
        else:
            self.current_view = view_class(self.root, *args)

        self.current_view.pack(fill=tk.BOTH, expand=True)
