"""
Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to calculate the sum of even numbers between 1 and N
def sum_of_even_numbers(N):
    sum_even = 0
    i = 2  # Start with the first even number
    while i <= N:
        sum_even += i
        i += 2  # Move to the next even number
    return sum_even

# Function to get the input and calculate the sum of even numbers
def calculate_sum_of_even():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter an integer N:")
        N = int(dialog.result)

        if N < 1:
            messagebox.showerror("Error", "Please enter a positive integer greater than 0.")
            return

        # Calculate the sum of even numbers between 1 and N
        result = sum_of_even_numbers(N)

        # Show the result
        messagebox.showinfo("Sum of Even Numbers", f"The sum of even numbers between 1 and {N} is: {result}")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Call the function to get the input and calculate the sum of even numbers
calculate_sum_of_even()