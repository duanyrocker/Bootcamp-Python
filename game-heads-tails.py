# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

print("Welcome to game heads or tails!")
choice = input("Welcome to virtual coin toss program, choice 'Heads' or 'Tails?'")
choice_capitalize = choice.capitalize()
random_integer = random.randint(0, 1)
if random_integer == 0 and choice_capitalize == "Heads":
    print(f"Heads! You win")
elif random_integer == 1 and choice_capitalize == "Tails":
    print(f"Tails! You win")
else:
    print(f"You lose")
