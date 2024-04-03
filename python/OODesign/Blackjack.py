import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        self.populate()

    def populate(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []

    def hit(self):
        pass

    def stand(self):
        pass


class Dealer:
    def __init__(self):
        self.hand = []

    def hit(self):
        pass

    def stand(self):
        pass


class Game:
    def __init__(self):
        self.rolls = []
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()