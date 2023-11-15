import tkinter as tk


root = tk.Tk()
root.title("My Adventure Game")

# Create a label to display the game world
world_label = tk.Label(root, text="You are in a dark room. What do you do?")
world_label.pack()

# Create a button to move the player
move_button = tk.Button(root, text="Move forward")
move_button.pack()

def attack(enemy_name):
    print("You attack the", enemy_name, "with your sword!")
enemy_name = "dragon"
attack(enemy_name)
import random

def attack(enemy_name):
    success_chance = random.randint(1, 10)  # Generate a random number between 1 and 10
    if success_chance > 5:
        print("You attack the", enemy_name, "with your sword and defeat it!")
    else:
        print("Your attack misses and the", enemy_name, "strikes back!")

root.mainloop()

