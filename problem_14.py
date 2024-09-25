'''
Write a Python program that takes the time in hours (24-hour format) as input
and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to determine the appropriate greeting based on time
def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    elif (21 <= hour <= 23) or (0 <= hour < 5):
        return "Good Night"
    else:
        return "Invalid time"


# Function to get the time input and display the appropriate greeting
def check_greeting():
    try:
        # Take the hour input from the user
        dialog = CustomDialog(root, title="Input", text="Enter the time in hours (0-23): ")
        hour = int(dialog.result)

        # Ensure the hour is valid (between 0 and 23)
        if 0 <= hour <= 23:
            greeting = get_greeting(hour)
            messagebox.showinfo("Greeting", greeting)
        else:
            messagebox.showerror("Error", "Please enter a valid hour between 0 and 23.")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid number for hours.")


# Call the function to get the input and display the greeting
check_greeting()