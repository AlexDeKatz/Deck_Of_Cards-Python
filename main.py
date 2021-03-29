from random import choice
from card import Card
from deck import Deck

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = [Card(suit,value) for suit in suits for value in values]

new_deck = Deck(deck)
new_deck.shuffle()
card = new_deck.deal_card()
print(card)
hand = new_deck.deal_hand(5)
print(hand)

print(new_deck.cards)


