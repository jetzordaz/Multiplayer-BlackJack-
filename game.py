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

    def play_multiple(self, policies):
        # Create fresh hands every round
        players = [Hand() for _ in policies]
        dealer = Hand()                     # ← Fresh dealer every round

        # Initial deal - 2 cards each
        for player in players:
            player.add_card(self.deck.draw())
            player.add_card(self.deck.draw())

        dealer.add_card(self.deck.draw())
        dealer.add_card(self.deck.draw())

        dealer_upcard = dealer.hand[0]      # Value or rank? Make sure this is correct (usually the rank/value)

        # Each player plays their strategy
        for i, player in enumerate(players):
            policy = policies[i]

            while True:
                try:
                    action = policy(player, dealer_upcard)
                except TypeError:
                    action = policy(player)

                if not action:          # False = stand
                    break

                player.add_card(self.deck.draw())

                if player.is_bust():
                    break

        # Dealer plays (standard rule: hit until 17 or more)
        while dealer.get_value() < 17 or (dealer.get_value() == 17 and dealer.is_soft()):  
            # Better: usually hit soft 17. Change to <=17 if your rules say so.
            dealer.add_card(self.deck.draw())

        # Determine results
        dealer_val = dealer.get_value()
        results = []

        for player in players:
            player_val = player.get_value()

            if player_val > 21:
                results.append(-1)   # loss
            elif dealer_val > 21:
                results.append(1)    # win
            elif player_val > dealer_val:
                results.append(1)
            elif player_val < dealer_val:
                results.append(-1)
            else:
                results.append(0)    # tie / push
            

        return results 



    

