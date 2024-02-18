from os import name, system

def clear_console():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')

def display_title():
    print('------------- BLACKJACK --------------')
    print('(Important NOTE: Ace = 10Val.)')
    print('(Betting amounts: 5, 10, 25, 50, 100.)') 
    print('--------------------------------------\n')
