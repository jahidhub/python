
import random
number_to_guess = random.randint(1 ,100)

while True:
    try:
        guess = int(input('Guess the number between 1 to 100: '))

        if  guess < number_to_guess:
            print("too low")
        elif guess > number_to_guess:
            print("too hight")
        else :
            print("congratulations")
            break

    except ValueError:
        print('Please Enter a  valid  number')


