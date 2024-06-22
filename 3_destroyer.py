import tkinter as tk
from tkinter import filedialog
import shutil
import os

# Function to delete contents of a folder
def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Function to handle button click
def select_folders_and_delete():
    selected_folders = []
    while True:
        folder = filedialog.askdirectory()
        if not folder:
            break  # User canceled or closed the dialog
        selected_folders.append(folder)

    # Delete contents of each selected folder
    for folder in selected_folders:
        delete_folder_contents(folder)
        print(f"Contents of {folder} deleted.")

# Create main window
root = tk.Tk()
root.title("Folder Content Deletion App")

# Create button to select folders
select_button = tk.Button(root, text="Select Folders", command=select_folders_and_delete)
select_button.pack(pady=20)

# Run the application
root.mainloop()
