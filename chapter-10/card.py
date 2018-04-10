'''
card.py
by Nate Weeks, April 2018
'''
import random

class Card(object):
    '''card object that does some stuff given input of rank 1-13
    and suit h, s, c, or d'''
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        '''returns the blackjack value of a card'''
        BJValue = 0
        if self.rank <= 10:
            BJValue = self.rank
        elif self.rank <= 13:
            BJValue = 10
        else:
            print "please initiate with an integer 1-13"
        return BJValue

    def __str__(self):
        '''returns string value of the card'''
        name = ""
        suit = ""
        if self.rank == 1:
            name = "Ace"
        elif self.rank <= 10:
            name = str(self.rank)
        elif self.rank == 11:
            name = "Jack"
        elif self.rank == 12:
            name = "Queen"
        elif self.rank == 13:
            name = "King"
        if self.suit == "s":
            suit = "Spades"
        elif self.suit == "d":
            suit = "Diamonds"
        elif self.suit == "h":
            suit = "Hearts"
        elif self.suit == "c":
            suit = "Clubs"
        else:
            "please intiate with a suite s, h, c, or d"
        return "%s of %s" % (name, suit)

def randomCard(n):
    '''generates n random cards'''
    cardArray = []
    for i in range(n):
        card = Card(random.randrange(1, 14), random.choice("sdhc"))
        cardArray.append(card)
    return cardArray

def main():
    '''generates a random number of cards based on user input
    and prints them with their associated blackjack value'''
    print "please enter a number of random cards you would like to generate"
    number = input()
    array = randomCard(number)
    print "you generated:"
    for card in array:
        score = card.BJValue()
        print "Card Name: %s, Blackjack Value: %s" % (card, score)

main()
