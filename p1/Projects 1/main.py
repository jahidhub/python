# SNAKE, WATER, GUN GAME
# Rules:
# Snake drinks water (snake wins)
# Water drowns gun (water wins)
# Gun shoots snake (gun wins)
# If both are same → Tie

import random
# Computer choice
computer = random.choice([-1, 0, 1])

# User input
youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Mapping
line = {"s": 1, "w": -1, "g": 0}
reverse_line = {1: "Snake", 0: "Gun", -1: "Water"}

# Validate input
if youStr not in line:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = line[youStr]

    print(f"\nYou chose: {reverse_line[you]}")
    print(f"Computer chose: {reverse_line[computer]}")

    # Decision logic
    if computer == you:
        print("It's a tie!")
    elif (
        (computer == -1 and you == 1)
        or (computer == 0 and you == -1)
        or (computer == 1 and you == 0)
    ):
        print("🎉 You win!")
    else:
        print("😢 You lose!")
