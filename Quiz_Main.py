import json
import random
import tkinter as tk
from tkinter import messagebox


class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")

        # Load questions from kb.json
        with open('kb.json', 'r') as file:
            all_questions = json.load(file)

        # Select 5 random questions
        self.questions = random.sample(all_questions, 5)

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(master, text=self.questions[self.current_question]["question"])
        self.question_label.pack(pady=10)

        self.var = tk.StringVar(value="")
        self.options_frame = tk.Frame(master)
        self.options_frame.pack()

        self.create_radio_buttons()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def create_radio_buttons(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for option in self.questions[self.current_question]["options"]:
            rb = tk.Radiobutton(self.options_frame, text=option, variable=self.var, value=option)
            rb.pack(anchor=tk.W)

    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            self.create_radio_buttons()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score}/{len(self.questions)}")
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()