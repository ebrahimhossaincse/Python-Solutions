'''
Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Show the custom dialog and get Celsius temperature as input
dialog = CustomDialog(root, title="Input", text="Enter a number: ")
number = dialog.result

# Function to check if a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

result = check_number(int(number))
messagebox.showinfo("Result", f"The number {number} is {result}.")
