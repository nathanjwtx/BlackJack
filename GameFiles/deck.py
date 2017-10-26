import random as r

class Deck:
    # deck = set()

    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                      '10', 'J', 'Q', 'K']
        self.suits = ['c', 'd', 'h', 's']
        self.new_deck = []

    def make_deck(self):
        for card in range(0, len(self.cards)):
            for suit in range(0, len(self.suits)):
                self.new_deck.append(self.cards[card] + self.suits[suit])
        # self.deck = set(self.new_deck)
        r.shuffle(self.new_deck)
        return self.new_deck

    def deal_card(self):
        if len(self.new_deck) == 0:
            self.make_deck()
        else:
            card = self.new_deck.pop()
            return card