#Módulo utilizado para alterar o dinheiro que o jogador pôs em jogo corretamente
class money:

    def __init__(self, budget):
        self._total = budget

        def __init__(self, bet):
            self._bet = bet

    def addWin(self, bet):
        self._total = self._total + 2*(bet)
        return self._total
    
    def addBlackjackWin(self, bet):
        self._total = self._total + (2.5)*(bet)
        return self._total