
import random
import os

UNICODE_USABLE_VALUES = [i for i in range(0x1F0A1, 0x1F0AF) if i != 0x1F0AC]

class Player:
    
    balance = 0
    available_hand = []
    name = ""
    
    def __init__(self, available_balance, name = "Your"):
        self.balance = available_balance
        self.available_hand = []
        self.name = name
        
    def addCard(self, card):
        print("You got a " + str(card) + "  valuing " + str(card.getValueStr()) + " points" )
        while(card not in self.available_hand):
            if(card.getValue() == 1 or card.getValue() == 11):
                res = askForAnInt("Knowing that your hand is worth " + str(self.getHandValue()) + " points. Do you want your Ace to value 1 or 11? " )
                if(res == 1 or res == 11):
                    card.setValue(res)
                    self.available_hand.append(card)
                    print(self.name + " " + str(card) + "  is worth " + str(card.getValue()) + " points" )                    
                else:
                    print("Thats an invalid input...")
            else:
                self.available_hand.append(card)
        
    def getHand(self):
        return self.available_hand

    def getBalance(self):
        return self.balance

    #vou ter que dar fix a isto
    def getHandValue(self):
        handvalue = 0
        for card in self.available_hand:
            handvalue += card.getValue()
        return handvalue

    #for simplification the value won is rounded to the nearest integer
    def naturalWin(self, value_to_bet):
        self.balance += round(value_to_bet * 1.5)
        print("A natural win! WoW!")
        print("You won " + str(round(value_to_bet * 1.5)) + " dollars and now you have " + str(self.balance) + " dollars")
        
    def win(self, value_to_bet):
        print("YOU WON!")
        self.balance += value_to_bet
        print("You won " + str(value_to_bet) + " dollars and now you have " + str(self.balance) + " dollars")

    
    def lost(self, value_to_bet):
        print("YOU LOST!")
        self.balance -= value_to_bet
        print("You lost " + str(value_to_bet) + " dollars and now you have " + str(self.balance) + " dollars")
    
    def draw(self):
        print("Its a drawn :|")
        print("You still have " + str(self.balance) + " dollars")
    
    def getHandStr(self):
        string = ""
        for i in self.available_hand:
            string += str(i) + "  "
        string = self.name + " hand is: "+ string + "\nValuing on total " + str(self.getHandValue()) + " points"
        return string
        
class Dealer(Player):
    
    def __init__(self, name="Dealer"):
        super().__init__(0, name)
    
    def addCard(self, card):
        print("The dealer got a " + str(card) + "  valuing " + str(card.getValueStr()) + " points" )
        self.available_hand.append(card)
                    
    def getHandValue(self):
        handvalue = 0
        countaces = 0
        for card in self.available_hand:
            if(card.getHidden() == True):
                continue
            if(card.getValue() == 1 or card.getValue() == 11):
                countaces += 1
            handvalue += card.getValue()
        #This checks if the ace is worth 11 or 1
        if(countaces > 0 and handvalue + 10 <= 21):
            handvalue += 10
            countaces -= 1
        return handvalue

    def showAllCards(self):
        for i in self.available_hand:
            i.setShown()
        print("The dealer will show his hand!!\n" + self.getHandStr())


class Card:
    
    value = 0
    name_type = ""
    unicode_value = ''
    hidden = False
    
    def __init__(self, value, name_type, unicode_value):
        self.value = value
        self.name_type = name_type
        self.unicode_value = unicode_value
        
    def getValue(self):
        return self.value
    
    def getValueStr(self):
        return "?" if self.hidden else str(self.value) if self.value != 1 else "1 or 11"

    def getName(self):
        return self.name_type
    
    def getUnicode(self):
        return self.unicode_value
    
    def setHidden(self):
        self.hidden = True
        
    def getHidden(self):
        return self.hidden    
        
    def setShown(self):
        self.hidden = False
    
    def setValue(self, value):
        self.value = value
    
    
    def __str__(self):
        return chr(self.unicode_value) if not self.hidden else "🂠"
    
    def __repr__(self):
        return chr(self.unicode_value) if not self.hidden else "🂠"
    
    

