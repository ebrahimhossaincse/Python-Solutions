"""
Write a Python program to find the sum of all elements in a given list of integers.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to calculate the sum of all elements in a list
def sum_of_list():
    try:
        # Input the list from the user
        dialog = CustomDialog(root, title="Input", text="Enter a list of integers (comma-separated):")
        input_list = dialog.result
        integer_list = [int(x) for x in input_list.split(",")]  # Convert input to a list of integers

        # Calculate the sum of the list
        total_sum = sum(integer_list)

        # Display the result in a messagebox
        messagebox.showinfo("Result", f"The sum of the elements in the list is: {total_sum}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")


# Call the function to calculate the sum
sum_of_list()