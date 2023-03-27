import random
from random import randrange
from random import randint

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
            #Escolha de tipo de carta
            self._type = random.choice(["Numbered", "Queen", "Numbered", "King", "Numbered", "Jack", "Ace"])

            #Associar valor respetivo
            if self._type == "Numbered":
                value = random.randint(2, 10)
            if self._type == "Ace":
                value = 11
            if (self._type == "Queen") or (self._type == "King") or (self._type == "Jack"):
                value = 10

            self._suit = random.choice(["hearts", "diamonds", "spades", "clubs"])

            if (str(str(self._type) + " of " + str(self._suit)) in self._elem) or (str(str(value) + " of " + str(self._suit)) in self._elem):
                name = False
            else:
                name = True

        if self._type != "Numbered":  
            self._elem.insert(0, str(self._type) + " of " + str(self._suit))
            return "★: " + str(self._type) + " of " + str(self._suit) + " - Value: " + str(value)
        else:
            self._elem.insert(0, str(str(value) + " of " + str(self._suit)))
            return "★: " + str(value) + " of " + str(self._suit) + " - Value: " + str(value) 

    def ultimoValor(self):
        ultValor = self._elem[0]
        if "Ace" == str(ultValor[0:3]):
            value = 11
        elif ("Queen" == str(ultValor[0:5])) or ("Jack" == str(ultValor[0:4])) or ("King" == str(ultValor[0:4])):
            value = 10
        else:
            s = "".join(x for x in str(ultValor[0]) if x.isdigit())
            value = int(str(s))
        return int(value)
    

    def naturalTest(self):
        return len(self._elem)==2 and ("Ace" and "10" in self._elem)
    
    def clear(self):
        self._elem = []
        return self._elem