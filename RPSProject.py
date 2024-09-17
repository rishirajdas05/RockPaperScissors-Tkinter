import random
import tkinter as tk
from PIL import Image, ImageTk

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("1000x1000")

        # Load the images
        try:
            self.rock_image = ImageTk.PhotoImage(Image.open(r"C:\Users\rishi\Downloads\Rock.jpeg"))
            self.paper_image = ImageTk.PhotoImage(Image.open(r"C:\Users\rishi\Downloads\Paper.jpeg"))
            self.scissor_image = ImageTk.PhotoImage(Image.open(r"C:\Users\rishi\Downloads\scissor.jpeg"))
        except Exception as e:
            print(f"Error loading images: {e}")

        # Create a label to display the computer's choice
        self.computer_label = tk.Label(self.window, text="", image="")
        self.computer_label.pack()

        # Create a label to display the result
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Create buttons for the user's choice
        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissor_button = tk.Button(self.window, text="Scissor", command=lambda: self.play("scissor"))
        self.scissor_button.pack()

    def play(self, user_choice):
        # Generate the computer's choice
        choices = ["rock", "paper", "scissor"]
        computer_choice = random.choice(choices)

        # Display the computer's choice
        if computer_choice == "rock":
            self.computer_label.config(image=self.rock_image)
        elif computer_choice == "paper":
            self.computer_label.config(image=self.paper_image)
        else:
            self.computer_label.config(image=self.scissor_image)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissor") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissor" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Display the result
        self.result_label.config(text=result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
    