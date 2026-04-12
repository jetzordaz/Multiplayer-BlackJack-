# game.py --> Blackjack game logic
from hand import Hand

class BlackjackGame:
    def __init__(self, deck):
        self.deck = deck

    def play(self, policy):
        player = Hand()
        dealer = Hand()

        #Initial deal
        player.add_card(self.deck.draw())
        dealer.add_card(self.deck.draw()) 
        player.add_card(self.deck.draw())
        dealer.add_card(self.deck.draw())

        dealer_upcard = dealer.hand[0]

        while True:
            try:
                action = policy(player, dealer_upcard)
            except TypeError:
                action = policy(player)

            if not action:
                break

            player.add_card(self.deck.draw())

            if player.is_bust():
                return -1
            
        while dealer.get_value() < 17:
            dealer.add_card(self.deck.draw())

            if dealer.is_bust():
                return 1
        
        player_value = player.get_value()
        dealer_value = dealer.get_value()

        if player_value > dealer_value:
            return 1  # Player wins
        elif player_value < dealer_value:
            return -1  # Dealer wins
        else:
            return 0  # Tie

    

