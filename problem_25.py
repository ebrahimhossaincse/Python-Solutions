"""
Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.
"""
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox


# Function to compute the sum, average, max, and min values
def calculate_list_statistics():
    # Take a list of integers as input from the user
    dialog = CustomDialog(root, title="Input", text="Enter a list of integers (comma-separated):")
    user_input = dialog.result

    try:
        # Convert the user input into a list of integers
        int_list = [int(x.strip()) for x in user_input.split(',')]

        # Initialize sum, max, and min values
        total_sum = 0
        max_value = int_list[0]
        min_value = int_list[0]

        # Use a for loop to calculate sum, max, and min
        for num in int_list:
            total_sum += num
            if num > max_value:
                max_value = num
            if num < min_value:
                min_value = num

        # Calculate the average
        average_value = total_sum / len(int_list)

        # Display the results in a message box
        result_message = (
            f"Sum: {total_sum}\n"
            f"Average: {average_value:.2f}\n"
            f"Maximum: {max_value}\n"
            f"Minimum: {min_value}"
        )
        messagebox.showinfo("List Statistics", result_message)

    except ValueError:
        # Handle the case where the input is not valid
        messagebox.showerror("Error", "Please enter a valid list of integers.")


# Call the function to compute the statistics
calculate_list_statistics()