from dataclasses import dataclass
import random

@dataclass
class Card:
    suit: str
    value: int


@dataclass
class Deck:
    cards: [Card]
    number_of_cards: int


def create_deck():
    cards = [Card] * 52

    for i in range(1, 53):
        if i < 14:
            cards[i-1] = Card('hearts', i)
        elif 14 <= i < 27:
            cards[i-1] = Card('Spades', i-13)
        elif 27 <= i < 40:
            cards[i-1] = Card('Diamonds', i-26)
        else:
            cards[i-1] = Card('Clubs', i-39)
    deck = Deck(cards, 52)
    return deck


def shuffle_deck(deck):
    cards = deck.cards
    shuffled_deck = [Card] * 51
    temp = {set}
    new_card = True
    for i in range(0, 51):
        while new_card:
            rand = random.randint(0, 51)
            if rand not in temp:
                temp.add(rand)
                shuffled_deck[i] = cards[rand]
                new_card = False
        new_card = True
    deck.cards = shuffled_deck


deck = create_deck()
shuffle_deck(deck)