import os
from random import randrange
from time import sleep


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def wrong_input():
    print('\nInvalid input...')
    sleep(3)
    clear_screen()


def play():
    options = ('rock', 'paper', 'scissor')
    while True:
        player_choice = str(input(
            'CHOOSE A WEAPON WITH WHICH TO DO BATTLE!\n'
            'R = rock, P = paper, S = scissor\n\n'))
        if player_choice in ('r', 'R'):
            player_choice = options[0]
        elif player_choice in ('p', 'P'):
            player_choice = options[1]
        elif player_choice in ('s', 'S'):
            player_choice = options[2]
        else:
            wrong_input()
            continue
        computer_choice = options[randrange(len(options))]
        clear_screen()
        print('\n' + player_choice.upper())
        sleep(2)
        print('\n.vs'.upper())
        sleep(2)
        print('\n' + computer_choice.upper())
        sleep(2)
        results(player_choice, computer_choice)
        sleep(4)
        try_again()


def results(player_choice, computer_choice):
    if (player_choice, computer_choice) in\
            (('rock', 'scissor'), ('paper', 'rock'), ('scissor', 'paper')):
        print('\nWINNIN\'! WINNIN\'! CHICKEN DICKIN\'!!!')

    elif (player_choice, computer_choice) in\
            (('rock', 'paper'), ('paper', 'scissor'), ('scissor', 'rock')):
        print('\nLOSER! TRY AGAIN!')

    elif (player_choice, computer_choice) in\
            (('rock', 'rock'), ('paper', 'paper'), ('scissor', 'scissor')):
        print('\nANTICLIMACTIC! IT\'S A DRAW! TRY AGAIN!')


def try_again():
    clear_screen()
    while True:
        option = str(input(
            'Would you like to play again?\n\n'
            'Enter P = play again, X = exit\n\n'))
        if option in ('p', 'P'):
            clear_screen()
            break
        elif option in ('x', 'X'):
            exit()
        else:
            wrong_input()
            continue


while True:
    clear_screen()
    option = str(input(
        'WELCOME! WELCOME! WELCOME!\n\n'
        'to\n\n'
        'ROCK PAPER SCISSORS!\n\n'
        'Enter P = play or X = exit\n\n'))
    if option in ('p', 'P'):
        clear_screen()
        play()
    elif option in ('x', 'X'):
        exit()
    else:
        wrong_input()
