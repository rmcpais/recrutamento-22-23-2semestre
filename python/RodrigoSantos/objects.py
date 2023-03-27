# Objetos do Blackjack (cartas, jogador e pack, i.e. o conjunto de cartas p/ o jogo)


import random


class Card:

    def __init__(self, id):
        self._id = id
        self._type = "common"
        self._value = 0
        
        if self._id / 13 <= 1:
            self._suit = "clubs"
            self._idFactor = 0 
        elif 1 < self._id / 13 <= 2:
            self._suit = "diamonds"
            self._idFactor = 1
        elif 2 < self._id / 13 <= 3:
            self._suit = "hearts"
            self._idFactor = 2  
        else:
            self._suit = "spades"
            self._idFactor = 3

        figs = [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]
        aces = [1, 14, 27, 40]

        if int(self._id) in figs:
            self._value = 10
            self._type = "figure"

        elif self._id in aces:
            self._value = 0
            self._type = "ace"
            
        else:
            self._value = self._id - self._idFactor * 13
    
    def id(self):
        return int(self._id)
    
    def value(self):
        return self._value
    
    def value_set(self, num):
        if num == 11:
            self._value = 11
        self._value = 1
        
    def __repr__(self):
        if self.id() == 1 or self.id() == 14 or self.id() == 27 or self.id() == 40:
            return  "Ace of " + self.suit() 
        
        if self.id() == 11 or self.id() == 24 or self.id() == 37 or self.id() == 50:
            return  "Jack of " + self.suit()

        if self.id() == 12 or self.id() == 25 or self.id() == 38 or self.id() == 51:
            return  "Queen of " + self.suit() 
        
        if self.id() == 13 or self.id() == 26 or self.id() == 39 or self.id() == 52:
            return  "King of " + self.suit()
        
        return str(self.value()) + " of " + self.suit()

    def suit(self):
        return self._suit
    
    def type(self):
        return self._type
    

class Pack:

    def __init__(self):
        self._pack = set()
        count = 0
        while count < 7:
            for i in range(1, 53):
                self._pack.add(Card(i))
            count += 1

    def packIds(self):
        packIds = []
        for card in self._pack:
            packIds.append(card.id())
        return packIds
    
    def pack(self):
        return self._pack
    
    def remove(self, card):
        self._pack.remove(card)
    
    def pull(self, player):
        id = random.choice(self.packIds())
        for card in self.pack():
            if card.id() == id:
                self.remove(card)
                player.hand(card)
                break

    def shuffle(self):
        random.shuffle(self._pack)
 
class Player:

    def __init__(self,cash):
        self._hand = []
        self._handValue = 0
        self._chips = cash // 50            

    def bet(self, n_chips):
        self._chips -= n_chips
    
    def hand(self, card=None):
        if card == None:
            return self._hand
        self._hand.append(card)
    
    def hand_reset(self):
        self._hand = []

    def chips(self, mult=0):
        if mult != 0:
            self._chips = self._chips * mult
            return self._chips
        return self._chips
    
    def cardTypes(self):
        types = []
        for card in self.hand():
            types.append(card.type())
        return types
        