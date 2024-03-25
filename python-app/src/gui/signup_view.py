import tkinter as tk
from tkinter import ttk, messagebox


class SignupView(ttk.Frame):
    """
    Class implements the sign up view for the user to create a new userprofile
    """
    def __init__(self, parent, show_login, show_main):
        super().__init__(parent)
        self.show_login = show_login
        self.show_main = show_main
        self.parent = parent
        self.parent.title("Sign Up")

        self.fullname_label = ttk.Label(self, text="Full Name:")
        self.fullname_label.place(x=215, y=150, width=60, height=40)
        self.fullname_entry = ttk.Entry(self)
        self.fullname_entry.place(x=280, y=150, width=160, height=40)

        self.age_label = ttk.Label(self, text="Age:")
        self.age_label.place(x=215, y=200, width=60, height=40)
        self.age_entry = ttk.Entry(self)
        self.age_entry.place(x=280, y=200, width=160, height=40)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.place(x=215, y=250, width=60, height=40)
        self.username_entry = ttk.Entry(self)
        self.username_entry.place(x=280, y=250, width=160, height=40)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.place(x=215, y=300, width=60, height=40)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.place(x=280, y=300, width=160, height=40)

        self.password_confirm_label = ttk.Label(self, text="Confirm\nPassword:")
        self.password_confirm_label.place(x=215, y=350, width=60, height=40)
        self.password_confirm_entry = ttk.Entry(self, show="*")
        self.password_confirm_entry.place(x=280, y=350, width=160, height=40)

        self.signup_button = ttk.Button(self, text="Sign Up", command=self.signup)
        self.signup_button.place(x=300, y=400, width=120, height=40)

        self.back_button = ttk.Button(self, text="Back to Login", command=self.show_login)
        self.back_button.place(x=300, y=450, width=120, height=40)

    def signup(self):
        
        messagebox.showinfo("Signup Successful", "You have successfully signed up.")
        self.show_main()
