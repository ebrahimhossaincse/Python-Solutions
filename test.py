import calendar
# Import the custom dialog from the other module
from custom_dialog import CustomDialog, root, messagebox

dialog = CustomDialog(root, title="Input", text="Enter the year: ")
year = int(dialog.result)
dialog = CustomDialog(root, title="Input", text="Enter the month in number: ")
month = int(dialog.result)
messagebox.showinfo("Calendar", calendar.month(year,month))
