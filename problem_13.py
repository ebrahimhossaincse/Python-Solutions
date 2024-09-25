'''
Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.
'''
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

# Function to determine if a character is a vowel or a consonant
def check_vowel_or_consonant(char):
    vowels = 'AEIOUaeiou'
    if len(char) == 1 and char.isalpha():  # Ensure it's a single alphabetic character
        if char in vowels:
            return "vowel"
        else:
            return "consonant"
    else:
        return "invalid input"


# Function to get the character input and display the result
def check_character():
    try:
        # Take the character input from the user
        dialog = CustomDialog(root, title="Input", text="Enter a character")
        char = dialog.result

        # Check if it's a vowel or consonant
        result = check_vowel_or_consonant(char)

        # Show the result
        if result == "invalid input":
            messagebox.showerror("Error", "Please enter a valid single alphabetic character.")
        else:
            messagebox.showinfo("Result", f"The character '{char}' is a {result}.")
    except ValueError:
        # Handle unexpected errors
        messagebox.showerror("Error", "An unexpected error occurred.")


# Call the function to get the input and check if it's a vowel or consonant
check_character()