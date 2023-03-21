import random
import time
import math


'''
	Created by Filipe Piçarra
	  15/03 - 21/03 | 2023
	Recrutamento HackerSchool
'''


# Dictionary that defines each value's... value
VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

# List containing all the Npc's, with their names, confidance value and starter money
NPCS = [
    ("Carlos Bispo", 0.7, 3500),
    ("Nuno Roma", 0.35, 2000),
    ("Nuno Horta", 0.1, 2400),
    ("Pedro Ramos", 0.75, 10000),
    ("O Epifânio", 0.7, 7E14),
    ("Carlos Conceição", 0.5, 20),
    ("Carlos Baleizão", 0.4, 500),
    ("Conceição Amado", 0.64573861, 3500),
    ("Felix", 0.55, 1450),
    ("Armando Inverno", 0.31, 57000),
    ("Esmeralda Dias", 0.47, 7600),
    ("Cláudia Phillip", 0.5764587388, 20500),
    ("Virginia Bispo", 0.25, 500),
    ("Lígia Milheiro", 0.80, 6000),
    ("Nuno Serra", 0.6, 100)
]


# Class that defines a player, npc or dealer
class Player:
    def __init__(self, coins, ci=0.5, name="Player"):
        self.coins = coins
        self.initial_coins = coins
        self.hand = None
        self.name = name
        self.confidance_interval = ci

    # If the player has enough coins for a bet returns True and removes said coins, otherwise, returns False
    def bet(self, value):
        if value > self.coins:
            return False
        self.coins -= value
        return True

    # Defines if a npc will bet or pass the round
    def bot_bet(self):
        # Based on the ratio between how many coins have been lost/won, the npc will decide how mush he will bet
        # or just leave the table
        x = self.confidance_interval+(self.coins / self.initial_coins)
        if random.random() < x:
            y = math.ceil(self.confidance_interval*self.coins)
            self.bet(y)
            return y
        return 0

    # Defines if a npc will hit or pass given its hand
    def bot_hit_pass(self):
        hand = self.hand_value()
        if hand <= 11:
            return True
        dist = (21 - hand)/21
        chance = self.confidance_interval + dist - (1-dist**2)*0.7
        if random.random() < chance:
            return True
        return False

    # gimme ma coins
    def win(self, value):
        self.coins += value

    # Prints a player's name, hand and hand-value
    def __str__(self) -> str:
        cards = ""
        text = self.name.rjust(16)
        try:
            for card in self.hand:
                cards += (card[0]+card[1]+"  ").rjust(1)
        except TypeError:
            cards += "Empty Hand"

        cards = cards[:-1].rjust(20)
        hand = (" | Hand Value:" + str(self.hand_value()).rjust(2) + " | ")
        return text+hand+cards

    # Options that does not print the dealers second card, and total hand value
    def print_dealer(self):
        text = self.name.rjust(16) + " | Hand Value: ?".rjust(2) + " | "
        text += ((self.hand[0][0]+self.hand[0][1]+"  ").rjust(1)+"** ".rjust(1)).rjust(20)
        print(text)

    # Returns how much the hand is worth
    def hand_value(self):
        total = 0
        aces = 0
        for card in self.hand:
            total += VALUES[card[0]]
            if card[0] == 'A':
                aces += 1
        while (total > 21) and (aces > 0):
            total -= 10
            aces -= 1
        return total


# Class that defines a normal 56 cards deck
class Deck:
    def __init__(self):
        self.stack = []
        self.first = None

        suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for value in values:
                self.stack.append((value, suit))
        random.shuffle(self.stack)
        self.last = self.stack[0]

    def deal(self, n_cards=1):
        if len(self.stack) < n_cards:
            return None
        draw_list = []
        for n in range(n_cards):
            draw_list.append(self.stack.pop())
        return draw_list

    # if the card that just returned is the last, reshuffle the whole deck
    def return_to_deck(self, card):
        self.stack.insert(0, card)
        if card == self.last:
            random.shuffle(self.stack)
            self.last = self.stack[0]


