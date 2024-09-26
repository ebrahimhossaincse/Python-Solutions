"""Write a Python program using a while loop to check if a given number N is prime or not."""

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to check if a number is prime
def is_prime(N):
    if N <= 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


# Function to get the input and check if the number is prime
def check_prime():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter an integer N:")
        N = int(dialog.result)

        if N < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
            return

        # Check if N is prime
        result = is_prime(N)

        # Show the result
        if result:
            messagebox.showinfo("Prime Check", f"The number {N} is a prime number.")
        else:
            messagebox.showinfo("Prime Check", f"The number {N} is not a prime number.")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Call the function to get the input and check if the number is prime
check_prime()