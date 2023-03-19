import random
from random import randrange

#Módulo uyilizado para gerar cartas e gerir as cartas em jogo
class cards:
    #Informações base
    cardTypes = ["Numbered", "Queen", "King", "Jack", "Ace"]
    cardSuits = ["hearts", "diamonds", "spades", "clubs"]

    def __init__(self):
        self._elem = []

        #Propriedades das cartas
        def __init__(self, suit, type, value):
            self._type = type
            self._value = value
            self._suit = suit
            self._names = []

    #Devolve historial de cartas
    def getCards(self):
        return self._elem
    
    #Gerar carta nova
    def newCard(self):
        name = False
        while not name:
            counter = 0
            #Escolha de tipo de carta
            self._type = random.choice(["Numbered", "Queen", "King", "Jack", "Ace"])


            while not name:
                if self._type == "Numbered":
                    value = randrange(1,10)

                if self._type == "Ace":
                    value = 11
                else:
                    value = 10

                self._suit = random.choice(["hearts", "diamonds", "spades", "clubs"])

                if str(str(self._type) + " of " + str(self._suit)) in self._elem or str(str(value) + " of " + str(self._suit)) in self._elem:
                    name = False
                else:
                    name = True

        if self._type != "Numbered":  
            self._elem.insert(-1, str(self._type) + " of " + str(self._suit))
            return "★: " + str(self._type) + " of " + str(self._suit) + " - Value: " + str(value)
        else:
            self._elem.insert(-1, str(str(value) + " of " + str(self._suit)))
            return "★: " + str(value) + " of " + str(self._suit) + " - Value: " + str(value) 

    def ultimoValor(self):
        for i in range(1, 11):
            if str(i) in self._elem[-1]:
                self._value = i
        if "Ace" in self._elem[-1]:
            self._value = 11
        else:
            self._value = 10
        return int(self._value)