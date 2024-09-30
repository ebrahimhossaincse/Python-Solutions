"""
Write a Python program using a while loop to reverse a given string.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox


# Function to reverse a string using a while loop
def reverse_string():
    # Take the string input from the user
    dialog = CustomDialog(root, title="Input", text="Enter a string to reverse:")
    user_input = dialog.result

    # Initialize the variables for the loop
    reversed_string = ""
    i = len(user_input) - 1

    # Use a while loop to reverse the string
    while i >= 0:
        reversed_string += user_input[i]
        i -= 1

    # Display the reversed string
    messagebox.showinfo("Reversed String", f"Original String: {user_input}\nReversed String: {reversed_string}")


# Call the function to reverse the string
reverse_string()