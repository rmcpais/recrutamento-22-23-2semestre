import random

#(naipe, tipo, valor)
#definimos o ás como 11 (apesar de tambem poder tomar o valor de 1) por default. mais tarde no codigo sao feitas as excecoes para quando tem que tomar o valor de 1
suits = {'Clubs', 'Diamonds', 'Hearts', 'Spades'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ace': 11} 


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

class bet: #para atualizar apostas
    def __init__(self):
        self.total = 0
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
    
    def win_bet(self):
        self.total += self.bet





