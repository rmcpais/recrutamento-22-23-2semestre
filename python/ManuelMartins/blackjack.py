#Manuel Martins blackjack game 2023

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
                      for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            if card.value in ["J", "Q", "K"]:
                score += 10
            elif card.value == "A":
                aces += 1
                score += 11
            else:
                score += int(card.value)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score
    
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Hand()
    def reset_hand(self):
        self.hand = Hand()

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
    def add_player(self, name, money):
        self.players.append(Player(name, money))
    def start_round(self):
        self.deck = Deck()
        self.deck.shuffle()

        for player in self.players:
            player.reset_hand()
            for _ in range(2):
                player.hand.add_card(self.deck.deal())
    def play(self, player):
        print(f"{player.name}'s cards: {[str(card) for card in player.hand.cards]}")
        score = player.hand.calculate_score()
        print(f"{player.name}'s score: {score}")
        while True:
            action = input(f"{player.name}, do you want to hit or stand? ").lower()
            if action == "hit":
                player.hand.add_card(self.deck.deal())
                score = player.hand.calculate_score()
                print(f"{player.name}'s cards: {[str(card) for card in player.hand.cards]}, Score: {score}")
                if score > 21:
                    print(f"{player.name} busted!")
                    return False
                elif score == 21:
                    break
            elif action == "stand":
                break
            else:
                print("Invalid action. Please choose 'hit' or 'stand'.")
        return True

    def dealer_play(self, dealer):
        while dealer.hand.calculate_score() < 17:
            dealer.hand.add_card(self.deck.deal())

    def get_result(self, player, dealer):
        player_score = player.hand.calculate_score()
        dealer_score = dealer.hand.calculate_score()

        if player_score > 21:
            return -1
        elif dealer_score > 21 or player_score > dealer_score:
            return 1
        elif player_score == dealer_score:
            return 0
        else:
            return -1    

    def payout(self, player, bet, result):
        if result == 1:
            if player.hand.calculate_score() == 21 and len(player.hand.cards) == 2:
                player.money += bet * 2.5
            else:
                player.money += bet * 2
        elif result == 0:
            player.money += bet


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    initial_money = float(input("Enter your initial amount of money: "))

    game = BlackjackGame()
    game.add_player(player_name, initial_money)
    game.add_player("Dealer", 0)

    while game.players[0].money > 0:
        bet = float(input(f"{player_name}, enter your bet amount: "))
        while bet > game.players[0].money:
            print("You don't have enough money to make that bet.")
            bet = float(input(f"{player_name}, enter your bet amount: "))
        
        game.players[0].money -= bet
        game.start_round()

        player_busted = not game.play(game.players[0])
        if not player_busted:
            game.dealer_play(game.players[1])

        print(f"Dealer's cards: {[str(card) for card in game.players[1].hand.cards]}, Score: {game.players[1].hand.calculate_score()}")

        result = game.get_result(game.players[0], game.players[1])
        game.payout(game.players[0], bet, result)

        if result == 1:
            print(f"{player_name} wins!")
        elif result == 0:
            print("It's a tie!")
        else:
            print("Dealer wins!")

        print(f"{player_name}'s current balance: ${game.players[0].money}")

        if game.players[0].money <= 0:
            print("You are out of money!")
            break

        exit_game = input("Do you want to exit the game? (yes/no) ").lower()
        if exit_game == "yes":
            break