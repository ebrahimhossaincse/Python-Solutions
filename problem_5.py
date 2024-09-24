'''
Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Show the custom dialog and get Celsius temperature as input
dialog = CustomDialog(root, title="Input", text="Enter temperature in Celsius: ")

# Ensure the input is not empty and convert to float
celsius_input = dialog.result
if celsius_input:
    try:
        celsius = float(celsius_input)
    except ValueError:
        messagebox.showinfo("Result", "Invalid input! Please enter a valid number.")
    else:
        # Function to convert Celsius to Fahrenheit
        def celsius_to_fahrenheit(celsius):
            return (celsius * 9/5) + 32

        fahrenheit = celsius_to_fahrenheit(celsius)
        messagebox.showinfo("Result", f"{celsius}°C is equal to {fahrenheit}°F")
else:
    messagebox.showinfo("Result", "No input provided.")

