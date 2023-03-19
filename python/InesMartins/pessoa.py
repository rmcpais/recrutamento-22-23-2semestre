#Módulo utilizado para gerir cartas do jogador e do dealer
class pessoa:

    def __init__(self):
        self._elem = []

    #Adicionar Carta
    def addCard(self, card):
        return self._elem.insert(-1, card)

    def seeCards(self):
        return self._elem

    #teste de natural
    def naturalTest(self):
        return len(self._elem)==2 and ("Ace" and "10" in self._elem)
    
    #soma do valor
    def sum(self):
        sum = 0
        for elem in self._elem:
            sum = sum + int(elem)
        return sum

    
    def wChecker(self):
        return self._elem.sum() == 21