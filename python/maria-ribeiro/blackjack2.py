import random 

class Blackjack:
    def __init__(self):
        self.player_money = float(input("\nGame Money: "))
        self.player_points = 0
        self.dealer_points = 0
        self.deck = []
        self.bet = 0
        self.continue_play = "Y"
        self.busted = False

    def make_deck(self):
        for suit in range(4):
            for value in range(1,14):
                self.deck.append((suit, value))


    def print_card(self, value):
        if value == 11:
            return "J"
        if value == 12:
            return "Q"
        if value == 13:
            return "K"
        if value == 1:
            return "A"
        else:
            return value
                
    
    def card_points(self, value, isDealer):
        if isDealer:
            if value <= 10 and value > 1:
                return value
            if value == 1:
                if self.dealer_points + 10 > 17 and self.dealer_points + 10 < 21:
                    return 10
                else:
                    return 1
            else:
                return 10
            
        if not isDealer:
            if value <= 10 and value > 1:
                return value
            if value == 1:
                points = float(input("Is the Ace worth 1 or 10? "))
                return points 
            else:
                return 10

    def draw(self, isDealer):
        card_removed = False
        while card_removed == False:
            suit = random.randrange(0,3)
            value = random.randrange(1,14)
            if (suit, value) in self.deck:
                self.deck.remove((suit, value))
                card_removed = True
                if isDealer:
                    self.dealer_points += Blackjack.card_points(self, value, True)
                else:
                    self.player_points += Blackjack.card_points(self, value, False)
        return (suit, value)
    
                
    def check_blackjack(self):
        if self.dealer_points == 21:
            print("The Dealer has a natural Blackjack! You lost this round.")
            self.player_money -= self.bet
            self.continue_play = input("Another Round? Y or N ")
            Blackjack.print_money(self)

        if self.player_points == 21:
            print("You have a natural Blackjack! You won this round!")
            self.player_money += 1.5 * self.bet
            self.continue_play = input("Another Round? Y or N ")
            Blackjack.print_money(self)

        if self.player_points == 21 and self.dealer_points == 21:
            print("Both you and the dealer have a natural Blackjack! You get to keep your money!")
            self.continue_play = input("Another Round? Y or N ")
            Blackjack.print_money(self)


    def check_bust(self):
        if self.player_points > 21:
            print("\nYou busted!")
            self.player_money -= self.bet
            self.continue_play = input("Another Round? Y or N ")
            Blackjack.print_money(self)
            self.busted = True
            return True
        
    def print_money(self):
        if self.continue_play == "Y":
            print("\nYou have ", self.player_money, "€")
        else:
            print("\nYou leave the game with ", self.player_money, "€")

    
    def blackjack(self):
        while self.player_money >= 0 and self.continue_play == "Y":
            self.busted=False
            self.player_points = 0
            self.dealer_points = 0
            Blackjack.make_deck(self)
            self.bet = float(input("\nRound Money: "))
            while self.bet > self.player_money:
                self.bet = float(input("Round Money: "))
            
            card = Blackjack.draw(self, False)
            print("\nYou got a ", Blackjack.print_card(self, card[1]))
            card = Blackjack.draw(self, False)
            print("You got a ", Blackjack.print_card(self, card[1]))
            print("You have ", self.player_points, " points")

            card = Blackjack.draw(self, True)
            print("\nThe dealer got a ", Blackjack.print_card(self, card[1]))
            card = Blackjack.draw(self, True)

            Blackjack.check_blackjack(self)
            Blackjack.check_bust(self)
            
            if self.continue_play == "N":
                break

            continue_draw = input("\nDo you want another card? Y or N ")
            while continue_draw == "Y" and self.player_points < 21:
                card = Blackjack.draw(self, False)
                print("\nYou got a ", Blackjack.print_card(self, card[1]))
                print("You have ", self.player_points, " points")
                if Blackjack.check_bust(self):
                    if self.continue_play == "N":
                        break 
                else:
                    continue_draw = input("\nDo you want another card? Y or N ")

            if self.continue_play == "N":
                break

            if not self.busted:

                while self.dealer_points < 17:
                    card = Blackjack.draw(self, True)

                if self.dealer_points > self.player_points and self.dealer_points < 21:
                    self.player_money -= self.bet
                    print("The Dealer won! Good game!")
            
                if self.dealer_points < self.player_points or self.dealer_points > 21:
                    self.player_money += self.bet
                    print("You won! Congratulations!")
            
                if self.dealer_points == self.player_points:
                    print("It's a tie!")

                self.continue_play = input("\nAnother Round? Y or N ")
                Blackjack.print_money(self)


game = Blackjack()
game.blackjack()
            






                  







