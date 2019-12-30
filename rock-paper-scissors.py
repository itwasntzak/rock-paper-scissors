# //TODO: on linux, esc returns ^[ and then requires pressing enter after

import os
from random import randrange
import sys
from time import sleep
if os.name == 'nt':
    import msvcrt

os.system('cls' if os.name == 'nt' else 'clear')


def play():
    options = ('rock', 'paper', 'scissor')
    while True:
        player_option = int(input('CHOOSE A WEAPON WITH WHICH TO DO BATTLE!\n'
                                  '(1. rock, 2. paper, 3. scissor)\n'))
        random_number = randrange(3)

        if player_option == 1:
            print('\nROCK')
        elif player_option == 2:
            print('\nPAPER')
        elif player_option == 3:
            print('\nSCISSOR')
        else:
            print('\nInvalid input...\n')
        sleep(1)
        print('\n.VS\n')
        sleep(2)
        print(options[random_number].upper())
        sleep(2)
        results(player_option, random_number)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        try_again()


def results(player_option, random_number):
    if (player_option == 1 and random_number == 2)\
            or (player_option == 2 and random_number == 0)\
            or (player_option == 3 and random_number == 1):
        print('\nWINNIN\'! WINNIN\'! CHICKEN DICKIN\'!!!')

    elif (player_option == 1 and random_number == 1)\
            or (player_option == 2 and random_number == 2)\
            or (player_option == 3 and random_number == 0):
        print('\nLOSER! TRY AGAIN!')

    elif (player_option == 1 and random_number == 0)\
            or (player_option == 2 and random_number == 1)\
            or (player_option == 3 and random_number == 2):
        print('\nANTICLIMACTIC! IT\'S A DRAW! TRY AGAIN!')


def try_again():
    print('Would you like to play again?\nPress enter for yes, escape for no')
    if os.name == 'nt':
        option = ord(msvcrt.getch())
        os.system('cls')
        if option == 13:
            pass
        elif option == 27:
            exit()
        else:
            print('Invalid input...')
    else:
        option = ord(sys.stdin.read(1))
        os.system('clear')
        if option == 10:
            pass
        elif option == 27:
            exit()
        else:
            print('Invalid input...')


while True:
    print('WELCOME! WELCOME! WELCOME!\n\nto\n\nROCK PAPER SCISSORS!\n\n'
          'Press enter to play or escape to close the game')
    if os.name == 'nt':
        option = ord(msvcrt.getch())
        os.system('cls')
        if option == 13:
            play()
        elif option == 27:
            exit()
        else:
            print('Invalid input...')
    else:
        option = ord(sys.stdin.read(1))
        os.system('clear')
        if option == 10:
            play()
        elif option == 27:
            exit()
        else:
            print('Invalid input...')
