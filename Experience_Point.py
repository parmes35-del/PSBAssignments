import tkinter as tk
import random

# Player class to handle player attributes, actions, and experience points
class Player:
    def __init__(self, name, hp, atk, def_):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_ = def_
        self.experience = 0  # Initialize experience points

    def attack(self, opponent):
        # Calculate effective damage using the provided formula
        damage = (self.atk - opponent.def_) + random.randint(0, 5)
        damage = max(damage, 0)  # Prevent negative damage
        opponent.hp -= damage
        if damage > 0:
            self.gain_experience(10)  # Gain 10 XP for a successful hit
        return damage

    def gain_experience(self, points):
        self.experience += points

    def is_alive(self):
        return self.hp > 0

    def get_experience(self):
        return self.experience

# Game class to control the game flow
class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Turn-Based Battle Game")

        # Players initialization
        self.player1 = Player("Player 1", 100, 20, 5)  # ATK: 20, DEF: 5
        self.player2 = Player("Player 2", 100, 15, 10)  # ATK: 15, DEF: 10

        self.current_attacker = self.player1

        # GUI elements
        self.info_label = tk.Label(master, text=self.status_message())
        self.info_label.pack(pady=20)

        self.attack_button = tk.Button(master, text="Attack", command=self.attack)
        self.attack_button.pack(pady=10)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)

    def status_message(self):
        return (f"{self.player1.name} HP: {self.player1.hp} | XP: {self.player1.get_experience()} | "
                f"{self.player2.name} HP: {self.player2.hp} | XP: {self.player2.get_experience()}")

    def attack(self):
        if self.current_attacker.is_alive():
            # Determine opponent and perform the attack
            opponent = self.player2 if self.current_attacker == self.player1 else self.player1
            damage = self.current_attacker.attack(opponent)
            opponent_name = opponent.name

            self.info_label.config(text=f"{self.current_attacker.name} attacks {opponent_name} for {damage} damage!")

            # Check for winner
            if not self.player1.is_alive() or not self.player2.is_alive():
                winner = self.player1 if self.player1.is_alive() else self.player2
                self.info_label.config(text=f"{winner.name} wins! {winner.name} gains {winner.get_experience()} XP!")
                self.attack_button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.NORMAL)
            else:
                # Switch turn to the other player
                self.current_attacker = self.player2 if self.current_attacker == self.player1 else self.player1
                self.info_label.config(text=self.status_message())

    def restart(self):
        self.player1.hp = 100
        self.player2.hp = 100
        self.player1.experience = 0
        self.player2.experience = 0
        self.current_attacker = self.player1
        self.info_label.config(text=self.status_message())
        self.attack_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)

# Create the main window and initialize the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
