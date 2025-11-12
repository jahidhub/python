from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 99.")
print("Try to guess it!\n")

actual = randint(1, 99)
player = -1
guess = 0

while player != actual:
    try:
        player = int(input("Enter your guess number: "))
        guess += 1

        if player > actual:
            print("📉 Lower number please!\n")
        elif player < actual:
            print("📈 Higher number please!\n")
        else:
            print(f"🎉 Congratulations! You guessed the number {actual} correctly!")
            print(f"✅ You took {guess} guesses to get it right.\n")
    except ValueError:
        print("❌ Please enter a valid number!\n")
