import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.guesses_taken = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_text = tk.Text(master, height=10, width=30)
        self.result_text.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.guesses_taken += 1

        if guess < self.secret_number:
            self.result_text.insert(tk.END, "Too low! Try again.\n")
        elif guess > self.secret_number:
            self.result_text.insert(tk.END, "Too high! Try again.\n")
        else:
            self.result_text.insert(tk.END, f"Congratulations! You guessed it in {self.guesses_taken} tries.\n")
            self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guesses_taken = 0
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
