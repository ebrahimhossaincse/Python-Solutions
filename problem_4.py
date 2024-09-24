'''
Given a list of integers, write a Python program to convert each element of the list to a string.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root

# Show the custom dialog
dialog = CustomDialog(root, title="Input", text="Enter a list of integers (comma-separated): ")

# Check if user input is valid
if dialog.result:
    # Split the user input and convert to a list of integers
    int_list = [int(i) for i in dialog.result.split(",")]

    # Convert each integer to a string
    str_list = [str(i) for i in int_list]

    # Print the converted list
    print('List: ',str_list)

