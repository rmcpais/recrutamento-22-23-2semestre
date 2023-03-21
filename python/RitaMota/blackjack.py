import random


class Carta:
    def __init__(self, naipe, carta, valor_carta):

        self.naipe = naipe
        self.carta = carta
        self.valor_carta = valor_carta


class Jogo():
    def __init__(self, baralho):
        self.montante_inicial = int(input("Montante inicial: "))
        if self.montante_inicial < 10:
            raise KeyError("É necessário no mínimo 10€")

        self.pontos_jogador = 0
        self.pontos_dealer = 0
        self.dinheiro_jogador = self.montante_inicial
        self._baralho = baralho


    def ace(self, _as):
        if _as.carta == "A":
            valor = int(input("Valor Às: 1 ou 11?"))
            if valor == 1:
                _as.valor = 1
            if valor == 11:
                _as.valor = 11
    
    def reset(self):
        if self.dinheiro_jogador > 0:
            again=input("Queres jogar outra rodada? (S ou N)")
            if again.upper() == "S":
                self.jogo()
            else:
                print("Até à próxima")
                quit()
        else:
            new = input("Gostarias de voltar a apostar? (S ou N)")
            if new.upper() == "S":
                self.montante_inicial = int(input("Montante inicial: "))
                self.jogo()
            else:
                print("Até à próxima")
                quit()


    def jogo(self):
        self.pontos_jogador = 0
        self.pontos_dealer = 0

        a = 0
        while a != 1:
            aposta = int(input("Aposta para esta rodada: "))
            if aposta <= 0:
                print("Mínimo de 1€")
            elif aposta > self.dinheiro_jogador:
                print("Não é possível apostar mais que o montante inicial")
            elif aposta >= 0:
                a = 1
        baralho = self._baralho
        jogada_jogador = []
        jogada_dealer = []
        while len(jogada_jogador) < 2:
            carta_jogador = random.choice(baralho)
            jogada_jogador.append(carta_jogador)
            baralho.remove(carta_jogador)

            if carta_jogador.carta == "A":
                self.ace(carta_jogador)

            self.pontos_jogador += carta_jogador.valor_carta

            print("Carta Jogador-> ", carta_jogador.carta, carta_jogador.naipe)
            print("Pontos do jogador: ", self.pontos_jogador)

            input()

            carta_dealer = random.choice(baralho)
            jogada_dealer.append(carta_dealer)

            if carta_dealer.carta == "A":
                carta_dealer.valor = 1

            baralho.remove(carta_dealer)
            self.pontos_dealer += carta_dealer.valor_carta

            if len(jogada_dealer) == 1:
                print("Carta Dealer ->", carta_dealer.carta, carta_dealer.naipe)
                print("Pontos do dealer: ", self.pontos_dealer)
            input()
            
        print("Pontos do dealer: ", self.pontos_dealer)
        input()
        print("Pontos do jogador: ", self.pontos_jogador)
        input()

        if self.pontos_jogador == 21:
            print("BLACKJACK!!!!")
            print("GANHASTE!!!!")
            self.dinheiro_jogador = aposta * 2.5
            print("Montante:", self.dinheiro_jogador)
            self.reset()
            
        while self.pontos_jogador < 21:
            escolha = input("Hit or Stand (escolher H ou S)")
                
            if escolha.upper() == 'H':
                carta_jogador = random.choice(baralho)
                jogada_jogador.append(carta_jogador)
                baralho.remove(carta_jogador)

                if carta_jogador.carta == "A":
                    self.ace(carta_jogador)

                self.pontos_jogador += carta_jogador.valor_carta

                print("Carta Jogador-> ", carta_jogador.carta, carta_jogador.naipe)

                print("Pontos do jogador: ", self.pontos_jogador)
                input()
            
            if escolha.upper() == 'S':
                break
        
        if self.pontos_jogador == 21:
            print("BLACKJACK!!!!")
            print("GANHASTE!!!!")
            self.dinheiro_jogador = aposta * 2.5
            print("Montante:", self.dinheiro_jogador)
            self.reset()
        
        if self.pontos_jogador > 21:
            print("BUSTED!!! >PERDESTE!!!")
            self.dinheiro_jogador -= aposta
            print("Montante atual:", self.dinheiro_jogador)
            self.reset()
        
        input()

        while self.pontos_dealer < 17:
            carta_dealer = random.choice(baralho)
            jogada_dealer.append(carta_dealer)

            if carta_dealer.carta == "A":
                carta_dealer.valor = 1

            baralho.remove(carta_dealer)
            self.pontos_dealer += carta_dealer.valor_carta

            print("Carta Dealer ->", carta_dealer.carta, carta_dealer.naipe)
            input()

            print("Pontos do dealer: ", self.pontos_dealer)
            input()

        if self.pontos_dealer > 21:
            print("DEALER BUSTED!!! GANHASTE !!!")
            self.dinheiro_jogador = aposta * 2
            print("Montante atual:", self.dinheiro_jogador)
            self.reset()
        
        if self.pontos_dealer == 21:
            print("DEALER TÊM BLACKJACK!! PERDESTE -_-")
            self.dinheiro_jogador -= aposta
            print("Montante atual:", self.dinheiro_jogador)
            quit()
        
        if self.pontos_dealer == self.pontos_jogador:
            print("JOGO EMPATADO!!")
            print("Montante:", self.dinheiro_jogador)
            self.reset()

        if self.pontos_dealer < self.pontos_jogador:
            print("PARABÉNS!! GANHASTE!!")
            self.dinheiro_jogador += aposta * 2
            print("Montante atual:", self.dinheiro_jogador)
            self.reset()

        else:
            print("PERDESTE!! melhor sorte para a próxima '_'")
            self.dinheiro_jogador -= aposta
            print("Montante atual:", self.dinheiro_jogador)
            self.reset()
    

        






        

baralho = []
naipes = ["Copas", "Ouros", "Paus", "Espadas"]
cartas = ["A", "K", "J", "Q", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
valor_cartas = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

for naipe in naipes:
    for carta in cartas:
        baralho.append(Carta(naipe, carta, valor_cartas[carta]))
    


aa = Jogo(baralho)
aa.jogo()



        
    
        

        
        





