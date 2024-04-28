import tkinter as tk
import datetime
from tkinter import ttk
from gui.workout_element import WorkoutElement
from gui.pillar_chart import PillarChart
from event_handlers.login_handler import LoginManager
from event_handlers.json_manager import JsonManager
from event_handlers.session_manager import Session


class MainView(ttk.Frame):
    """
    Main view interface for the user to navigate the app.
    """

    def __init__(self, parent, show_workout_view):
        """
        Constructor for the view

        Args:
            parent: tkinter widget where view is displayed 
            show_workout_view: method to switch the view
        """
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
        """
        Sets up the elements for a mainview for the app. 
        Places a user info label, a scrollable list and a pillar chart graph to the view.
        """
        style = ttk.Style()
        style.configure('Info.TLabel', font=('Segoe UI', 12, 'bold'),
                        foreground='black', background='#f7efd7',
                        padding=(10, 10), relief='raised')
        style.configure('Describtion.TLabel', font=('Segoe UI', 10, 'bold'),
                        foreground='black', background='#f7efd7', padding=(10, 10))

        user_info_label = ttk.Label(self, text=(
            f"Name:  {self.user.name}\n"
            f"Age:  {self.user.age}\n"
            f"Workouts logged:  {len(self.user.workouts)}"), style='Info.TLabel')

        user_info_label.place(x=20, y=20, width=250, height=100)

        self.setup_list_view()

        self.graph = PillarChart(self, 300, width=400, height=300)
        self.graph.place(x=370, y=20, width=400, height=300)
        self.load_chart_data()

        description_label = ttk.Label(self, text=("Workout history visualized by months:"),
                                                    style='Describtion.TLabel')
        description_label.place(x=360, y=330, width=300, height=40)

        detailed_view_button = ttk.Button(
            self, text="Complete History", command=self.open_scrollable_window)
        detailed_view_button.place(x=420, y=400, width=160, height=40)

        new_workout_button = ttk.Button(
            self, text="Add a Workout", command=self.show_workout_view)
        new_workout_button.place(x=420, y=460, width=160, height=40)


    def setup_list_view(self):
        """
        Sets up the list view for recent workouts
        """
        frame = ttk.Frame(self)
        frame.place(x=20, y=140, width=300, height=395)

        canvas = tk.Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)
        
        list_view = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=list_view, anchor="nw")
        
        self.populate_list_view(list_view)


    def populate_list_view(self, list_view):
        """
        Loops the workout data and add's the 7 or fewest most recent entries to the view

        Args:
            list_view: the frame where the elements are being displayed in
        """
        for i in range(min(7, len(self.workout_data))):
            workout = self.workout_data[-i-1]
            formatted_date = workout.date.strftime("%Y-%m-%d")
            item = WorkoutElement(
                list_view, f"Date: {formatted_date}", "\n".join(workout.content))
            item.pack(fill='x', expand=True, padx=5, pady=5)

        list_view.update_idletasks()


    def load_user_data(self):
        """
        Uses json manager class to fetch user workout data 
        """
        self.workout_data = []
        self.workout_data = self.json_manager.load_workouts(
            Session.get_current_user())


    def load_chart_data(self):
        """
        Initializes the graphical pillar charts construction by calling its
        helper methods  
        """
        data = self.count_recent_workouts()
        months = ['Two months ago', 'Last month', 'This month']

        self.graph.update_data(months, data)


    def open_scrollable_window(self):
        """
        Opens a separate window for the user to view their entire workoutdata
        """
        history_window = tk.Toplevel(self)
        history_window.title("Complete History")
        canvas = tk.Canvas(history_window, borderwidth=0)

        frame = ttk.Frame(canvas)
        scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        for workout in reversed(self.workout_data):
            formatted_date = workout.date.strftime("%Y-%m-%d")
            item = WorkoutElement(frame, f"Date: {formatted_date}", "\n".join(workout.content))
            item.pack(fill='x', expand=True, padx=5, pady=5)

        frame.bind("<Configure>", lambda event,
                    canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
        
        
    def count_recent_workouts(self):
        """
        Counts the workout frequency from past months

        Returns:
            The count for each of three past months
        """
        now = datetime.datetime.now()
        
        this_month = 0
        last_month = 0
        two_months_ago = 0

        for workout in reversed(self.workout_data):
            workout_date = workout.date
            
            if now.year == workout_date.year and now.month == workout_date.month:
                this_month += 1

            elif now.year == workout_date.year and now.month - 1 == workout_date.month:
                last_month += 1
                
            elif now.year == workout_date.year and now.month - 2 == workout_date.month:
                two_months_ago += 1

            elif workout_date.month - now.month <= -4:
                break
        
        return [two_months_ago, last_month, this_month]
    