"""
Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to check the range of the number
def check_range(number):
    if 0 <= number <= 50:
        return "The number is in the range of 0-50."
    elif 51 <= number <= 100:
        return "The number is in the range of 51-100."
    elif 101 <= number <= 150:
        return "The number is in the range of 101-150."
    elif number > 150:
        return "The number is above 150."
    else:
        return "The number is negative and not in any defined range."


# Function to get the number input and display the range
def check_number_range():
    try:
        # Take the number input from the user
        dialog = CustomDialog(root, title="Input", text="Enter a number")
        number = int(dialog.result)

        # Determine the range of the number
        result = check_range(number)

        # Show the result
        messagebox.showinfo("Result", result)
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Call the function to get the input and check the number range
check_number_range()