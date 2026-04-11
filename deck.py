# deck.py --> Supports Infinite Deck and Single Deck
import random

BASE_DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Deck:
    def __init__(self, deck_type='infinite'):
        """
        deck type:
            "infinite": Infinite Deck (cards are not removed after being drawn), same probability for each card
            "single": Single Deck (Standard 52-card deck), reshuffled after every game
        """
        self.deck_type = deck_type
        
        if self.deck_type == 'single':
            self.__init__single_deck()
    
    def __init__single_deck(self):
        """
        Initialize and shuffle a standard 52-card deck.
        Card values:
            Ace = 1
            2–9 = face value
            10, J, Q, K = 10
        """
        self.cards = BASE_DECK * 4  # 4 suits
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw a card from the deck.
        For infinite deck, return a random card value.
        For single deck, return the top card and remove it from the deck.
        """
        if self.deck_type == 'infinite':
            return random.choice(BASE_DECK)
        
        elif self.deck_type == 'single':
            if not self.cards:
                self.__init__single_deck()
            return self.cards.pop()
        
        else:
            raise ValueError("Invalid deck type. Use 'infinite' or 'single'.")
            
