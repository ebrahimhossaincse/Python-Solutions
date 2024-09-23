'''
Write a Python program to swap the values of two variables without using a temporary variable.
'''

import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

a = simpledialog.askstring("Input", "Please enter the first variable value: ")
b = simpledialog.askstring("Input", "Please enter the second variable value: ")

# Swapping values without using a temporary variable
a, b = b, a

# Output the swapped values
print(f"After swapping: a = {a}, b = {b}")

