"""
Starts the app  by creating a root and running the app.py to initialize
the user interface.
"""

import tkinter as tk
from app import MainApp

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
