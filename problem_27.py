"""
Write a Python program using nested loops to multiply two matrices.
"""

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox


# Function to multiply two matrices
def matrix_multiplication():
    try:
        # Input dimensions and elements of the first matrix
        dialog = CustomDialog(root, title="Input", text="Enter the number of rows for Matrix A:")
        rows_A = int(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the number of columns for Matrix A:")
        cols_A = int(dialog.result)
        matrix_A = []

        messagebox.showinfo("Input", f"Enter the elements of Matrix A ({rows_A}x{cols_A}) row by row:")

        for i in range(rows_A):
            dialog = CustomDialog(root, title="Input", text=f"Enter row {i + 1} elements (space-separated):")
            row = dialog.result
            matrix_A.append([int(x) for x in row.split()])

        # Input dimensions and elements of the second matrix
        dialog = CustomDialog(root, title="Input", text="Enter the number of rows for Matrix B:")
        rows_B = int(dialog.result)
        dialog = CustomDialog(root, title="Input", text="Enter the number of columns for Matrix B:")
        cols_B = int(dialog.result)

        if cols_A != rows_B:
            messagebox.showerror("Error", "Matrix A's columns must equal Matrix B's rows for multiplication!")
            return

        matrix_B = []

        messagebox.showinfo("Input", f"Enter the elements of Matrix B ({rows_B}x{cols_B}) row by row:")

        for i in range(rows_B):
            dialog = CustomDialog(root, title="Input", text=f"Enter row {i + 1} elements (space-separated):")
            row = dialog.result
            matrix_B.append([int(x) for x in row.split()])

        # Initialize result matrix with zeros
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        # Perform matrix multiplication using nested loops
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += matrix_A[i][k] * matrix_B[k][j]

        # Prepare and display the result
        result_message = "Matrix A * Matrix B =\n"
        for row in result:
            result_message += ' '.join(map(str, row)) + '\n'

        messagebox.showinfo("Result", result_message)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter integers only.")


# Call the function to multiply matrices
matrix_multiplication()