import tkinter as tk
from tkinter import ttk, simpledialog

class WorkoutView(ttk.Frame):
    """
    Workout view interface, for the user to select which movements they want to
    include in their planned workout.
    """

    def __init__(self, parent, show_main_view):
        super().__init__(parent)
        self.parent = parent
        self.show_main_view = show_main_view
        self.parent.title("WOD View")

        self.pack(fill=tk.BOTH, expand=True)
        # placeholders
        self.available_movements = ["Jogging", "Bench Press", "Squats", "Deadlift", "Pull-ups"]
        
        self.setup_ui()

    def setup_ui(self):

        self.current_workout_frame = ttk.LabelFrame(self, text="Current Workout")
        self.current_workout_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.current_workout_list = tk.Listbox(self.current_workout_frame)
        self.current_workout_list.pack(fill=tk.BOTH, expand=True)

        self.available_movements_frame = ttk.LabelFrame(self, text="Available Movements")
        self.available_movements_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.available_movements_list = tk.Listbox(self.available_movements_frame)
        self.available_movements_list.pack(fill=tk.BOTH, expand=True)

        for movement in self.available_movements:
            self.available_movements_list.insert(tk.END, movement)

        self.add_button = ttk.Button(self, text="Add to Workout", command=self.add_to_workout)
        self.add_button.pack(pady=10)

        self.return_main_button = ttk.Button(self, text="Return to Homepage", command=self.show_main_view)
        self.return_main_button.pack(pady=10)

    def add_to_workout(self):
        selection = self.available_movements_list.curselection()
        if selection:
            selected_movement = self.available_movements_list.get(selection[0])
            details = simpledialog.askstring("Input", f"Enter details for {selected_movement} (e.g., duration, sets/reps):")
            if details:
                self.current_workout_list.insert(tk.END, f"{selected_movement}: {details}")
