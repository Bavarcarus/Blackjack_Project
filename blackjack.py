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

    def __init__(self, name, seat):
        self.name = name
        self.seat = seat
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]
        self.scoring()
        self.wins = 0
        self.losses = 0
        self.play_again = True

    def __repr__(self):
        return self.seat

    def hit_me(self):
        self.hand_print()
        self.stand = False
        self.blackjack = False
        if self.score == 21:
            self.blackjack = True
            temp = input("BLACKJACK!")
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
            self.blackjack = False
            if self.score == 21:
                self.blackjack = True
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
            for player in active_players:
                print(player.printable_hand + "\nScore: " + str(player.score) + " Wins: " + str(player.wins) + " Losses: " + str(player.losses))

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
        if self.score > dealer.score and self.score <= 21 or self.score <= 21 and dealer.score > 21 or self.blackjack and not dealer.blackjack:
            print(self.name + " Wins!")
            self.wins += 1
        elif self.blackjack and dealer.blackjack or self.score == dealer.score and not dealer.blackjack:
            print(f"{self.name}: Push")
        else:
            print(f"Dealer beats {self.name}.")
            self.losses += 1
        play = ""
        while not play:
            play = input(f"{self.name}, would you like to play again? Y/N")
            try:
                if play[0].lower() == "n":
                    self.play_again = False                    
                elif play[0].lower() != "y":
                    play = ""
                    clear()
                    print(blackjack_title)
                    print(f"{self.name} - Wins: {self.wins} Losses: {self.losses}")
                elif play[0].lower() == "y":
                    self.play_again = True
            except IndexError:
                clear()
                print(blackjack_title)
                print(f"{self.name} - Wins: {self.wins} Losses: {self.losses}")
                continue
        if self.play_again:
            self.redeal()
            #dealer.redeal()
    
    def redeal(self):
        self.player_cards = [[random.choice(cards), random.choice(suit)], [random.choice(cards), random.choice(suit)]]
        self.scoring()


new_player = False       
num_player = 0
while num_player == 0:
    clear()
    print(blackjack_title)
    try:
        num_player = int(input("There are 4 seats available, how many players?"))
        if num_player < 0 or num_player > 4:
            num_player = 0
    except ValueError:
        num_player = 0

player_1 = Hand("Player 1", "Seat 1")
player_2 = Hand("Player 2", "Seat 2")
player_3 = Hand("Player 3", "Seat 3")
player_4 = Hand("Player 4", "Seat 4")
dealer = Hand("Dealer", "Seat 0")
player_list = [player_1, player_2, player_3, player_4]
active_players = []
inactive_players = []
for n in range(num_player):
    active_players.append(player_list[n])
    active_players[n].name = input(f"What is {active_players[n].name}'s name?")

while num_player > 0:
    if num_player < 4:
        new_player = True 
        while new_player:
            player_join = input(f"There are {len(inactive_players)} seats available, how many wish to join?")
            try:
                if int(player_join) <= len(inactive_players) and int(player_join) != 0:
                    for n in range(int(player_join)):
                        inactive_players[n].name = input(f"What is your name?")
                        inactive_players[n].redeal()
                        inactive_players[n].wins = 0
                        inactive_players[n].losses = 0
                        active_players.append(inactive_players[n])
                        num_player += 1
                    for player in active_players:
                        if player in inactive_players:
                            inactive_players.remove(player)
                    new_player = False
                elif int(player_join) == 0:
                    new_player = False
            except:
                continue
        active_players.sort(key=lambda hand: hand.seat)

    for player in active_players:
        player.hit_me()
    dealer.dealer_hit()
    for player in active_players:
        player.winner()
        if not player.play_again:
            inactive_players.append(player)
            num_player -= 1
    for quitter in inactive_players:
        if quitter in active_players:
            active_players.remove(quitter)
    dealer.redeal()

