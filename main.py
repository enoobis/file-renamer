import os
from tkinter import *
from tkinter import filedialog

# Function to browse for folder
def browse_folder():
    path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, path)

# Function to rename files
def rename_files():
    path = path_entry.get() # Get the path of the folder
    prefix = prefix_entry.get() # Get the prefix
    extension = extension_entry.get() # Get the extension (if any)
    only_extension = extension_checkbox_var.get() # Check if only files with the extension should be renamed
    count = 1
    for file_name in os.listdir(path):
        # Rename the file with the new name
        if only_extension and not file_name.endswith("." + extension):
            continue # Skip files that don't have the specified extension
        if extension:
            new_name = prefix + str(count) + "." + extension
        else:
            new_name = prefix + str(count)
        os.rename(os.path.join(path, file_name), os.path.join(path, new_name))
        count += 1
    # Clear the entry fields
    path_entry.delete(0, END)
    prefix_entry.delete(0, END)
    extension_entry.delete(0, END)
    extension_checkbox.deselect()

# Create the GUI
root = Tk()
root.title("File Renamer")
root.config(bg="#24292e") # Set the background color to a dark gray

# Set the color scheme for the widgets
label_fg = "#c9d1d9" # Light gray
entry_fg = "#24292e" # Dark gray
button_fg = "#fff" # White
button_bg = "#2ea44f" # Green
checkbutton_fg = "#c9d1d9" # Light gray
checkbutton_bg = "#24292e" # Dark gray

# Add a label and entry for the path
path_label = Label(root, text="Enter the path of the folder:", fg=label_fg, bg="#24292e")
path_label.grid(row=0, column=0, padx=5, pady=5)
path_entry = Entry(root, width=30, fg=entry_fg, bg="#fff")
path_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = Button(root, text="Browse", fg=button_fg, bg=button_bg, command=browse_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Add a label and entry for the prefix
prefix_label = Label(root, text="Enter the prefix for the files:", fg=label_fg, bg="#24292e")
prefix_label.grid(row=1, column=0, padx=5, pady=5)
prefix_entry = Entry(root, width=30, fg=entry_fg, bg="#fff")
prefix_entry.grid(row=1, column=1, padx=5, pady=5)

# Add a label and entry for the extension
extension_label = Label(root, text="Enter the file extension (optional):", fg=label_fg, bg="#24292e")
extension_label.grid(row=2, column=0, padx=5, pady=5)
extension_entry = Entry(root, width=10, fg=entry_fg, bg="#fff")
extension_entry.grid(row=2, column=1, padx=5, pady=5)

# Add a checkbox to rename only files with the specified extension
extension_checkbox_var = IntVar()
extension_checkbox = Checkbutton(root, text="Rename only files with the specified extension", fg=checkbutton_fg, bg=checkbutton_bg, variable=extension_checkbox_var)
extension_checkbox.grid(row=3, column=1, padx=5, pady=5)

#Add a button to rename the files
rename_button = Button(root, text="Rename Files", fg=button_fg, bg=button_bg, command=rename_files)
rename_button.grid(row=4, column=1, padx=5, pady=5)

#run
root.mainloop()
