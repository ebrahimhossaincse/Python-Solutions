"""
Write a Python program using a for loop to print the multiplication table of a given number N.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to generate the multiplication table using a for loop
def multiplication_table(N):
    table = ""
    for i in range(1, 11):
        table += f"{N} x {i} = {N * i}\n"
    return table


# Function to get the input and print the multiplication table
def print_multiplication_table():
    try:
        # Take the value of N as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter an integer N:")
        N = int(dialog.result)

        # Generate the multiplication table for N
        result = multiplication_table(N)

        # Show the result
        messagebox.showinfo("Multiplication Table", result)
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")

# Call the function to get the input and print the multiplication table
print_multiplication_table()