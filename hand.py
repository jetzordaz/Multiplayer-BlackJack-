# hand.py --> Handles hand logic
class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        total = sum(self.hand)
        aces = self.hand.count(1)

        while aces > 0 and total + 10 <= 21:
            total += 10
            aces -= 1

        return total
    
    def is_soft(self):
        total = sum(self.hand)
        return 1 in self.hand and total + 10 <= 21
    
    def is_blackjack(self):
        return len(self.hand) == 2 and self.get_value() == 21