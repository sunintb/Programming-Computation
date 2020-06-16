# Sunint Bindra
# sa7cs1
# card.py
# February 8, 2019
# This program makes a card class and uses that assigns card based ranks (king, queen, etc.) and suits (Hearts, Spades)
# based on a numerical input and returns the card name


# Creates a class called Card
class Card:


    # Assigns the #'s to specific card related names, which remain constant since the convention always stays the same
    SUITS = ('N/A', 'Clubs', 'Spades', 'Diamonds', 'Hearts')
    RANKS = ('N/A', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')


    # Defines self variables of card suit and rank
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank


    # Returns the card name
    def __str__(self):
         self.card = str(Card.RANKS[self.rank]) + " of " + str(Card.SUITS[self.suit])
         return self.card
