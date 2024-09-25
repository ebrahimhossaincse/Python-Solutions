"""
Write a Python program using a while loop to calculate the factorial of a given number N
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to calculate the factorial using a while loop
def calculate_factorial(N):
    factorial = 1
    while N > 0:
        factorial *= N
        N -= 1
    return factorial

# Function to get the input and calculate the factorial
def factorial_of_number():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter a non-negative integer N:")
        N = int(dialog.result)
        if N < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
            return

        # Calculate the factorial of the number N
        result = calculate_factorial(N)

        # Show the result
        messagebox.showinfo("Result", f"The factorial of {N} is {result}.")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")

# Call the function to get the input and calculate the factorial
factorial_of_number()