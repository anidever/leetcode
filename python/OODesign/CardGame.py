import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self, card_count):
        self.cards = []
        self.card_count = card_count
        self.populate()

    def shuffle(self):
        random.shuffle(self.cards)

    def populate(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in range(1, int(self.card_count/4))]

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None


class Player:
    def __init__(self, index):
        self.hand = []
        self.score = 0
        self.index = index

    def add_to_hand(self, card):
        self.hand.insert(0, card)

    def play(self):
        if self.hand:
            return self.hand.pop()
        else:
            return None

    def increase_score(self, points):
        self.score += points


class Game:
    def __init__(self, card_count=52, player_count=2):
        self.deck = Deck(card_count)
        self.player_count = player_count
        self.players = [Player(idx) for idx in range(player_count)]

    def deal_cards(self):
        self.deck.shuffle()
        while len(self.deck.cards) > self.player_count:
            for player in self.players:
                player.add_to_hand(self.deck.draw())

    def play_round(self):
        played_cards = {idx: player.play() for idx, player in enumerate(self.players)}
        winning_player, winning_card = max(played_cards.items(), key=lambda x: x[1].value)
        for idx, card in played_cards.items():
            self.players[winning_player].add_to_hand(card)
            self.players[winning_player].increase_score(1)

    def play_game(self):
        self.deal_cards()
        while all(len(player.hand) for player in self.players):
            self.play_round()


game = Game(player_count=4, card_count=104)
game.play_game()
