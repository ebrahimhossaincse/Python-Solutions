'''
Write a Python function to reverse a given string and return the reversed string.
'''
import tkinter as tk
from tkinter import simpledialog

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a custom dialog class
class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.geometry("250x100")  # Set custom size (width x height)
        tk.Label(master, text="Please enter the value:").grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=1)
        return self.entry

    def apply(self):
        self.result = (self.entry.get())  # Convert the result to an integer

# Show the custom dialog
dialog = CustomDialog(root, title="Input")

def reverse_string(s):
    return s[::-1]

input_string = dialog.result
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")
