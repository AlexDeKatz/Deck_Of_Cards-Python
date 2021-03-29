class Card:

    _allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __init__(self, suit, value):
        if suit in Card._allowed_suit:
            self.suit = suit
            self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

