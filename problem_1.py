'''
Write a Python program to swap the values of two variables without using a temporary variable.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

dialog = CustomDialog(root, title="Input", text="Please enter the first variable value: ")
a = dialog.result

dialog = CustomDialog(root, title="Input", text="Please enter the second variable value: ")
b = dialog.result

messagebox.showwarning("Info", f"Before swapping: a = {a}, b = {b}")

# Swapping values without using a temporary variable
a, b = b, a

messagebox.showinfo("Result", f"After swapping: a = {a}, b = {b}")