def init_players():
    # Asks how many coins does the player want to have
    while True:
        try:
            n_coins = int(input("Enter a number of coins to bet with: "))
            if n_coins < 0:
                continue
            break
        except ValueError:
            print("Sorry can't recognise that number... maybe GPT might...")

    # How many npcs does the player want to play with
    try:
        n_npc = int(input("Enter a number of ncps to play with: "))
        if n_npc < 0 or n_npc > 7:
            if n_npc < 0:
                n_npc = 0
            else:
                n_npc = 7
    except ValueError:
        print("Sorry can't figure that number out... Let's see who joins the table!\n")
        n_npc = random.randint(1, len(NPCS))

    # Initiates the players list, with the entry at index 0 being the player itself
    player_list = [Player(n_coins)]
    for j in range(0, n_npc):
        npc = NPCS.pop(random.randint(0, len(NPCS)-1))
        player_list.append(Player(npc[2],
                                  npc[1],
                                  npc[0]))
    return player_list, [0]*(n_npc+1)


def print_players(p_list, b_list, dlr, hidden_dlr=False):
    print("\n")
    i = 0
    if hidden_dlr:
        dlr.print_dealer()
    else:
        print(dlr)

    for p in p_list:
        print(p, end="")
        print("\t| Bet: "+str(b_list[i]))
        i += 1
    print("\n")


# Function for the user to decide if it wants to hit or pass on a card
def hit_or_pass():
    while True:
        x = input("HIT or PASS? ")
        x = x.lower()
        if x[0] == 'p':
            return False
        elif x[0] == 'h':
            return True


# If the dealer has a blackjack, only the players who have another blackjack will recieve their money back
def dealer_blackjack(p_list, b_list, dlr):
    if dlr.hand_value() == 21:
        print("Dealer BlackJack!")
        i = 0
        for p in p_list:
            if p.hand_value() == 21:
                p.win(b_list[i])
                print(p.name+" won with a BlackJack!!")
            else:
                print(p.name+" lost...")
            i += 0
        return True
    return False


# If the dealer busts, give each player what they earned
def dealer_bust(p_list, b_list, dlr):
    if dlr.hand_value() > 21:
        print("Dealer BUST!!")
        i = 0
        for p in p_list:
            h = p.hand_value()
            if h == 21:
                p.win(b_list[i]*2.5)
                print(p.name + " has a BlackJack!!")
            elif h < 21:
                p.win(b_list[i]*2)
                print(p.name + " won...")
            else:
                print(p.name + " lost...")
            i += 0
        return True
    return False


# If the dealer does not bust or has a blackjack
# this function decides who wins or looses
def dealer_normal_hand(p_list, b_list, dlr):
    i = 0
    d_hand = dlr.hand_value()
    for p in p_list:
        h = p.hand_value()
        if h == 21:
            p.win(b_list[i] * 2.5)
            print(p.name + " has a BlackJack!!")
        elif h > 21:
            print(p.name + " BUST...")
        elif h < d_hand:
            print(p.name + " lost...")
        elif h == d_hand:
            print(p.name + " tie with dealer...")
            p.win(b_list[i])
        elif h > d_hand:
            p.win(b_list[i] * 2)
            print(p.name + " won!!")
        i += 0


# Retrieves all the cards in the table and puts them at the end of the deck
def retrieve_cards(p_list, dck):
    for p in p_list:
        for card in p.hand:
            dck.return_to_deck(card)


# Wait a given time and makes a cool ... animation
def wait(wait_time):
    timer = wait_time/3
    print(".", end="")
    time.sleep(timer)
    print(".", end="")
    time.sleep(timer)
    print(".")
    time.sleep(timer)


# Starting the game itself, let us first initiate the deck, dealer, and players
deck = Deck()
dealer = Player(-1, 0, "Dealer's")
player_list, bets_list = init_players()

