"""
Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input
and calculates and prints the real roots (if they exist) or a message indicating the complex roots.
"""

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox
import math

# Function to calculate the roots of a quadratic equation
def calculate_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return f"Complex roots: {real_part} ± {imaginary_part}i"


# Function to get the coefficients input and display the roots
def solve_quadratic():
    try:
        # Take the coefficients as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter coefficient a (non-zero):")
        a = float(dialog.result)
        if a == 0:
            messagebox.showerror("Error", "Coefficient a cannot be zero in a quadratic equation.")
            return
        dialog = CustomDialog(root, title="Input", text="Enter coefficient b:")
        b = float(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter coefficient c:")
        c = float(dialog.result)

        # Calculate the roots of the quadratic equation
        result = calculate_roots(a, b, c)

        # Show the result
        messagebox.showinfo("Result", result)
    except ValueError:
        # Handle the case where the input is not a valid number
        messagebox.showerror("Error", "Please enter valid numbers for the coefficients.")


# Call the function to get the input and calculate the roots
solve_quadratic()