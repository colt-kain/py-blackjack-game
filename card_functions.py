import random
import time
from card import *

def create_card_set(symbol):
    return [f'{value}{symbol}' for value in Card.values]

def shuffle_deck():
    shuffled_deck = random.sample(
        create_card_set(Card.suits['CLUBS']) +
        create_card_set(Card.suits['DIAMONDS']) +
        create_card_set(Card.suits['HEARTS']) +
        create_card_set(Card.suits['SPADES']),
        k=52 # The number of cards in a normal card deck
    )

    return shuffled_deck

def check_deck_length(deck):
    if len(deck) <= 2:
        print('Please wait. Shuffling deck...')
        time.sleep(3)
        print()

        new_deck = shuffle_deck()
        return new_deck
    else:
        return deck

def initialize_hand(deck):
    first_card = random.choice(deck)
    second_card = random.choice(deck)

    deck.remove(first_card)
    deck.remove(second_card)

    return [first_card, second_card]

def display_hand(person, hand, hand_value):
    print(f'{person}\'s hand: ', end='')
    for card in hand:
        print(card, end=' ')
    print()

    print(f'(HAND VALUE: {hand_value})\n')

def append_card(deck, hand):
    new_card = random.choice(deck)
    deck.remove(new_card)
    hand.append(new_card)

def get_hand_value(hand):
    hand_value = 0

    for card in hand:
        if card[0] in ['J', 'Q', 'K', 'A']:
            hand_value += 10
        else:
            hand_value += int(''.join(value for value in card if value.isdigit()))

    return hand_value
