from random import shuffle


class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # def get_card(self):
    #     return f"type: {self.type}, value: {self.value}"
    def __repr__(self):
        return f"{self.type} {self.value}"


class Deck:
    types = ["karo", "sinek", "kupa", "maça"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(type, value) for type in Deck.types for value in Deck.values]

    def count_card(self):
        return len(self.cards)

    def shuffle_cards(self):
        if self.count_card() < 52:
            raise ValueError("you only shuffle before cards deal")
        shuffle(self.cards)

    def deal_card(self, piece):
        count_card = self.count_card()
        if count_card == 0:
            raise ValueError("no card to deal")
        piece = min([count_card, piece])  # --------------> ı don't know what is it doing??
        cards = self.cards[-piece:]
        self.cards = self.cards[:-piece]
        return cards
    def throw_card(self):
        return self.deal_card(1)[0]

deck1 = Deck()
deck1.shuffle_cards()
print(deck1.deal_card(5))
print(deck1.throw_card())
print(deck1.count_card())
print(deck1.cards)