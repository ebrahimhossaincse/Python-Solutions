import tkinter as tk
from tkinter import simpledialog

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a custom dialog class
class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, text=""):
        self.text = text  # Store the label text
        super().__init__(parent, title=title)

    def body(self, master):
        self.geometry("300x100")  # Set custom size (width x height)
        tk.Label(master, text=self.text).grid(row=0)  # Display custom label text
        self.entry = tk.Entry(master)
        self.entry.grid(row=1)
        return self.entry

    def apply(self):
        self.result = self.entry.get()  # Get the user input as a string
