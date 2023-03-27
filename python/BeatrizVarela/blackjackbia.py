import random 

class Player:

    def __init__(self, bet):
        self.pointcount = 0 
        self.acecount = 0
        self.cards = []
        self.bet = bet 

class Dealer:

    def __init__(self):
        self.pointcount = 0 
        self.acecount = 0
        self.cards = []

def shoemaker(decknumber):
    shoe = {}
    shoe["ace"] = decknumber * 4
    shoe["king"] = decknumber * 4
    shoe["queen"] = decknumber * 4
    shoe["jack"] = decknumber * 4
    shoe["two"] = decknumber * 4
    shoe["three"] = decknumber * 4
    shoe["five"] = decknumber * 4
    shoe["six"] = decknumber * 4
    shoe["seven"] = decknumber * 4
    shoe["eight"] = decknumber * 4
    shoe["nine"] = decknumber * 4
    shoe["ten"] = decknumber * 4
    return shoe 

def drawcard():
    card = random.choice(list(shoe)) 
    while shoe[card] == 0:
        card = random.choice(list(shoe))
    shoe[card] = shoe[card] - 1
    return card 


cardpoints = {"ace": 11, "king":10, "queen":10, "jack": 10, "one":1, "two":2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight":8, "nine": 9, "ten":10}
        
#intro 
print("Hi there! Welcome to BlackJack! ")
print("This is a two person game: dealer vs player; however the dealer will play automatically.")

deposit = float(input("How much would you like to deposit?"))

while deposit > 0:
    print("You have ", deposit, "$.")
    bet = float(input("How much would you like to bet in this round? "))

    #setting up dealer object
    dealer = Dealer()

    #setting up player object 
    player = Player(bet)

    #getting ready
    decknumber = int(input("Please tell me: how many decks would you like to play with?  "))
    shoe = shoemaker(decknumber)

    #round 1
    print("The dealer is now going shuffle all the cards and draw one for the player and another one for themselves")


    #player's 1st card 
    pcard1 = drawcard()
    player.pointcount += cardpoints[pcard1]
    if pcard1 == "ace": player.acecount += 1
    print("Player's first card is a ", pcard1)


    #dealer's 1st card
    dcard1 = drawcard()
    dealer.pointcount += cardpoints[dcard1]
    if dcard1 == "ace": dealer.acecount += 1
    print("Dealer's first card is a ", dcard1)

    #round 2
    print("Let's repeat!")

    #player 2nd card
    pcard2 = drawcard()
    if pcard2 == "ace": player.acecount += 1
    player.pointcount += cardpoints[pcard2]
    print("Player's second card is a ", pcard2)

    #dealer 2nd card
    dcard2 = drawcard()
    if dcard2 == "ace": dealer.acecount += 1
    dealer.pointcount += cardpoints[dcard2]

    if player.acecount == 1 and player.pointcount == 21:
        print("You got a BlACKJACK. Let's check what the dealer's got:")
        if "ace" in dealer.acecount == 1 and dealer.pointcount == 21:
            print("Dealer also got a BLACKJACK. You both get nothing... :(")
        else: 
            print("Dealer got ", dcard1, " and ", dcard2, " . Player wins 2.5x their bet: ", player.bet, "$ in total.")
            deposit = deposit + 2.5 * player.bet
    else: 
        print("Dealer's second card... won't be revealed!")

        print("Now the player will hit or stay...")


    while player.pointcount <= 21 and int(input("Player, please type 1 to hit and 2 to stay ")) == 1:

        card = drawcard()
        if card == "ace": player.acecount += 1
        player.pointcount += cardpoints[card]
        print("Player's new card is a ", card)
        #caso player seja bust reduzir os As
        if player.pointcount > 21 and player.acecount != 0:
            print("Oh no! Player has now ", player.pointcount," points! Let's take the aces into account...")
            for i in (0, player.acecount):
                if player.pointcount > 21:
                    player.pointcount = player.pointcount - 10
                    player.acecount = player.acecount - 1
        print("Player has ", player.pointcount, " points.")


    else:
        if player.pointcount > 21: print("Player busted with ", player.pointcount, " points. Dealer collects player's bet: ", player.bet,"$.")
        else: 
            print("Dealer's second card is a ", dcard2, " It is now their turn to draw cards.")
            while dealer.pointcount <= player.pointcount and dealer.pointcount <= 21:
                card = drawcard()
                if card == "ace": dealer.acecount += 1
                dealer.pointcount += cardpoints[card]
                print("Dealer's new card is a ", card)
                if dealer.pointcount > 21 and dealer.acecount !=0:
                    print("Oh no! Dealer has more than 21 points. Let's take the aces into account...")
                    for i in (0, dealer.acecount):
                        if dealer.pointcount > 21:
                            dealer.pointcount = dealer.pointcount - 10
                            dealer.acecount = dealer.acecount - 1
                print("Dealer has ", dealer.pointcount, " points.")
            else:
                if dealer.pointcount > 21: 
                    print("Dealer busted with ", dealer.pointcount, " points. Player collects 2x their bet: ",player.bet, "$.")
                    deposit = deposit + 2*player.bet
                else: 
                    print("Dealer wins and collects player's bet: ", player.bet, "$.")
                    deposit = deposit - player.bet

print("You have no money left!")


