from tkinter import ttk

class WorkoutElement(ttk.Frame):
    """
    A custom widget for previous workouts list, item that can be clicked to expand
    on the list

    Attributes:
        parent: widget where the element is displayed on
        text: 
        detail:
        expanded:
    """
    def __init__(self, parent, text, detail, *args, **kwargs):
        """Constructor for the class

        Args:
            parent: widget or element where the object is imposed on
            text: the title for the workout
            detail: workout details
            *args: 
            **kwargs:
        """
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.text = text
        self.detail = detail
        self.expanded = False

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        """
        Configures the workout widgets
        """
        self.label = ttk.Label(self, text=self.text, style='Title.TLabel')
        self.label.pack(pady=5, padx=10, anchor='w')
        self.label.bind("<Button-1>", self.toggle_detail)

        self.detail_label = ttk.Label(self, text=self.detail, style='Detail.TLabel')
        self.detail_label.pack(pady=5, padx=20, anchor='w')
        self.detail_label.pack_forget()

    def style_widgets(self):
        """
        Adds styling to the text 
        """
        style = ttk.Style()
        style.configure(
            'Title.TLabel', font=('Roboto', 14, 'bold'),
              foreground='#0d1c02', background='#a1bd8e')
        style.configure(
            'Detail.TLabel', font=('Arial', 11), foreground='black', background='#eafade')

    def toggle_detail(self, event):
        """
        Allows the workout to be expanded and collapsed when clicked
        """
        if self.expanded:
            self.detail_label.pack_forget()
        else:
            self.detail_label.pack(pady=5, padx=20, anchor='w')
        self.expanded = not self.expanded
