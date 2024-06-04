import os
from time import sleep

def clear_screen(message = None):
    print(message)
    sleep(2)
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')