#This is my blackjack python program
import random
suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

class Hand:
    def __init__(self):
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]

player_1 = Hand()
dealer = Hand()
print(player_1.player_cards)
print(dealer.player_cards)