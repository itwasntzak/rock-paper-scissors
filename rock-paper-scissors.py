# //TODO: ask reddit how to make this work on linux. msvcrt is only windows

import os
from random import randrange
import msvcrt
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')


def play():
    options = ('rock', 'paper', 'scissor')
    while True:
        random_number = randrange(3)
        player_option = int(input('CHOOSE A WEAPON WITH WHICH TO DO BATTLE!\n'
                                  '(1. rock, 2. paper, 3. scissor)\n'))

        if player_option == 1:
            print('\nROCK')
        elif player_option == 2:
            print('\nPAPER')
        elif player_option == 3:
            print('\nSCISSOR')
        else:
            print('\nInvalid input...\n')
        print('\n.VS\n\n' + options[random_number].upper())
        sleep(3)
        results(player_option, random_number)
        sleep(3)
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
    print('Would you like to play again?\nPress enter for yes, escape for no)')
    option = ord(msvcrt.getch())
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == 13:
        pass
    elif option == 27:
        exit()
    else:
        print('Invalid input...')


while True:
    print('WELCOME! WELCOME! WELCOME!\n\nto\n\nROCK PAPER SCISSORS!\n\n'
          'Press enter to play or escape to close the game')
    option = ord(msvcrt.getch())
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == 13:
        play()
    elif option == 27:
        exit()
    else:
        print('Invalid input...')
