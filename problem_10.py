'''
Write a Python program that takes three numbers as input and prints the largest among them.
'''

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

def find_largest(a, b, c):
    return max(a, b, c)


# Function to take three inputs and find the largest
def get_largest_number():
    try:
        # Take input from the user
        dialog = CustomDialog(root, title="Input", text="Enter the first number: ")
        num1 = float(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the second number: ")
        num2 = float(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the third number: ")
        num3 = float(dialog.result)

        # Find the largest number
        largest = find_largest(num1, num2, num3)

        # Show the result in a message box
        messagebox.showinfo("Result", f"The largest number is {largest}.")
    except ValueError:
        # Handle the case where the input is not valid
        messagebox.showerror("Error", "Please enter valid numbers.")


# Call the function to get inputs and display the largest number
get_largest_number()