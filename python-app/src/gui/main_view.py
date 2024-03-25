import tkinter as tk
from tkinter import ttk
from gui.workout_element import WorkoutElement

class MainView(ttk.Frame):
    """
    Main view interface for the user to navigate the app.
    """
    
    def __init__(self, parent, show_workout_view):
        super().__init__(parent)
        self.parent = parent
        self.show_workout_view = show_workout_view
        self.parent.title("Main View")
        
        self.setup_ui()

    def setup_ui(self):
        # user info 
        user_info_label = ttk.Label(self, text="user info placeholder")
        user_info_label.place(x=20, y=20, width=200, height=100)

        # scrollable list 
        scroll_frame = ttk.Frame(self)
        scroll_frame.place(x=20, y=140, width=200, height=400)

        canvas = tk.Canvas(scroll_frame)
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_list = ttk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.create_window((0, 0), window=scrollable_list, anchor="nw")
        scrollable_list.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
    
        # to remove: example items 
        for i in range(10):
            item = WorkoutElement(scrollable_list, f"Item {i+1}", "Detail")
            item.pack(fill='x', expand=True, padx=5, pady=5)
        
        # graph placeholder 
        graph_placeholder = ttk.Label(self, text="Graph placeholder", background="lightgray")
        graph_placeholder.place(x=240, y=20, width=400, height=300)

        new_workout_button = ttk.Button(self, text="Add a Workout", command=self.show_workout_view)
        new_workout_button.place(x=480, y=340, width=160, height=40)
