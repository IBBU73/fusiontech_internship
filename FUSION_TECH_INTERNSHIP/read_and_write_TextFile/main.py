import tkinter as tk
from tkinter import filedialog, messagebox
import os

def read_names_from_file(input_file):
    """Read names from input file."""
    try:
        with open(input_file, 'r') as file:
            names = file.readlines()
        return [name.strip() for name in names]
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{input_file}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    return []

def write_names_to_file(sorted_names, output_file):
    """Write sorted names to output file."""
    try:
        with open(output_file, 'w') as file:
            for name in sorted_names:
                file.write(name + '\n')
        messagebox.showinfo("Success", f"Names have been sorted and written to {output_file} successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to {output_file}: {str(e)}")

def sort_and_write_names(input_file, output_file):
    """Sort names from input file and write to output file."""
    names = read_names_from_file(input_file)
    if names:
        names.sort()
        write_names_to_file(names, output_file)

def browse_input_file():
    """Browse and select the input file."""
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        entry_input_file.delete(0, tk.END)
        entry_input_file.insert(0, filename)

def browse_output_file():
    """Browse and select the output file."""
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        entry_output_file.delete(0, tk.END)
        entry_output_file.insert(0, filename)

def sort_and_write_callback():
    """Callback function for Sort & Write button."""
    input_file = entry_input_file.get()
    output_file = entry_output_file.get()
    if input_file and output_file:
        sort_and_write_names(input_file, output_file)
    else:
        messagebox.showerror("Error", "Please select both input and output files.")

# Create main window
root = tk.Tk()
root.title("Name Sorter")

# Input file frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

# Input file label and entry
tk.Label(input_frame, text="Input File:").grid(row=0, column=0, padx=5, pady=5)
entry_input_file = tk.Entry(input_frame, width=50)
entry_input_file.grid(row=0, column=1, padx=5, pady=5)

# Browse input file button
browse_input_button = tk.Button(input_frame, text="Browse", command=browse_input_file)
browse_input_button.grid(row=0, column=2, padx=5, pady=5)

# Output file label and entry
tk.Label(input_frame, text="Output File:").grid(row=1, column=0, padx=5, pady=5)
entry_output_file = tk.Entry(input_frame, width=50)
entry_output_file.grid(row=1, column=1, padx=5, pady=5)

# Browse output file button
browse_output_button = tk.Button(input_frame, text="Browse", command=browse_output_file)
browse_output_button.grid(row=1, column=2, padx=5, pady=5)

# Sort & Write button
sort_write_button = tk.Button(root, text="Sort & Write", command=sort_and_write_callback)
sort_write_button.pack(pady=10)

# Run the main loop
root.mainloop()
