import tkinter as tk
from tkinter import ttk
from gui.workout_element import WorkoutElement
from event_handlers.login_handler import LoginManager
from event_handlers.json_manager import JsonManager
from event_handlers.session_manager import Session


class MainView(ttk.Frame):
    """
    Main view interface for the user to navigate the app.
    """

    def __init__(self, parent, show_workout_view):
        super().__init__(parent)
        self.parent = parent
        self.show_workout_view = show_workout_view
        self.parent.title("Main View")

        self.login_handler = LoginManager()
        self.json_manager = JsonManager()
        self.username = Session.get_current_user()

        self.user = self.json_manager.load_user(self.username)
        self.load_user_data()
        self.setup_ui()

    def setup_ui(self):
        # user info
        user_info_label = ttk.Label(self, text=(
            f"Name: {self.user.name}\n"
            f"Age: {self.user.age}\n"
            f"Workouts logged: {len(self.user.workouts)}"))

        user_info_label.place(x=20, y=20, width=200, height=100)

        # scrollable list
        scroll_frame = ttk.Frame(self)
        scroll_frame.place(x=20, y=140, width=200, height=400)

        canvas = tk.Canvas(scroll_frame)
        scrollbar = ttk.Scrollbar(
            scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_list = ttk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.create_window((0, 0), window=scrollable_list, anchor="nw")
        scrollable_list.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        for workout in self.workout_data:
            formatted_date = workout.date.strftime("%Y-%m-%d")
            item = WorkoutElement(scrollable_list, f"Date: {
                                  formatted_date}", "\n".join(workout.content))
            item.pack(fill='x', expand=True, padx=5, pady=5)

        # graph placeholder
        graph_placeholder = ttk.Label(
            self, text="Graph placeholder", background="lightgray")
        graph_placeholder.place(x=240, y=20, width=400, height=300)

        new_workout_button = ttk.Button(
            self, text="Add a Workout", command=self.show_workout_view)
        new_workout_button.place(x=480, y=340, width=160, height=40)

    def load_user_data(self):
        self.workout_data = []
        self.workout_data = self.json_manager.load_workouts(
            Session.get_current_user())
