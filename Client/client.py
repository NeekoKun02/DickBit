import sys, os
from dotenv import load_dotenv
from send import Send
from list import List
from login import *
from help import *
from lost import Lost

global IP, PORT, ID_LENGTH
load_dotenv()

IP = os.getenv('IP')
PORT = os.getenv('PORT')
ID_LENGTH = os.getenv('ID_LENGTH')

def logo():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(' ____________________________________________________')
    print('|///////////____  _      _    ____  _ _ \\\\\\\\\\\\\\\\\\\\\\\\\\|')
    print('|//////////|  _ \(_) ___| | _| __ )(_) |_\\\\\\\\\\\\\\\\\\\\\\\\|')
    print('|///////// | | | | |/ __| |/ /  _ \| | __|\\\\\\\\\\\\\\\\\\\\\\|')
    print('|////////  | |_| | | (__|   <| |_) | | |_  \\\\\\\\\\\\\\\\\\\\|')
    print('|///////   |____/|_|\___|_|\_\____/|_|\__|  \\\\\\\\\\\\\\\\\\|')
    print(' ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞\n\n\n')

def welcome():
    print('What do you wanna do?\n')
    print('1) Login on DickBit')
    print('2) Index')
    print('3) Message a specific contact')
    print('4) View lost messages')
    print('5) Help')
    print('0) Exit\n')

###################################################################################################################################
###################################################################################################################################

def exit():
    print('Goodbye user')
    sys.exit()

def options(c):
    if c == '1':
        login()
    elif c == '2':
        List().contacts()
    elif c == '3':
        Send(IP, PORT, ID_LENGTH).pre_send(None)
    elif c == '4':
        Lost.lost()
    elif c == '5':
        help()
    elif c == '0':
        exit()
    else:
        print('Enter a number from 0 to 5')

def send():
    print('sended')

#########################################################################################################################
#########################################################################################################################

logo()
while True:
    welcome()
    options(input(']> '))