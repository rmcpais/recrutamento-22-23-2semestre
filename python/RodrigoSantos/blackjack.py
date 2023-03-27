from objects import *
from time import sleep

globalAceValue = None
cash = None
dealer = Player(7000)

def ace_set():
    aceFinder = 0
    for card in player1.hand():
        if card.type() == "ace":
            aceFinder += 1
            break
    
    if aceFinder == 1:
        aceValue = input(random.choice["Uh, looks like you got an ace. What would you like its value to be? [1/11]",
                                           "An ace! What would you like it to be worth?",
                                           "Alright, how would you like to set the ace's value?"])
        for card in player1.hand():
            if card.type() == "ace":
                card.value_set(aceValue)
        return globalAceValue == aceValue

def ace_update():
    for card in player1.hand() or dealer.hand():
        if card.value() == 0:
            card.value_set(globalAceValue)

while not isinstance(cash, float):
    cash = input("Welcome to the HS Casino! How much money would you like to bet?\n")
    sleep(1)
    try:
        float(cash)
    except ValueError or TypeError:
        print("\nReally? I'm not in the mood for games, pal. Let's take a deep breath and start from the beginning.")
        sleep(0.5)
    else:
        cash = float(cash)

player1 = Player(cash)

while isinstance(cash, str):
    print("Really dude... come on, for real this time.")
    cash = float(input("Let's try again. How much money would you like to bet?\n"))


while cash < 0:
    print("Come on! Negative money? Really? What's next, you'll say you wanna bet 'sofa' euros? Be reasonable.")
    cash = float(input("Let's try again. How much money would you like to bet?\n"))


while cash < 50:
    print("\nI'm sorry. If you're broke, you could have just said that. Minimum bet is 50, pal.")
    sleep(0.5)
    cash = float(input("Let's try again. How much money would you like to bet?\n"))

pack = Pack()
sleep(0.50)

if cash > 10000:
    print("\nGreat! I must say, that'll keep us going for a while.\n")

if (cash//50) == 1:
    print("Wow, that'll give you a grand total of... A SINGLE CHIP! I swear to god, if you turn a profit on this...")
    sleep(1)
else: 
    print("\nAlright. That's ", int(cash // 50), "chips. Let's get started, shall we?")
    sleep(1)

roundCounter = 1
while player1.chips() > 0 and dealer.chips() > 0:

    
    print("\nROUND ", roundCounter)
    sleep(1)
    print("\nCHIPS REMAINING: ", player1.chips())
    sleep(1)
    
    bet = None

    while not isinstance(bet, int):
        bet = input("\nHow many chips do you wanna put down this round?\n")
        try:
            int(bet)
        except ValueError or TypeError:
            sleep(1)
            bet = input("Please remember: you can't bet 'x' chips or anything like that. It's not funny. Let us try again.") 
        else:
            bet = int(bet)
    

    while bet > player1.chips():
        sleep(1)
        bet = input("\nYou can't bet more than you have, genius. So, again: how many will you put down?\n")
        try:
            int(bet)
        except ValueError or TypeError:
            sleep(1)
            bet = input("Please remember: you can't bet 'x' chips or anything like that. It's not funny. Let us try again.") 

    bet = int(bet)

    player1.bet(bet)
    sleep(0.5)
    
    print("\nOk, your chips are in the pot now. Hope you don't regret that!")
    
    pack.pull(player1)
    print("You pull a card.")
    sleep(1)
    print("\nYour hand: ", player1.hand())
    sleep(1)
    ace_set()
    print("\nYou pull another card.")
    sleep(1)
    pack.pull(player1)
    print("\nYour hand: ", player1.hand())
    ace_set()
    ace_update()
    sleep(1)

    playerPoints = 0
    for cards in player1.hand():
        playerPoints += cards.value()

    if playerPoints > 21:
         sleep(1)
         print("Oops! Looks like it's a bust.")
         sleep(1)
         print("Don't worry though, let's go for another round.")
         roundCounter += 1
         player1.hand_reset()    

    pack.pull(dealer)
    print("Dealer's hand: ", dealer.hand())

    sleep(0.25)

    dealerPoints = 0
    for cards in dealer.hand():
        dealerPoints += cards.value()

    playerPoints = 0
    for cards in player1.hand():
        playerPoints += cards.value()  

    if dealerPoints == 21:
        print("\nUh, looks like I'm a natural! But don't worry, you may still draw this...")
         
    if playerPoints == 21:
        print("\n A natural, hey? I can still draw this.")

    if playerPoints != 21:
        response = input("\nDo you want to pull another card? [y/n]\n")
        lowerResp = response.lower()
        possibleResp = ["y", "yes", "n", "no"]

        if lowerResp not in possibleResp:
            while lowerResp not in possibleResp:
                sleep(1)
                response = input("Come on, I don't have all day! It's a yes or no question. Do you want to draw another card? [y/n]")
                lowerResp = response.lower()


            while lowerResp == ("y" or "yes"): 
                sleep(1)   
                print(random.choice(["Alright then!", "Ok!", "Alright, sure!"]))
                pack.pull(player1)
                ace_set()
                ace_update()
                sleep(0.5)
                print("\nYour hand: ", player1.hand())
                sleep(0.5)
                playerPoints = 0
                for cards in player1.hand():
                    playerPoints += cards.value() 
                if playerPoints > 21:
                    print("Oops! Looks like it's a bust.")
                    sleep(0.5)
                    print("Don't worry though, let's go for another round.")
                    roundCounter += 1
                    player1.hand_reset()
                    break 
                response = input(random.choice(["\nSo, wanna go again? The deck's calling [y/n]\n",
                                                "\nOne more? [y/n]", 
                                                "\nAnother one? [y/n]"]))
                lowerResp = response.lower()

    dealerPoints = 0
    for cards in dealer.hand(): # tentei implementar isto como uma função inerente à classe Player, mas surgiam imensos bugs.
        dealerPoints += cards.value() # esta solução mais bruta foi a melhor que encontrei, no tempo que tive
        
    while dealerPoints < 17:
        pack.pull(dealer)
        print("The dealer has pulled a card.")
        sleep(1)        
        print("\nDealer's hand: ", dealer.hand())
        sleep(1)        
        dealerPoints = 0
        for cards in dealer.hand():
            dealerPoints += cards.value() 
        print("Dealer's hand value = ", dealerPoints)
        sleep(1)

    if dealerPoints > 21:
        print("\nDamn it! It's a bust. I'll get you next time...")
        player1.hand_reset()
        dealer.hand_reset()
        player1.chips(2)

    playerPoints = 0
    for cards in player1.hand():
        playerPoints += cards.value() 

    if 21 > dealerPoints > playerPoints:
        print("\nAha! I win. Let's go for another round.")
        player1.hand_reset()
        dealer.hand_reset()
    
    if dealerPoints < playerPoints < 21:
        print("\nBeginner's luck. Another round, shall we?")
        player1.hand_reset()
        dealer.hand_reset()
        player1.chips(2)

    if dealerPoints < playerPoints and playerPoints == 21:
        print("\nA natural?. Another round!")
        player1.hand_reset()
        dealer.hand_reset()
        player1.chips(2.5)

    if dealerPoints > playerPoints and dealerPoints == 21:
        print("\nAHA! I'm so good a this game! Next round!")
        player1.hand_reset()
        dealer.hand_reset()

    if dealerPoints == playerPoints:
        print("\nA draw?. Boring!")
        player1.hand_reset()
        dealer.hand_reset()
    
    roundCounter += 1
