#This is my blackjack python program
import random
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
blackjack_title = '''
  ____  _        _    ____ _  __   _   _    ____ _  __
 | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /
 |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / 
 | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ 
 |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\                                                      
'''
suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

class Hand:

    def __init__(self, name):
        self.name = name
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]
        self.scoring()       

    def __repr__(self):
        return f"{self.name}'s Blackjack game"

    def hit_me(self):
        self.hand_print()
        self.stand = False
        while self.score < 21 and self.stand == False:
            self.hit = input("Hit or Stand?").lower()
            if len(self.hit) > 0 and self.hit[0] == "h":
                self.player_cards.append([random.choice(cards), random.choice(suit)])
                self.scoring()
                self.hand_print()
            elif len(self.hit) > 0 and self.hit[0] == "s":
                self.stand = True
        self.stand = True
        
    def dealer_hand(self):
        while dealer.score <=17:
            dealer.player_cards.append([random.choice(cards), random.choice(suit)])
            dealer.scoring()
        

    def hand_print(self):
        self.printable_hand = f"{self.name}'s hand: \n"
        for show_cards in self.player_cards:
            self.printable_hand += f"{show_cards[0]} of {show_cards[1]}, "
        self.printable_hand = self.printable_hand[0:-2]
        clear()
        print(blackjack_title)
        if self.name != "Dealer":
            print(f"Dealer shows {dealer.player_cards[0][0]} of {dealer.player_cards[0][1]} \n")
        print(self.printable_hand + "\nScore: " + str(self.score))

    def scoring(self):
        self.score = 0
        for card in self.player_cards:
            self.score += card_value[card[0]]
        for ace in self.player_cards:
            if 'Ace' in ace and self.score <= 11:
                self.score += 10
        
clear()
print(blackjack_title)
player_1 = Hand(input("What should I call you?"))
dealer = Hand("Dealer")

player_1.hit_me()