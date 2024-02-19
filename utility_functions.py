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

def wait_to_continue():
    user_confirmation = input('Please press ENTER to continue... ')

    while user_confirmation != '':
        print('Invalid response.\n')
        user_confirmation = input('Please press ENTER to continue... ')

def display_round_outcome(outcome, player_bet):
    round_sign = ''
    if outcome == 'win':
        round_sign = '+'
    elif outcome == 'lose':
        round_sign = '-'
    else:
        round_sign = '[X]'

    print('---------------')
    print(f'Round: {outcome}.\nBALANCE {round_sign}${player_bet}')
    print('---------------\n')
