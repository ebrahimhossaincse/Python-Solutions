"""
Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to generate the Fibonacci sequence up to a given limit N
def fibonacci_sequence(N):
    sequence = []
    a, b = 0, 1
    while a <= N:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Function to get the input and display the Fibonacci sequence
def generate_fibonacci_sequence():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title='Input', text="Enter the limit N for the Fibonacci sequence")
        N = int(dialog.result)

        if N < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
            return

        # Generate the Fibonacci sequence up to N
        result = fibonacci_sequence(N)

        # Format the result as a string
        result_str = ', '.join(map(str, result))

        # Show the result
        messagebox.showinfo("Fibonacci Sequence", f"The Fibonacci sequence up to {N} is:\n{result_str}")
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")

# Call the function to get the input and generate the Fibonacci sequence
generate_fibonacci_sequence()
