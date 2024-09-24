'''
Write a Python function to check if a given string is a palindrome or not.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root

# Show the custom dialog and get Celsius temperature as input
dialog = CustomDialog(root, title="Input", text="Enter a String")
input_string = dialog.result


def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

