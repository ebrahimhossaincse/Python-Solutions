'''
Write a Python function to reverse a given string and return the reversed string. / Write a Python function to reverse a given string using slicing.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Show the custom dialog
dialog = CustomDialog(root, title="Input", text="Please enter a value")

def reverse_string(s):
    return s[::-1]

input_string = dialog.result
reversed_string = reverse_string(input_string)
messagebox.showinfo("Result", f"Reversed string: {reversed_string}")