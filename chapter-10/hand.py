'''
hand.py
A program to create a blackjack hand of playing cards
Nate Weeks, april 2018
'''
from deck import *

class Hand(object):
    '''Object that returns a hand given an input of two cards
    '''
    def __init__(self, card1, card2):
        self.hand = [card1, card2]

    def getHand(self):
        '''returns self.hand'''
        return self.hand

    def addCard(self, card):
        '''adds a card to the hand'''
        self.hand.append(card)

    def score(self):
        ''' tallies the blackjack score of a given hand'''
        score = 0
        for card in self.hand:
            if card.getRank() != 1:
                score += card.BJValue()
            else:
                if score <= 10:
                    score += 11
                else:
                    score += 1
        return score

    def getString(self):
        '''returns the string value of a given initial hand'''
        return "{}, and {}".format(self.getHand()[0], self.getHand()[1])
