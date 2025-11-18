import tkinter as tk
import random


# Player class to manage player attributes, actions, and experience points
class Player:
    def __init__(self, name, hp, atk, def_):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_ = def_
        self.experience = 0  # Experience points
        self.level = 1  # Level initial value

    def attack(self, opponent):
        # Calculate effective damage
        damage = (self.atk - opponent.def_) + random.randint(5, 10)
        damage = max(damage, 0)  # Prevent negative damage

        opponent.hp -= damage
        self.gain_experience(damage, opponent.def_)

        return damage

    def gain_experience(self, damage, opponent_def):
        if damage == opponent_def:
            self.experience += 10  # Equal to DEF
        elif damage > opponent_def:
            self.experience += 20  # Greater than DEF

        # Level up if EXP reaches 100
        while self.experience >= self.level_up_threshold():
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 10  # Increase HP on level up
        self.atk += 2  # Increase ATK on level up
        self.def_ += 1  # Increase DEF on level up

    def level_up_threshold(self):
        return 100  # Level up at 100 EXP

    def is_alive(self):
        return self.hp > 0

    def get_experience(self):
        return self.experience

    def get_level(self):
        return self.level


# Game class to control the game flow
class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Turn-Based Battle Game")

        # Players initialization
        self.player1 = Player("Player 1", 100, 20, 5)  # HP, ATK, DEF
        self.player2 = Player("Player 2", 100, 15, 10)

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
        return (f"{self.player1.name} HP: {self.player1.hp} | Level: {self.player1.get_level()} | "
                f"XP: {self.player1.get_experience()} | "
                f"{self.player2.name} HP: {self.player2.hp} | Level: {self.player2.get_level()} | "
                f"XP: {self.player2.get_experience()}")

    def attack(self):
        if self.current_attacker.is_alive():
            # Determine opponent and perform the attack
            opponent = self.player2 if self.current_attacker == self.player1 else self.player1
            damage = self.current_attacker.attack(opponent)
            opponent_name = opponent.name

            self.info_label.config(text=f"{self.current_attacker.name} attacks {opponent_name} for {damage} damage!")

            # Check for removal from team
            if opponent.hp <= 0:
                opponent.hp = 0  # Ensure HP does not go negative
                self.info_label.config(text=f"{opponent_name} has been defeated!")

            # Check for winner
            if not self.player1.is_alive() or not self.player2.is_alive():
                winner = self.player1 if self.player1.is_alive() else self.player2
                self.info_label.config(
                    text=f"{winner.name} wins! {winner.name} is Level {winner.get_level()} with {winner.get_experience()} XP!")
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
        self.player1.level = 1
        self.player2.level = 1
        self.current_attacker = self.player1
        self.info_label.config(text=self.status_message())
        self.attack_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)


# Create the main window and initialize the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
