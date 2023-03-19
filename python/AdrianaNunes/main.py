# Simples jogo de Blackjack

import random

class Carta:
    naipes = {"P": "Paus", 
              "O": "Ouros", 
              "E": "Espadas", 
              "C": "Copas"}
    
    valores = (False, "Ás", "2", 
               "3", "4", "5", "6", 
               "7", "8", "9", "10",
               "Valete", "Dama", "Rei")

    def __init__(self, naipe_carta: str, valor_carta: int):
        self.n = naipe_carta
        self.v = valor_carta
        
    def obter_valor(self) -> int:
        if (self.v < 11):
            return self.v
        else:
            return 10

    def __str__(self) -> str:
        return self.valores[self.v]+ " de " + self.naipes[self.n] 
        

class Baralho:
    def __init__(self):
        self.criar_cartas()
        self.num_cartas = len(self.cartas)
        
    def criar_cartas(self):
        self.cartas = []
        naipes = ('P', 'O', 'E', 'C')

        for n in naipes:                        # Paus, Ouros, Espadas, Copas
            for v in range(1, 14):              # Ás, 2, ..., 10, Valete, Dama, Rei
                self.cartas.append(Carta(n, v))
    
    def retirar_carta(self):
        n = random.randint(0, self.num_cartas-1)
        carta = self.cartas.pop(n)
        self.num_cartas -= 1
        return carta


class Jogador:
    def __init__(self):
        self.montante = self.pedir_montante_inicial()
        self.cartas = []
        self.pontos = 0
        self.aposta = 0
        self.retirar = True

    def pedir_montante_inicial(self):
        return float(input("\nQual o teu montante inicial? "))

    def acrescentar_dinheiro(self, valor):
        self.montante += valor

    def retirar_dinheiro(self, valor):
        self.montante -= valor
    
    def pedir_valor_aposta(self):
        aposta = int(input("\nVamos começar uma rodada. Qual o valor da tua aposta? "))

        while (aposta > self.montante):
            aposta = int(input("\nNão tens montante suficiente. Qual o valor da tua aposta? "))

        self.retirar_dinheiro(aposta)
        self.aposta = aposta

        return aposta
    
    def adicionar_carta(self, c):
        if (self.retirar):
            print("\n-> Tu foste buscar uma carta.")
            self.cartas.append(c)
            self.atualizar_pontos()
        else:
            print("\n-> Não foste buscar nenhuma carta.")
        
    def atualizar_pontos(self):
        pontos = 0
        num_ases = 0
        # pontuação sem ases
        for c in self.cartas:
            if (c.obter_valor() == 1):
                num_ases += 1
            else:
                pontos += c.obter_valor() 
        
        # verificar pontuação dos ases    
        if (num_ases > 0 and pontos + 11 + num_ases-1 <= 21):
            pontos += 11 + num_ases-1
            
        else:
            pontos += num_ases
            
        self.pontos = pontos
    
    def terminar_rodada(self):
        self.cartas = []
        self.pontos = 0
        self.aposta = 0
        self.retirar = True
    
    def __str__(self):
        string = "\n-- As tuas cartas --\n" 
        for c in self.cartas:
            string += '** '
            string += c.__str__() 
            string += ' **\n'
            
        return string[:-1]
    
    
class Dealer:
    def __init__(self):
        self.cartas = []
        self.pontos = 0
        self.retirar = True

    def adicionar_carta(self, c):
        if (self.retirar):
            if (self.pontos < 18):
                print("\n-> O dealer foi buscar uma carta.") 
                self.cartas.append(c)
                self.atualizar_pontos()
            else: 
                print("\n-> O dealer não foi buscar nenhuma carta.")
                self.retirar = False
        
    def atualizar_pontos(self):
        pontos = 0
        num_ases = 0
        # pontuação sem ases
        for c in self.cartas:
            if (c.obter_valor() == 1):
                num_ases += 1
            else:
                pontos += c.obter_valor() 
        
        # verificar pontuação dos ases
        if (num_ases > 0 and pontos + 11 + num_ases-1 <= 21):
            pontos += 11 + num_ases-1
            
        else:
            pontos += num_ases
            
        self.pontos = pontos
    
    def revelar_baralho(self):
        string = "\n-- Cartas que o dealer tinha --\n" 
        for c in self.cartas:
            string += '** '
            string += c.__str__() 
            string += ' **\n'
            
        return string[:-1]
        
    def __str__(self):
        string = "\n-- Cartas do dealer --\n" 
        for c in self.cartas[1:]:
            string += '** '
            string += c.__str__() 
            string += ' **\n'
        string += "** CARTA SECRETA **\n"
            
        return string[:-1]
            

