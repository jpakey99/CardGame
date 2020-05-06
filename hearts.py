from dataclasses import dataclass


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


create_deck()