# While the player has money to its name
while player_list[0].coins > 0:
    # set all the bets to zero
    for i in bets_list:
        i = 0
    # Attempt to ask for a bet in this round, if the player bets <= 0, the game will end
    # If the player asks bets for money that he does not have ...
    # give one card to the player
    try:
        bet = int(input(f"Coins: {player_list[0].coins} | Bet? "))
        if bet > 0:
            if player_list[0].bet(bet):
                bets_list[0] = bet
                player_list[0].hand = deck.deal()
            else:
                print("You don't have that many coins!")
        else:
            break
    except ValueError:
        break

    # Retrieve the bet values of all the other npc's, based on their confidence and earned coins
    # Give every npc a card, if they have bet something
    # If they don't bet they will be kicked from the table
    i = 1
    for player in player_list[1:]:
        bet = player.bot_bet()
        if bet > 0:
            bets_list[i] = bet
            player.hand = deck.deal()
            i += 1
        else:
            player_list.pop(i)
            bets_list.pop(i)

    # Deal one card to the dealer
    dealer.hand = deck.deal()
    print_players(player_list, bets_list, dealer)

    print("\nNext cards", end="")
    wait(1.2)

    # Second dealing round has begun!
    for player in player_list:
        player.hand += deck.deal()
    dealer.hand += deck.deal()

    print_players(player_list, bets_list, dealer, True)

    # Checks if the dealer has a blackjack, if he has, only the play who also share one will tie
    # The rest will lose and the round will end
    if dealer_blackjack(player_list, bets_list, dealer):
        continue

    # Asks if the player wants to hit or pass on a card, while he does not bust
    n_busts = 0
    if player_list[0].hand_value() < 21:
        while hit_or_pass():
            player_list[0].hand += deck.deal()
            hand = player_list[0].hand_value()
            print_players(player_list, bets_list, dealer, True)
            if hand == 21:
                print("You have a BlackJack!")
                break
            elif hand > 21:
                n_busts += 1
                print("BUST...")
                break

    # Runs the algorithm to check if the npc's want to hit or pass on a card
    # This works by combining their confidence level with the distance to a blackjack
    # But, has said distance increases, their chances to hit will start to decrease
    for player in player_list[1:]:
        while player.bot_hit_pass():
            print(f"{player.name} is deciding", end="")
            wait(2)
            player.hand += deck.deal()
            hand = player.hand_value()
            print_players(player_list, bets_list, dealer, True)
            if hand == 21:
                print(f"{player.name} has a BlackJack!")
                break
            elif hand > 21:
                print(f"{player.name} BUSTED...")
                n_busts += 1
                break

    # While the dealers hand has a value that is less than 17, the dealer will get more cards
    while dealer.hand_value() < 17 and n_busts < len(player_list):
        dealer.hand += deck.deal()

    print_players(player_list, bets_list, dealer)

    '''
    Now 4 things can happen:
        Every player busts, they all lose!
        
        Dealer has a blackjack:
            All the player that don't have a blackjack will lose,
            the remaining will tie with the dealer
        
        Dealer Busts:
            Everyone wins their respective earnings
        
        Normal Round:
            The player who have a blackjack and the ones that have more value in their hand than the dealer's
            will win their respective earnings, the ones that match the value will tie, and those whose hand value is
            less than the dealer's will lose
    '''
    if n_busts == len(player_list):
        print("No winners...", end="")
        wait(2.4)
        retrieve_cards(player_list, deck)
        continue
    if dealer_blackjack(player_list, bets_list, dealer):
        print("Next Round", end="")
        wait(2.4)
        retrieve_cards(player_list, deck)
        continue
    if dealer_bust(player_list, bets_list, dealer):
        print("Next Round", end="")
        wait(2.4)
        retrieve_cards(player_list, deck)
        continue

    dealer_normal_hand(player_list, bets_list, dealer)
    retrieve_cards(player_list, deck)
    print("Next Round", end="")
    wait(3.6)