def generate_deck(default = 1):
    deck = []
    value = 0
    for j in range(0, default):
        for i in range(0, 13):
            if(i >= 10):
                value = 10
            else:
                value = i + 1
            deck.append(Card(value, "hearts", UNICODE_USABLE_VALUES[i]))
            deck.append(Card(value, "diamonds", UNICODE_USABLE_VALUES[i] + 0x10))
            deck.append(Card(value, "spades", UNICODE_USABLE_VALUES[i] + 0x20))
            deck.append(Card(value, "clubs", UNICODE_USABLE_VALUES[i] + 0x30))
    return deck

def askForAnInt(msg):
    user_input = 0
    while(user_input == 0):
        user_input = input(msg)
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Input is not a positive integer.")
                user_input = 0
        except ValueError:
            print("Input is not a valid integer.")
            user_input = 0
    return user_input
    
def inicialize_player():
    return Player(askForAnInt("How much money do you have? "))

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dealerSetup(dealer, deck):
    dealer.addCard(deck.pop())
    dealer_card = deck.pop()
    dealer_card.setHidden()
    dealer.addCard(dealer_card)
    print(dealer.getHandStr())
    
def playerTurn(player, dealer, value_to_bet, deck):
    player.addCard(deck.pop())
    player.addCard(deck.pop())
    
    print(player.getHandStr())
    
    while(player.getHandValue() < 21):
        response = input("Do you want to hit or stand? (h/s) ")
        if response.lower() == 'h':
            clearScreen()

            print("You chose to hit.")
            print(dealer.getHandStr())
            player.addCard(deck.pop())
            newvalue = player.getHandValue()
            print(player.getHandStr())
            if(newvalue > 21):
                print("YOU BUSTED!")
                dealer.showAllCards()
                player.lost(value_to_bet)
                return True
        elif response.lower() == 's':
            clearScreen()
            print("You chose to stand.")
            print(dealer.getHandStr())
            print(player.getHandStr())
            dealer.showAllCards()
            while(dealer.getHandValue() < 17):
                print("Since the dealer has less than 17 points, he will hit")
                newcard = deck.pop()
                dealer.addCard(newcard)
                print(dealer.getHandStr())
            dealervalue = dealer.getHandValue()  
            playervalue = player.getHandValue()
            if(dealervalue > 21 or dealervalue < playervalue):
                if(dealervalue > 21):
                    print("DEALER BUSTED!")
                player.win(value_to_bet)
                return True
            elif(dealervalue > playervalue):
                player.lost(value_to_bet)
                return True
            else:
                player.draw()
                return True
        else:
            print("Invalid input, please try again.")
            continue
    
    if(player.getHandValue() == 21):
        dealer.showAllCards()
        if(dealer.getHandValue() == 21):
            print("You both have 21...")
            player.draw()
        else:
            player.naturalWin(value_to_bet)
    return True
    
    
def resetCards(player, dealer, deck):
    for i in range(len(player.getHand())):
        deck.append(player.getHand().pop())
    for i in range(len(dealer.getHand())):
        deck.append(dealer.getHand().pop())
    random.shuffle(deck)


def gameTurn(player, dealer, deck):
    value_to_bet = 0
    while( value_to_bet <= 0 or value_to_bet > player.getBalance()):
        value_to_bet = askForAnInt("How much do you want to bet? ")
        if(value_to_bet > player.getBalance()):
            print("My boy you dont have that much money 💀\nYou only have " + str(player.getBalance()) + " dollars")
    clearScreen()
    print("You will bet " + str(value_to_bet) + " dollars")
    dealerSetup(dealer, deck)
    if(playerTurn(player, dealer, value_to_bet, deck)):
        resetCards(player, dealer, deck)
        if(player.getBalance() == 0):
            return -1
    return 0
        
def startGame():
    clearScreen()
    deck = generate_deck(6)
    random.shuffle(deck)
    player = inicialize_player()
    dealer = Dealer()       
    stop = False 
    while(stop == False):
        response = input("Do you want to continue? (y/n) ")
        
        if response.lower() == 'y':
            print("Lets continue!")
            if(gameTurn(player, dealer, deck) == -1):
                print("Ahaha, no money? 🥺")
                return
        elif response.lower() == 'n':
            print("It was fun while it lasted, you ended with " + str(player.getBalance()) + " dollars.")
            stop = True
            return
        else:
            print("Invalid response.")
    
startGame()