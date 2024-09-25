"""
Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to print a right-angled triangle pattern
def right_angled_triangle(n):
    pattern = ""
    for i in range(1, n + 1):
        pattern += '*' * i + '\n'
    return pattern


# Function to print an inverted right-angled triangle pattern
def inverted_right_angled_triangle(n):
    pattern = ""
    for i in range(n, 0, -1):
        pattern += '*' * i + '\n'
    return pattern


# Function to print a pyramid pattern
def pyramid(n):
    pattern = ""
    for i in range(1, n + 1):
        pattern += ' ' * (n - i) + '*' * (2 * i - 1) + '\n'
    return pattern


# Function to print all patterns
def print_patterns():
    try:
        # Take the number of rows as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter the number of rows for the pattern:")
        n = int(dialog.result)

        if n < 1:
            messagebox.showerror("Error", "Please enter a positive integer greater than 0.")
            return

        # Generate patterns
        right_triangle = right_angled_triangle(n)
        inverted_triangle = inverted_right_angled_triangle(n)
        pyramid_pattern = pyramid(n)

        # Display patterns in message boxes
        messagebox.showinfo("Right-Angled Triangle", right_triangle)
        messagebox.showinfo("Inverted Right-Angled Triangle", inverted_triangle)
        messagebox.showinfo("Pyramid", pyramid_pattern)
    except ValueError:
        # Handle the case where the input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Call the function to get the input and display the patterns
print_patterns()