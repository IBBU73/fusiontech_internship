import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        """ generate random number from 1 - 100 """
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess the number (between 1 and 100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=10)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        self.entry.delete(0, tk.END)  # Clear the entry box after each guess
        try:
            guess = int(guess)
            self.attempts += 1
            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        messagebox.showinfo("New Game", "Starting a new game with a new number.")


# Create main window_box

root = tk.Tk()
game = NumberGuessingGame(root)

# Run the main loop
root.mainloop()
