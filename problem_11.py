'''
Write a Python program that takes a year as input and determines if it is a leap year or not.
'''

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to determine if a year is a leap year
def is_leap_year(year):
    # A leap year is divisible by 4, but not by 100, unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    try:
        # Take the year input from the user
        dialog = CustomDialog(root, title="Input", text="Enter a year: ")
        year = int(dialog.result)
        # Determine if the year is a leap year
        if is_leap_year(year):
            messagebox.showinfo("Result", f"{year} is a leap year.")
        else:
            messagebox.showinfo("Result", f"{year} is not a leap year.")
    except ValueError:
        # Handle the case where the input is not a valid year
        messagebox.showerror("Error", "Please enter a valid year.")

# Call the function to get the input and check for leap year
check_leap_year()