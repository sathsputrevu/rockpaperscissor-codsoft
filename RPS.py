import tkinter as tk
import random
import time

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.cheat_code = "godmode"

        self.choices = ["rock", "paper", "scissors"]

        self.user_choice_label = tk.Label(master, text="Choose your weapon:", font=("Helvetica", 14, "bold"), fg="#008080")
        self.user_choice_label.pack()

        self.buttons_frame = tk.Frame(master, bg="#F0F8FF")
        self.buttons_frame.pack()

        self.buttons = []
        for choice in self.choices:
            button = tk.Button(self.buttons_frame, text=choice.capitalize(), command=lambda ch=choice: self.play_game(ch), width=10, height=2, font=("Helvetica", 12, "bold"), bg="#87CEEB", fg="#2F4F4F", activebackground="#4682B4")
            button.pack(side=tk.LEFT, padx=10)
            self.buttons.append(button)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 14), fg="#008080", pady=20)
        self.result_label.pack()

        self.score_label = tk.Label(master, text="Score: User - 0, Computer - 0", font=("Helvetica", 12, "italic"), fg="#008080")
        self.score_label.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, state=tk.DISABLED, font=("Helvetica", 12), pady=5, bg="#87CEEB", fg="#2F4F4F", activebackground="#4682B4")
        self.play_again_button.pack()

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x_coordinate = (screen_width - master.winfo_reqwidth()) // 2
        y_coordinate = (screen_height - master.winfo_reqheight()) // 2

        master.geometry(f"+{x_coordinate}+{y_coordinate}")

    def play_game(self, user_choice):
        if user_choice.lower() == self.cheat_code:
            self.result_label.config(text="Cheat activated! You win this round.")
            self.user_score += 1
            self.computer_score -= 1
        else:
            computer_choice = self.get_computer_choice()
            self.animate_computer_choice(computer_choice)

            result = self.determine_winner(user_choice, computer_choice)
            self.result_label.config(text=f"Computer's choice: {computer_choice.capitalize()}\n{result}")

            if result == "You win!":
                self.user_score += 1
            elif result == "You lose!":
                self.computer_score += 1

        self.update_score()
        self.play_again_button.config(state=tk.NORMAL)

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_score()
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

    def animate_computer_choice(self, choice):
        for _ in range(5):
            self.result_label.config(text=f"Computer's choice: {random.choice(self.choices).capitalize()}")
            self.master.update()
            time.sleep(0.1)

        self.result_label.config(text=f"Computer's choice: {choice.capitalize()}")

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
