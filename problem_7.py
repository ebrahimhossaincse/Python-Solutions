'''
Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root

# Show the custom dialog and get Celsius temperature as input
dialog = CustomDialog(root, title="Input", text="Enter the first string: ")
string1 = dialog.result

dialog = CustomDialog(root, title="Input", text="Enter the second string: ")
string2 = dialog.result

def concatenate_strings(str1, str2):
    return f"{str1}{str2}"

concatenated_string = concatenate_strings(string1, string2)
print(f"Concatenated string: {concatenated_string}")

