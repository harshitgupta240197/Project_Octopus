import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

# Function to process each CSV file
def process_csv(file_path, server_name, date):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Add the 'Server' and 'Date' columns
    df['Server'] = server_name
    df['Date'] = date
    
    return df

# Function to get folder paths and file name from user
def get_user_inputs():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get folder paths
    folders = []
    for i in range(4):
        folder_path = filedialog.askdirectory(title=f"Select Folder {i+1}")
        if not folder_path:
            raise ValueError(f"Folder {i+1} selection was canceled. Exiting.")
        folders.append(folder_path)
    
    # Get common file name
    file_name = simpledialog.askstring("Input", "Enter the common CSV file name (including extension):")
    if not file_name:
        raise ValueError("File name input was canceled. Exiting.")
    
    # Get date
    date = simpledialog.askstring("Input", "Enter the date (dd-mm-yyyy):")
    if not date:
        raise ValueError("Date input was canceled. Exiting.")
    
    return folders, file_name, date

# Main function to create the master file
def create_master_file():
    try:
        directories, csv_filename, date = get_user_inputs()
        server_names = ['AM-Prod-Web01', 'AM-Prod-Web02', 'AM-Prod-Web03', 'AM-Prod-Web04']

        # List to hold the DataFrames
        dataframes = []

        # Process each file in the respective directories
        for directory, server in zip(directories, server_names):
            file_path = os.path.join(directory, csv_filename)
            df = process_csv(file_path, server, date)
            dataframes.append(df)

        # Concatenate all DataFrames into one master DataFrame
        master_df = pd.concat(dataframes, ignore_index=True)

        # Reorder columns as required
        master_df = master_df[['Server', 'Date', 'Client subdomain', 'Request URL', 'Request Method', 'Logged in user email ID', 'Start time', 'End time', 'Total Time']]

        # Save the master DataFrame to a new CSV file
        master_df.to_csv('master_file.csv', index=False)

        print("Master file created successfully!")

    except ValueError as ve:
        print(ve)

# Run the script
if __name__ == "__main__":
    create_master_file()
