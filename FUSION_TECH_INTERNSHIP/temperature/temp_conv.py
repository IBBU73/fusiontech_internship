import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    """Converts temperature based on user input."""
    conversion_type = conversion_var.get()
    temperature = float(entry_temperature.get())

    if conversion_type == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temperature)
        result_label.config(text=f"{temperature}°C = {result}°F")
    elif conversion_type == "Fahrenheit to Celsius":
        result = fahrenheit_to_celsius(temperature)
        result_label.config(text=f"{temperature}°F = {result}°C")
    elif conversion_type == "Celsius to Kelvin":
        result = celsius_to_kelvin(temperature)
        result_label.config(text=f"{temperature}°C = {result} K")
    elif conversion_type == "Kelvin to Celsius":
        result = kelvin_to_celsius(temperature)
        result_label.config(text=f"{temperature} K = {result}°C")
    elif conversion_type == "Fahrenheit to Kelvin":
        result = fahrenheit_to_kelvin(temperature)
        result_label.config(text=f"{temperature}°F = {result} K")
    elif conversion_type == "Kelvin to Fahrenheit":
        result = kelvin_to_fahrenheit(temperature)
        result_label.config(text=f"{temperature} K = {result}°F")
    else:
        messagebox.showerror("Error", "Invalid conversion type selected.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Temperature input frame
input_frame = tk.Frame(root, padx=20, pady=20)
input_frame.pack()

# Temperature entry and label
tk.Label(input_frame, text="Enter Temperature:").grid(row=0, column=0)
entry_temperature = tk.Entry(input_frame, width=10)
entry_temperature.grid(row=0, column=1)

# Conversion type dropdown
conversion_var = tk.StringVar()
conversion_options = [
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Fahrenheit"
]
conversion_var.set(conversion_options[0])  # Default selection
conversion_menu = tk.OptionMenu(input_frame, conversion_var, *conversion_options)
conversion_menu.grid(row=1, column=0, columnspan=2, pady=10)

# Convert button
convert_button = tk.Button(input_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", padx=20, pady=20)
result_label.pack()

# Run the main loop
root.mainloop()
