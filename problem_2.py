'''
Write a Python program that takes an integer as input and prints whether it is even or odd.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

dialog = CustomDialog(root, title="Input", text="Please enter an integer")
num = dialog.result

if dialog.result is not None:
    try:
        num = int(dialog.result)
        result_message = f"You have entered {num} and {num} is {'even number' if num % 2 == 0 else 'odd number'}."
        messagebox.showinfo("Result", result_message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")