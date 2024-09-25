"""
Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to calculate the sum of the first N natural numbers
def calculate_sum(N):
    total_sum = 0
    for num in range(1, N + 1):
        total_sum += num
    return total_sum


# Function to get the input and calculate the sum
def sum_of_natural_numbers():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter a positive integer N: ")
        N = int(dialog.result)

        if N <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        # Calculate the sum of the first N natural numbers
        result = calculate_sum(N)

        # Show the result
        messagebox.showinfo("Result", f"The sum of the first {N} natural numbers is {result}.")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Call the function to get the input and calculate the sum
sum_of_natural_numbers()