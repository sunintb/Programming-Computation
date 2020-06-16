# Sunint Bindra
# sa7cs1
# deck.py
# February 8, 2019
# This program makes a deck class and uses the card class to make a standard deck of cards, shuffle the deck to a random
# order, and to create a separate hand of cards and print those, as well as the remaining original deck



# Imports the randint function and card class
from random import randint
from card import *


# Creates a class named Deck
class Deck:


    def __init__(self):
        self.card_list = []


    # Appendixes all 52 cards by doing all suits of a card in 1 number, then cylcling through all numbers
    def add_standard_cards(self):
        index = 1
        while index <= 13:
            self.card_list.append(Card(index, 1))
            self.card_list.append(Card(index, 2))
            self.card_list.append(Card(index, 3))
            self.card_list.append(Card(index, 4))
            index = index + 1


    # Prints out card name
    def print(self):
        print(str(self.card_list))


    # Shuffles the deck by putting cards in the list into random positions
    def shuffle(self):
        for i in range(0, (len(self.card_list) - 1)):
            r = randint(0, (len(self.card_list) - 1))
            (self.card_list[i], self.card_list[r]) = (self.card_list[r], self.card_list[i])


    # Creates a new list of 5 cards and
    def deal(self, c):
        hand = Deck()
        for i in range(0, c):
            hand.card_list.append(self.card_list.pop())
        return hand






