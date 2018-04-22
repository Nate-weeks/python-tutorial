'''
deck.py
A program to initiate a deck of playing cards
Nate Weeks, april 2018
'''

from card import *
from random import shuffle

SUITS = ["s", "d", "h", "c"]

VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Deck(object):
    '''generates a unique deck of 52 playing cards'''
    def __init__(self):
        collection = []
        for suit in SUITS:
            for rank in VALUES:
                collection.append(Card(rank, suit))
        shuffle(collection)
        self.deck = collection

    def getDeck(self):
        '''returns self.deck'''
        return self.deck

    def deal(self):
        '''returns a card for the top of the deck'''
        return self.deck.pop()

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
