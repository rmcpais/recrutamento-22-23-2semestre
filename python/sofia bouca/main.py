import random

#(naipe, tipo, valor)
#definimos o ás como 11 (apesar de tambem poder tomar o valor de 1) por default. mais tarde no codigo sao feitas as excecoes para quando tem que tomar o valor de 1
suits = {'Clubs', 'Diamonds', 'Hearts', 'Spades'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ace': 11} 

player_doing_stuff = True

#criar uma carta
class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit

#criar um baralho. 1o criar um vetor onde vao ser colocadas as cartas. as cartas irao vir de um conjunto ja ordenado
class deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))


    def __str__(self): #apesar de nao querer printar no final o conteudo do baralho inteiro, é boa pratica fazer o '__str__' para debugging
        comb_deck = ''
        for card in self.deck: #vamos iterar por cada 'card' da lista 'self.deck'
            comb_deck += ' \n ' + card.__str__() #representar cada carta atraves de strings
        return 'Deck: ' + comb_deck


#baralhar as cartas
def shuffle(self):
    random.shuffle(self.deck)

#distribuir as cartas
def deal(self):
    one_card = self.deck.pop()
    return one_card


class hand:
    def __init__(self):
        self.cards = []
        self.value = []
        self.aces = 0 #para poder determinar se na jogada o ás deve valer 1 ou 11 (por default vem com 11)

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
    
    def change_value_ace(self): #ajust
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class chips: #para atualizar apostas
    def __init__(self):
        self.total = 0
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
    
    def win_bet(self, blackjack=False):
        if blackjack:
            self.total += int(self.bet * 2.5)
        else:
            self.total += int(self.bet * 2)

#pergunta ao utilizador qual vai ser o valor da aposta 
def ask_bet(bet):
    while True:
        chips.bet = input('How much do you want to bet? ')
        if chips.bet != int:
            print('Error: please write a number: ')
        else: 
            if chips.bet < 2 or chips.bet > 500:
                print('Error: your bet must be between 2eur-500eur')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal()) #distribuimos uma carta do baralho para a adicionar à mao
    hand.change_value_ace() #para checkar se temos de atualizar o valor do ás


#pergunta ao jogador o que quer fazer 
def hit_vs_stand(deck, hand):
    global player_doing_stuff #se nao declarar como variavel global dentro desta funcao, seria criada uma nova variavel 'player_doing_stuff'.
                              #ou seja, alterar o valor desta variavel dentro desta funcao nao alteraria em nada o valor fora da funcao

    while True:
        question = input('\n Please choose if you want to hit ("h") or stand ("s"): ')

        if question == 'h':
            hit(deck, hand)
        elif question == 's':
            print("Player stands, Dearler's turn.")
            player_doing_stuff = False #utilizador deixa de jogar. é a vez do dealer
        else: 
            print('Error: invalid command. Please try again')
            continue
        break

def hide_dealer(player, dealer):
    print("\n --> Dealer's Hand: ")
    print("<face down>")
    print(dealer.cards[1]) #printa o segundo elemento do vetor 'cards' da classe 'hand' do dealer
    print("\n --> Player's Hand: ")
    for card in player.cards: #printa cada carta do utilizador numa linha diferente
        print(card)
    
def show_cards(player, dealer): #mostra as cartas e os seus valores
    print("\n --> Dealer's Hand: ")
    for card in dealer.cards: 
        print(card)
    print("\n --> Dealer's Value: ", dealer.value)
    print("\n --> Player's Hand: ")
    for card in player.cards: 
        print(card)
    print("\n --> Player's Value: ", player.value)


#fins possiveis
def player_wins(player, dealer, chips):
    print("You nailed it! Player wins!")
    chips.win_bet()

def player_busts(player, dealer, chips):
    print("Better luck next time :') \n Dealer wins!")
    chips.lose_bet()

def dealer_wins(player, dealer, chips):
    print("Better luck next time :') \n Dealer wins!")
    chips.lose_bet()

def dealer_busts(player, dealer, chips):
    print("You nailed it! Player wins!")
    chips.win_bet()

def stand_off(player, dealer): #nao precisamos de pôr 'chips' no argumento da funcao. em caso de empate, nenhuma ficha tem de ser paga a ninguem
    print("Stand-off: player has the same total as the dealer")


    

        





        





