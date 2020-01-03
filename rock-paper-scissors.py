# //TODO: on linux, esc returns ^[ and then requires pressing enter after

import os
from random import randrange
import sys
from time import sleep
if os.name == 'nt':
    import msvcrt


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def wrong_input():
    print('\nInvalid input...')
    sleep(3)
    clear_screen()


def play():
    options = ('rock', 'paper', 'scissor')
    while True:
        try:
            player_choice = int(input(
                'CHOOSE A WEAPON WITH WHICH TO DO BATTLE!\n'
                '(1. rock, 2. paper, 3. scissor)\n'))
        except ValueError:
            wrong_input()
            continue
        if player_choice == 0:
            wrong_input()
            continue
        else:
            try:
                player_choice = options[player_choice - 1]
            except IndexError:
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
        print('Would you like to play again?\n\n'
              'Press enter for yes, escape for no')
        if os.name == 'nt':
            option = ord(msvcrt.getch())
            if option == 13:
                clear_screen()
                break
            elif option == 27:
                exit()
            else:
                wrong_input()
                continue
        else:
            option = ord(sys.stdin.read(1))
            if option == 10:
                clear_screen()
                break
            elif option == 27:
                exit()
            else:
                wrong_input()
                continue


while True:
    clear_screen()
    print('WELCOME! WELCOME! WELCOME!\n\nto\n\nROCK PAPER SCISSORS!\n\n'
          'Press enter to play or escape to close the game')
    if os.name == 'nt':
        option = ord(msvcrt.getch())
        if option == 13:
            clear_screen()
            play()
        elif option == 27:
            exit()
        else:
            wrong_input()
    else:
        option = ord(sys.stdin.read(1))
        if option == 10:
            clear_screen()
            play()
        elif option == 27:
            exit()
        else:
            wrong_input()
