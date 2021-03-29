from random import shuffle

class Deck:

    def __init__(self, card_deck):
        self.cards = card_deck

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, card_count):
        actual_count = self.count()
        remaining_cards = min(actual_count, card_count)
        if actual_count == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-remaining_cards:]
        self.cards = self.cards[:-remaining_cards]
        return hand

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, card_count):
        return self._deal(card_count)
