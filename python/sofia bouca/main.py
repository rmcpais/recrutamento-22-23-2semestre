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
        for card in self.deck: #vamos iterar por cada 'card' da lista 'deck'
            comb_deck += ' \n ' + card.__str__()
        return 'Deck: ' + comb_deck
