from utility_functions import *
from player_functions import *
from card_functions import *

def play_round(player_balance):
    clear_console()
    display_title()
    print(f'[Current balance: ${player_balance}]\n') 

    player_bet = get_player_bet(player_balance)
    deck = check_deck_length(shuffle_deck())

    player_hand = initialize_hand(deck)
    player_value = 0
    dealer_hand = initialize_hand(deck)
    dealer_value = 0

    while player_value <= 21 and dealer_value <= 21:
        deck = check_deck_length(shuffle_deck())

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        display_hand('Player', player_hand, player_value)
        display_hand('Dealer', dealer_hand, dealer_value)

        player_choice = get_player_choice()

        if player_choice == 'hit':
            append_card(deck, player_hand)
            player_value = get_hand_value(player_hand)

            if player_value > 21:
                display_hand('Player', player_hand, player_value)
                display_round_outcome('lose', player_bet)

                wait_to_continue()
                return player_balance - player_bet

            if player_value == 21:
                display_hand('Player', player_hand, player_value)
                display_round_outcome('win', player_bet)

                wait_to_continue()
                return player_balance + player_bet
        else:
            while dealer_value <= 17:
                append_card(deck, dealer_hand)
                dealer_value = get_hand_value(dealer_hand)

            display_hand('Dealer', dealer_hand, dealer_value)

            if dealer_value > 21 or dealer_value < player_value:
                display_round_outcome('win', player_bet)

                wait_to_continue()
                return player_balance + player_bet
            elif dealer_value == 21 or dealer_value > player_value:
                display_round_outcome('lose', player_bet)
                
                wait_to_continue()
                return player_balance - player_bet
            else:
                display_round_outcome('tie', player_bet)

                wait_to_continue() 
                return player_balance

def get_play_again(player_balance):
    while True:
        play_again = input('Would you like to play again?: ') 

        if play_again.lower() in ['yes', 'yeah', 'sure', 'why not', 'of course']:
            if player_balance == 0:
                print('\n- Too bad. You\'re no use to me, Mr. $0. =] HA HA HA\n')

                wait_to_continue()
                return False

            print(f'Current BALANCE: ${player_balance}\n')
            print('- Wonderful. =]\n')

            wait_to_continue()
            return True
        elif play_again.lower() in ['no', 'nah', 'nope', 'heck no', 'hell nah']:
            print(f'You quit the game with ${player_balance}.\n')
            print('- How unfortunate. See you next time, pal. =)\n')

            wait_to_continue()
            return False
        else:
            print('Invalid response.\n')
