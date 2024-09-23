'''
Write a Python program that takes an integer as input and prints whether it is even or odd.
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
        tk.Label(master, text="Please enter the number:").grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=1)
        return self.entry

    def apply(self):
        self.result = int(self.entry.get())  # Convert the result to an integer

# Show the custom dialog
dialog = CustomDialog(root, title="Input")
num = dialog.result

# Check if a number was provided
if num is not None:
    # Print if the number is even or odd
    print(f"You have entered {num} and {num} is {'even' if num % 2 == 0 else 'odd'}.")
