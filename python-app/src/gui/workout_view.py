import tkinter as tk
from tkinter import ttk, simpledialog
from datetime import datetime
from event_handlers.json_manager import JsonManager
from event_handlers.session_manager import Session
from objects import workout


class WorkoutView(ttk.Frame):
    """
    implements the workout pick, choose and edit view for the user
    """

    def __init__(self, parent, show_main_view):
        super().__init__(parent)
        self.parent = parent
        self.show_main_view = show_main_view
        self.parent.title("WOD View")
        self.pack(fill=tk.BOTH, expand=True)

        self.current_category = tk.StringVar(value="Select Category")
        self.available_movements = []

        self.json_manager = JsonManager()
        self.username = Session.get_current_user()
        self.user = self.json_manager.load_user(self.username)

        self.load_movements()
        self.setup_ui()

    def setup_ui(self):
        self.category_menu = ttk.Combobox(
            self, textvariable=self.current_category,
            values=["Select Category", "Upper Body",
                    "Lower Body", "Cardio", "Accessories", "Other"],
            state="readonly")
        self.category_menu.pack(pady=10)
        self.category_menu.bind("<<ComboboxSelected>>",
                                self.update_movements_list)

        self.current_workout_frame = ttk.LabelFrame(
            self, text="Current Workout")
        self.current_workout_frame.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.current_workout_list = tk.Listbox(self.current_workout_frame)
        self.current_workout_list.pack(fill=tk.BOTH, expand=True)

        self.available_movements_frame = ttk.LabelFrame(
            self, text="Available Movements")
        self.available_movements_frame.pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.available_movements_list = tk.Listbox(
            self.available_movements_frame)
        self.available_movements_list.pack(fill=tk.BOTH, expand=True)

        self.available_movements_list.insert(tk.END, self.instructions)

        self.add_button = ttk.Button(
            self, text="Add to Workout", command=self.add_to_workout)
        self.add_button.pack(pady=10)

        self.save_button = ttk.Button(
            self, text="Save Workout", command=self.save_workout)
        self.save_button.pack(pady=10)

        self.return_main_button = ttk.Button(
            self, text="Return to Homepage", command=self.show_main_view)
        self.return_main_button.pack(pady=10)

    def load_movements(self):
        """
        Loads movements from a JSON file
        """
        self.all_movements = {}
        self.all_movements = self.json_manager.load_categories()
        self.instructions = self.all_movements.get("instructions")

    def update_movements_list(self, event):
        """
        Updates the movements list based on the selected category
        """
        selected_category = self.current_category.get()
        if selected_category == "Select Category":
            self.available_movements_list.delete(0, tk.END)
            self.available_movements_list.insert(tk.END, self.instructions)
            return

        category_map = {
            "Upper Body": "upper_body_movements",
            "Lower Body": "lower_body_movements",
            "Cardio": "cardio_options",
            "Accessories": "accessory_exercises",
            "Other": "other_workout_options"
        }
        key = category_map.get(selected_category, "")
        movements = self.all_movements.get(key, [])

        self.available_movements_list.delete(0, tk.END)
        for movement in movements:
            self.available_movements_list.insert(tk.END, movement)

    def add_to_workout(self):
        """
        Adds the selected movement and details to the current workout list
        """
        selection = self.available_movements_list.curselection()
        if selection:
            selected_movement = self.available_movements_list.get(selection[0])
            details = simpledialog.askstring("Input", f"Enter details for {
                                             selected_movement} (e.g., duration, sets/reps):")
            if details:
                self.current_workout_list.insert(
                    tk.END, f"{selected_movement}: {details}")

    def save_workout(self):
        """
        Saves the generated workout to a json
        """
        content = [self.current_workout_list.get(
            idx) for idx in range(self.current_workout_list.size())]
        if content:
            current_date = datetime.now().strftime('%Y-%m-%d')
            wod = workout.Workout(self.user.username, current_date, content)
            self.json_manager.save_workout_json(wod)
            return True
        return False

    def save_button_pressed(self):
        if not self.save_workout():
            self.show_message("Failed to save",
                              "Add exercises to the workout before saving")
        else:
            self.show_message("Success", "Workout saved successfully!")

    def show_message(self, title, message):
        tk.messagebox.showwarning(title, message)
