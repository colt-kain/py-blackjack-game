from utility_functions import *
from card_functions import *

def filter_player_bet(player_bet, player_balance):
    if player_bet in [5, 10, 25, 50, 100] and player_bet <= player_balance:
        print()
        return player_bet
    else:
        print('Invalid betting amount inputted.\n')
        return None

def get_player_bet(player_balance):
    player_bet = None

    while player_bet == None:
        try:
            player_bet = int(input('==> Place your bet: $'))
            player_bet = filter_player_bet(player_bet, player_balance)
        except ValueError:
            print('Invalid format inputted.\n')

    return player_bet

def get_player_choice():
    while True:
        player_choice = input('---> HIT or STAY: ')

        if player_choice.lower() in ['hit', 'stay']:
            print()
            return player_choice.lower()
        else:
            print('Invalid choice inputted.\n')
