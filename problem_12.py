'''
Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria:
– 90% or above: A+
– 80-89%: A
– 70-79%: B
– 60-69%: C
– Below 60%: Fail
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to determine the grade based on percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

# Function to get the student's percentage and display the grade
def check_grade():
    try:
        # Take the percentage as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter the student's percentage:")
        percentage = float(dialog.result)

        # Check if percentage is within valid range (0 to 100)
        if 0 <= percentage <= 100:
            grade = get_grade(percentage)
            messagebox.showinfo("Result", f"The student's grade is: {grade}")
        else:
            messagebox.showerror("Error", "Please enter a valid percentage between 0 and 100.")
    except ValueError:
        # Handle the case where the input is not a valid number
        messagebox.showerror("Error", "Please enter a valid percentage.")


# Call the function to get the input and check for grade
check_grade()