class Rodada:
    def __init__(self, aposta: int, jogador: Jogador):
        self.aposta = aposta
        self.jogador = jogador
        self.dealer = Dealer()
        self.baralho = Baralho()
        self.distribuir_cartas()
        
    def distribuir_cartas(self):
        # 1 carta para cada
        self.jogador.adicionar_carta(self.baralho.retirar_carta())
        self.dealer.adicionar_carta(self.baralho.retirar_carta())
        
        # 2 cartas para cada
        self.jogador.adicionar_carta(self.baralho.retirar_carta())
        self.dealer.adicionar_carta(self.baralho.retirar_carta())
    
        print(self.dealer.__str__())
        print(self.jogador.__str__())
        
        self.verificar_pontuacoes()
        
    def verificar_pontuacoes(self):
        pontos_jogador = self.jogador.pontos
        pontos_dealer = self.dealer.pontos
        
        if (pontos_jogador == 21):
            if (pontos_dealer == 21):
                self.empate()
                self.terminar_jogo()
            else:
                self.blackjack_do_jogador()
                self.terminar_jogo()
                
        elif (pontos_jogador > 21):
            if (pontos_dealer > 21):
                self.empate()
                self.terminar_jogo()
            else:
                self.dealer_venceu()
                self.terminar_jogo()
        else:
            self.tirar_mais_cartas()
    
        
    def tirar_mais_cartas(self):
        pontos_jogador = self.jogador.pontos

        if (self.jogador.retirar):
            resposta = input("\nTens " + str(pontos_jogador) + " pontos. Desejas tirar mais cartas? (s, n): ")
            
            while (resposta not in ('S', 'N', 's', 'n')):
                resposta = input("\nNão percebi. Desejas tirar mais cartas? (s, n): ")
        else:
            resposta = 'n'
            
        if (resposta == 'S' or resposta == 's'):
            self.nova_jogada()
            
        elif (resposta == 'N' or resposta == 'n'):
            self.jogador.retirar = False
            
            if (self.dealer.retirar):
                self.nova_jogada()
            else:
                self.verificar_vencedor()

        
    def empate(self):
        print("\nHOUVE UM EMPATE. Vamos devolver-te o dinheiro que apostaste.")
        self.jogador.acrescentar_dinheiro(self.aposta)
        
    def dealer_venceu(self):
        print("\nO DEALER VENCEU.")
    
    def jogador_venceu(self):
        print("\nGANHASTE!!!")
        self.jogador.acrescentar_dinheiro(2*self.aposta)
    
    def blackjack_do_jogador(self):
        print("\nBLACKJACK!!! GANHASTE!!!")
        self.jogador.acrescentar_dinheiro(2.5*self.aposta)
        
    def nova_jogada(self):
        # tirar mais uma carta
        self.jogador.adicionar_carta(self.baralho.retirar_carta())
        self.dealer.adicionar_carta(self.baralho.retirar_carta())
        
        print(self.dealer.__str__())
        print(self.jogador.__str__())
        
        self.verificar_pontuacoes()
        
    def verificar_vencedor(self):
        pontos_jogador = self.jogador.pontos
        pontos_dealer = self.dealer.pontos
        
        if (pontos_dealer > 21):
            self.jogador_venceu()
            
        elif (pontos_jogador > pontos_dealer):
            self.jogador_venceu()
        
        elif (pontos_jogador == pontos_dealer):
            self.empate()
            
        else:
            self.dealer_venceu()
            
        self.terminar_jogo()
    
    def terminar_jogo(self):
        # verificar quem venceu
        pontos_jogador = self.jogador.pontos
        pontos_dealer = self.dealer.pontos
        
        print("\nO dealer ficou com", pontos_dealer, "pontos.")
        print(self.dealer.revelar_baralho())

        print("\nTu ficaste com", pontos_jogador, "pontos.")
        print(self.jogador.__str__())
        
        self.jogador.terminar_rodada()


def blackjack():
    print("Bem-vindo ao jogo BLACKJACK!")
    
    jogador = Jogador()

    if (jogador.montante <= 0.0):
            print("\nNão tens dinheiro. :(")
            return
    
    continuar = 1
    while (continuar):
        print("\nTens", jogador.montante, "moedas.")
        
        aposta = jogador.pedir_valor_aposta()

        Rodada(aposta, jogador)
        
        if (jogador.montante == 0):
            print("\nFicaste sem dinheiro. :(")
            break
            
        resposta = input("\nQueres continuar a jogar? (s, n): ")
        
        while (resposta not in ['S', 'N', 's', 'n']):
            resposta = input("\nNão percebi. Queres continuar a jogar? (s, n): ")
        
        if (resposta == 'S' or resposta == 's'):
            continuar = 1
        elif (resposta == 'N' or resposta == 'n'):
            continuar = 0
    
    print("\nFim do jogo!\n")
            

if __name__ == "__main__":

    blackjack()
    