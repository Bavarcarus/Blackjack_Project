#This is my blackjack python program
import random
suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

class Hand:

    def __init__(self):
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]
        self.score = 0
        self.scoring()

    def __repr__(self):
        blackjack_title = '''
  ____  _        _    ____ _  __   _   _    ____ _  __
 | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /
 |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / 
 | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ 
 |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\                                                      
        '''
        return blackjack_title

    def hit_me(self):
        pass
    
    def scoring(self):
        for card in self.player_cards:
            self.score += card_value[card[0]]
        for ace in self.player_cards:
            if 'Ace' in ace and self.score <= 11:
                self.score += 10
        
player_1 = Hand()
dealer = Hand()
print(repr(player_1))
print(player_1.player_cards, player_1.score)
print(dealer.player_cards, dealer.score)
