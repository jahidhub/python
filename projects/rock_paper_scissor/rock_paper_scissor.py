
import random
choices = ['r', 'p', 's']
emoji = {'r': '✊', 'p': '✋', 's': '✌️'}


def get_user_chpice():
    while True:
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        
        if user_choice in choices:
           return user_choice
        else:
            print('invalid choice')




def display_choices(user_choice,computer_choice):
    print(f'your choice{emoji[user_choice]}')
    print(f'Computer choice{emoji[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    
    elif ((user_choice=='r' and computer_choice == 's') or
            (user_choice=='s' and computer_choice == 'p') or
            (user_choice=='p' and computer_choice == 'r')):
        print('You Win')

    else:
        print('You Loss')


def play_game():
    while True:
        user_choice = get_user_chpice()
        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice, computer_choice)
        should_continue = input('Are you continue this game ? (y/n)').lower()
        if should_continue == 'n':
            break


play_game()










