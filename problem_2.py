'''
Write a Python program that takes an integer as input and prints whether it is even or odd.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root

dialog = CustomDialog(root, title="Input", text="Please enter an integer")
num = dialog.result

# Check if a number was provided
if num is not None:
    # Print if the number is even or odd
    print(f"You have entered {num} and {num} is {'even' if num % 2 == 0 else 'odd'}.")
