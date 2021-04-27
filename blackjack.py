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
        self.wins = 0
        self.losses = 0
        self.play_again = True

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
            elif len(self.hit) > 0 and self.hit[0] == "s":
                self.stand = True
            self.hand_print()
        
    def dealer_hit(self):
        if self.name == "Dealer":
            self.hand_print()
            while self.score < 17:
                pause = input("<Press Enter to Continue>")
                self.player_cards.append([random.choice(cards), random.choice(suit)])
                self.scoring()
                self.hand_print()


    def hand_print(self):
        self.printable_hand = f"{self.name}'s hand: \n"
        for show_cards in self.player_cards:
            self.printable_hand += f"{show_cards[0]} of {show_cards[1]}, "
        self.printable_hand = self.printable_hand[0:-2]
        clear()
        print(blackjack_title)
        if self.name != "Dealer":
            print(f"Dealer shows {dealer.player_cards[0][0]} of {dealer.player_cards[0][1]} \n")
            print(self.printable_hand + "\nScore: " + str(self.score) + " Wins: " + str(self.wins) + " Losses: " + str(self.losses))
        if self.name == "Dealer":
            print(self.printable_hand + "\nScore: " + str(self.score))
            print(player_1.printable_hand + "\nScore: " + str(player_1.score) + " Wins: " + str(player_1.wins) + " Losses: " + str(player_1.losses))

    def scoring(self):
        self.score = 0
        self.ace = False
        for card in self.player_cards:
            self.score += card_value[card[0]]
        for ace in self.player_cards:
            if 'Ace' in ace and self.score <= 11:
                self.score += 10
                self.ace = True
    
    def winner(self):
        if self.score >= dealer.score and self.score <= 21 or self.score <= 21 and dealer.score > 21:
            print(self.name + " Wins!")
            self.wins += 1
        else:
            print("Dealer wins.")
            self.losses += 1
        play = ""
        while not play:
            play = input("Would you like to play again? Y/N")
            try:
                if play[0].lower() == "n":
                    self.play_again = False
                elif play[0].lower() != "y":
                    play = ""
                    clear()
                    print(blackjack_title)
                    print(f"{self.name} - Wins: {self.wins} Losses: {self.losses}")
            except IndexError:
                clear()
                print(blackjack_title)
                print(f"{self.name} - Wins: {self.wins} Losses: {self.losses}")
                continue
        if self.play_again:
            self.redeal()
            dealer.redeal()
    
    def redeal(self):
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]
        self.scoring()


        
clear()
print(blackjack_title)
player_1 = Hand(input("What should I call you?"))
dealer = Hand("Dealer")

while player_1.play_again == True:
    player_1.hit_me()
    dealer.dealer_hit()
    player_1.winner()
