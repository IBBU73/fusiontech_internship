import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def perform_addition():
    try:
        result = float(num1_entry.get()) + float(num2_entry.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Function to perform subtraction
def perform_subtraction():
    try:
        result = float(num1_entry.get()) - float(num2_entry.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Function to perform multiplication
def perform_multiplication():
    try:
        result = float(num1_entry.get()) * float(num2_entry.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Function to perform division
def perform_division():
    try:
        divisor = float(num2_entry.get())
        if divisor == 0:
            raise ZeroDivisionError
        result = float(num1_entry.get()) / divisor
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Division by zero", "Cannot divide by zero")

# Main window setup
app = tk.Tk()
app.title("Basic Calculator")

# Variables for user inputs and results
num1_var = tk.StringVar()
num2_var = tk.StringVar()
result_var = tk.StringVar()

# Widgets for user interface
tk.Label(app, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
num1_entry = tk.Entry(app, textvariable=num1_var)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
num2_entry = tk.Entry(app, textvariable=num2_var)
num2_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(app, text="Add", command=perform_addition).grid(row=2, column=0, padx=10, pady=10)
tk.Button(app, text="Subtract", command=perform_subtraction).grid(row=2, column=1, padx=10, pady=10)
tk.Button(app, text="Multiply", command=perform_multiplication).grid(row=3, column=0, padx=10, pady=10)
tk.Button(app, text="Divide", command=perform_division).grid(row=3, column=1, padx=10, pady=10)

tk.Label(app, text="Result:").grid(row=4, column=0, padx=10, pady=10)
result_entry = tk.Entry(app, textvariable=result_var, state='readonly')
result_entry.grid(row=4, column=1, padx=10, pady=10)

# Start the main event loop
app.mainloop()
