import tkinter as tk
from tkinter import ttk, messagebox
from event_handlers import login_handler

class LoginView(ttk.Frame):
    """
    Login view interface for the user to login or move to sign up window
    """

    def __init__(self, parent, show_signup, show_main):
        super().__init__(parent)
        self.show_signup = show_signup
        self.show_main = show_main

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.place(x=215, y=170, width=60, height=40)
        self.username_entry = ttk.Entry(self)
        self.username_entry.place(x=280, y=170, width=160, height=40)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.place(x=215, y=225, width=60, height=40)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.place(x=280, y=225, width=160, height=40)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.place(x=300, y=275, width=120, height=40)

        self.signup_button = ttk.Button(self, text="Sign Up", command=self.show_signup)
        self.signup_button.place(x=300, y=320, width=120, height=40)

    def login(self):
        if login_handler.login(self.username_entry.get(), self.password_entry.get()):
            self.show_main()
        else:
            messagebox.showinfo("Login Unsuccessful", "Incorrect username or password")
