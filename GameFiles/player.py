class Player:
    # minimum bet is $10

    def __init__(self, name="Dealer", score=0, bet=10, money=100, stick="no",
                 result=''):
        self.name = name
        self.money = money
        self.hand = []
        self.score = score
        self.stick = stick
        self.bet = bet
        self.result = result

    def set_name(self):
        self.name = input("Enter your name: ")

    def set_money(self, winnings):
        if self.name == "Dealer":
            self.money = 1000
        else:
            self.money += winnings

    def set_bet(self, bet):
        self.bet = bet

    def set_result(self, result):
        self.result = result

    @property
    def get_result(self):
        return self.result

    @property
    def get_bet(self):
        return self.bet

    @property
    def get_money(self):
        return self.money

    def get_name(self):
        return self.name

    def make_hand(self):
        self.hand = []

    def update_hand(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def set_stick(self, stick):
        self.stick = stick

    @property
    def get_stick(self):
        return self.stick

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score