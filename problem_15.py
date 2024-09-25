'''
Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to determine the type of triangle
def check_triangle_type(a, b, c):
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a valid triangle"


# Function to get the sides input and display the type of triangle
def check_triangle():
    try:
        # Take the sides of the triangle as input from the user
        dialog = CustomDialog(root, title="Input", text="Enter the length of the first side:")
        a = float(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the length of the second side:")
        b = float(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the length of the third side:")
        c = float(dialog.result)

        # Determine the type of triangle
        triangle_type = check_triangle_type(a, b, c)

        # Show the result
        messagebox.showinfo("Result", f"The triangle is: {triangle_type}")
    except ValueError:
        # Handle the case where the input is not a valid number
        messagebox.showerror("Error", "Please enter valid numbers for the sides of the triangle.")

# Call the function to get the input and check the triangle type
check_triangle()