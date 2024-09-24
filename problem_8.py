'''
Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`,
write a Python program to perform the following operations and print the results:
– Convert `a` to an integer and add it to `b`.
– Convert `c` to a float and subtract it from the result of the first operation.
– Convert the final result to a string and concatenate it with the string ” is the answer.”
'''

# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Show the custom dialog and get Celsius temperature as input
dialog = CustomDialog(root, title="Input", text="Enter the first number: ")
a = dialog.result

dialog = CustomDialog(root, title="Input", text="Enter the second number: ")
b = dialog.result

dialog = CustomDialog(root, title="Input", text="Enter the third number: ")
c = dialog.result

# Step 1: Convert `a` and `b` to integers and add them
result_1 = int(a) + int(b)

# Step 2: Convert `c` to a float and subtract it from `result_1`
result_2 = result_1 - float(c)

# Step 3: Convert the final result to a string and concatenate it with " is the answer."
final_result = str(result_2) + " is the answer."

# Output the final result
messagebox.showinfo("Result", final_result)

