import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_files(directory):
    """
    Organize files in the given directory into subdirectories based on file type.

    Parameters:
    directory (str): The path of the directory to organize.
    """
    file_types = {
        'TextFiles': ['.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz']
    }

    # Create subdirectories if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files into subdirectories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

    messagebox.showinfo("Success", "Files have been organized successfully!")


def browse_directory():
    """
    Open a directory selection dialog and organize files in the selected directory.
    """
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)


# Create main window
root = tk.Tk()
root.title("File Organizer")

# Create and place widgets
label = tk.Label(root, text="Select a directory to organize files:")
label.pack(pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=10)

# Run the main loop
root.mainloop()
