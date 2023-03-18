import random


#definir as variaveis a ser usadas na descricao de um baralho de 52 cartas
card_suits = ["clubs", "diamonds", "hearts", "spades"]
card_ranks = ["king", "queen", "jack", "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #cartas diferentes que existem num naipe
card_values = {"ace": 11 or 1, "king": 10, "queen": 10, "jack": 10, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}


#descrever uma carta
class card:
    def __init__(self, suits, ranks, values):
        self.suits = suits
        self.ranks = ranks
        self.values = card_values[card_ranks]



random.shuffle