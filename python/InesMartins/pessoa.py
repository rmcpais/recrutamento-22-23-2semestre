#Módulo utilizado para gerir cartas do jogador e do dealer
class pessoa:

    def __init__(self):
        self._elem = []

    #Adicionar Carta
    def addCard(self, card):
        return self._elem.insert(-1, card)

    def seeCards(self):
        return self._elem

    
    #soma do valor
    def sum(self):
        sum = 0
        for elem in self._elem:
            sum = sum + int(elem)
        return sum

    def clear(self):
        self._elem = []
        return self._elem
    