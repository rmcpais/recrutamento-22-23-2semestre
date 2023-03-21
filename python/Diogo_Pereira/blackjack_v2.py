import os
import random

suits = ["♠", "♥", "♦", "♣"]
values = {"A" : 11,
          "2" : 2,
          "3" : 3,
          "4" : 4,
          "5" : 5,
          "6" : 6,
          "7" : 7,
          "8" : 8,
          "9" : 9,
          "J" : 10,
          "Q" : 10,
          "K" : 10
        }


class Deck():
    def __init__(self):
        self.deck = []
        for v in values:
            for n in suits:
                self.deck += [v + n]
        self.deck *= 6
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)
        self.cut = len(self.deck) - random.randint(60, 75)
        self.count = 0

    def deal(self):
        card = self.deck[self.count]
        self.count += 1
        if self.count >= self.cut:
            self.shuffle()
        return card

class User():
    def __init__(self):
        self.points = 0
        self.cards = []
    
    def add_card(self, card):
        self.cards += [card]
        if card[0] == "A":
            display_text([f"You got an Ace ({card}). Select value:"], False)
            choice = []
            options_form(["1.", "11."], choice, 2, False)
            choice = choice[0]
            if choice == 1: self.points += 1
            elif choice == 2: self.points += 11
        else:
            self.points += values[card[0]]
    
    def reset(self):
        self.points = 0
        self.cards = []

    def __str__(self):
        return "You have the cards " + str(self.cards) + " and " + str(self.points) + " points."


class Dealer():
    def __init__(self):
        self.points = 0
        self.cards = []

    def add_card(self, card):
        self.cards += [card]
        if card[0] == "A":
            if self.points > 10: self.points += 1
            else: self.points += 11
        else:
            self.points += values[dealer_card[0]]
    
    def reset(self):
        self.points = 0
        self.cards = []

    def __str__(self):
        return "The dealer has the cards " + str(self.cards) + " and " + str(self.points) + " points."



def clear_screen():
    if os.name == 'posix': os.system('clear')
    else: os.system('cls')

def text_form(labels, values, inputConds, inputTypes, n, clear):
    if clear: clear_screen()
    for i in range(n):
        valid = False
        while not valid:
            try:
                value = input(labels[i] + ": ")
                if not inputConds[i](value): print("Invalid Input.")
                else: valid = True; values += [inputTypes[i](value)]
            except: print("Invalid Input.")

def options_form(options, value, n, clear):
    if clear: clear_screen()
    print("Options:")
    for i in range(n):
        print("\t" + str(i + 1) + ": " + options[i])
    valid = False
    while not valid:
        try:
            v = input("Choice: ")
            if int(v) < 1 or int(v) > n: print("Invalid Input.")
            else: valid = True; value += [int(v)]
        except: print("Invalid Input.")

def display_text(lines, clear):
    if clear: clear_screen()
    for line in lines:
        print(line)

def wait():
    input("Press <Enter> to continue.")


        
startingValue = []
text_form(["Starting Amount"], startingValue, [lambda x: int(x) > 0], [int], 1, True)
startingValue = startingValue[0]

money = startingValue
deck = Deck()
user = User()
dealer = Dealer()



game = True
while game:
    choice = []
    options_form(["Start Game.", "Quit."], choice, 2, True)
    choice = choice[0]
    if choice == 1: pass
    elif choice == 2: game = False; break
    
    bet = []
    text_form([f"Money Bet (Total = {money}€)"], bet, [lambda x: int(x) > 0 and int(x) <= money], [int], 1, True)
    bet = bet[0]

    money -= bet
    
    stop = False

    user_card = deck.deal()
    user.add_card(user_card)
    display_text([user], True)
    dealer_card = deck.deal()
    dealer.add_card(dealer_card)
    display_text([dealer], False)
    wait()
    dealer_card = deck.deal()
    dealer.add_card(dealer_card)
    user_card = deck.deal()
    user.add_card(user_card)
    if dealer.cards[0][0] in ["A", "J", "Q", "K"]:
        display_text([dealer], True)
        display_text([user], False)
    else:
        display_text([user], True)
        display_text([dealer], False)
    wait()

    while ((user.points < 21 and not stop) or dealer.points < 17) and dealer.points <= 21 and user.points <= 21:
        if dealer.points < 17:
            dealer_card = deck.deal()
            dealer.add_card(dealer_card)
        
        if user.points < 21:
            choice = []
            options_form(["Hit.", "Stand."], choice, 2, False)
            choice = choice[0]
            if choice == 1:
                user_card = deck.deal()
                user.add_card(user_card)
                display_text([user], True)
            elif choice == 2: stop = True
        
        display_text([dealer], False)
        wait()

    if user.points > dealer.points or dealer.points > 21:
        if user.points < 21: money += 2 * bet
        elif user.points == 21: money += 2.5 * bet
        else: display_text(["Skill Issue."], True); wait()
    elif user.points == dealer.points == 21: money += bet
    else: display_text(["Skill Issue."], True); wait()

    if money == 0: display_text(["You have no money! Get out of here, you bum!"], True); break
    else: display_text([f"You now have {money}€."], True)
    wait()

    user.reset()
    dealer.reset()


if money < startingValue: display_text([f"You walked away with a {startingValue - money}€ loss."], True)
elif money == startingValue: display_text(["You might not have won money, but at least you also didn't lose anything."], True)
else: display_text([f"Congratulations! You won {money - startingValue}€!"], True)
wait()
