import random
import time

# SE O JOGADOR DER ALL IN O JOGO BREKA E FICA SEM DINHEIRO 
# # atualizar jogo e fica com 0 de balance
#-....................
# melhorar eficiencia 

class Sistema:
    def __init__(self):
        self.baralho = ["C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                        "D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                        "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA",
                        "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA"]
        self.player = Player()
        self.dealer = Player()

        self.mesa = [self.player.hand, self.dealer.hand]

    def getCardStrPreview(self,cardCode):
        naipe = cardCode[0]
        if naipe == "C": naipe = '♣'
        elif naipe == "D": naipe = '♦'
        elif naipe == "H": naipe = '♥'
        elif naipe == "S": naipe = '♠'

        numChar1 = cardCode[1]
        numChar2 = ' '
        if numChar1 == '1': numChar2 = '0'
        
        cardList = ['┌─────────┐',
                    f'│{numChar1}{numChar2}       │',
                    '│         │',
                    '│         │',
                    f'│    {naipe}    │',
                    '│         │',
                    '│         │',
                    f'│       {numChar1}{numChar2}│',
                    '└─────────┘']

        return cardList

    def stringCardsPreview(self,cardCodeList):
        cardsListPreview = []
        finalStrPreview = ""
        for cardCode in cardCodeList: cardsListPreview.append(self.getCardStrPreview(cardCode))
        for l in range(0,len(cardsListPreview[0])):
            line = ""
            for cardPreview in cardsListPreview:
                line += "  " + str(cardPreview[l])
            finalStrPreview += line + "\n"

        return finalStrPreview


    def print_mesa(self,revealLastDealerCard=True):
        if revealLastDealerCard == False:
            print("DEALER:")
            print(self.stringCardsPreview(self.dealer.playerHand()[:-1])) #  + " ? "
            # APRIMORAR A FUNCOA PARA METER CARTA ESCONDIDA COM PONTOS DE INTERROGACAO OU CARTA COM NAIPE E NUM??

            if str(self.dealer.playerHand()[0])[1:] == "A":
                print("1 / 11")
            else:
                if str(self.dealer.playerHand()[-1])[1:] == "A":
                    print(self.dealer.playerSum()[0]-1)
                elif str(self.dealer.playerHand()[-1])[1:] in ["Q","J","K"]:
                    print(self.dealer.playerSum()[0]-10)
                else:
                    print(self.dealer.playerSum()[0]-int(str(self.dealer.playerHand()[-1])[1:]))
        else:
            print("DEALER:")
            print(self.stringCardsPreview(self.dealer.playerHand()))
            if self.dealer.playerSum()[0] != self.dealer.playerSum()[1]:
                print(str(self.dealer.playerSum()[0]) + "/" + str(self.dealer.playerSum()[1]))
            else: 
                print(self.dealer.playerSum()[0])
        print("\n")
        print("JOGADOR:")
        print(self.stringCardsPreview(self.player.playerHand()))
        if self.player.playerSum()[0] != self.player.playerSum()[1]:
            print(str(self.player.playerSum()[0]) + "/" + str(self.player.playerSum()[1]))
        else: 
            print(self.player.sum[0])
        print("SALDO: " + str(self.player.playerBalance()) + " $")
        print("--------------------------------------------------------------------------------------------\n")

    def retirar_carta_baralho(self):
        carta = str(random.choice(self.baralho))
        self.baralho.remove(carta)
        return carta

    def isPush(self):
        if (self.dealer.sum[0] == 21 or self.dealer.sum[1] == 21) and (self.player.sum[0] == 21 or self.player.sum[1] == 21):
            return True
        else: return False


    def push(self, player, playerbet): # empate, player e dealer com mao abaixo de 22
        print("PUSH")
        player.darBalance(float(playerbet))

    def player_win(self, player, playerbet, blackjack=False):
        if blackjack:
            print("| PLAYER GANHOU COM BLACKJACK |")
            player.darBalance(float(playerbet) * 2.5)
        else:
            print("| PLAYER GANHOU |")
            player.darBalance(float(playerbet) * 2)


    def player_loss(self, player, playerbet, ):
        print("| PLAYER LOSS |")


    def resetCards(self):
        self.baralho = ["C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                        "D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                        "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA",
                        "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA"]

        self.player.hand, self.dealer.hand = [],[]

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False


    def comecar_jogo(self):
        keepGoing = True
        
        x = input("Qual o teu balance inicial? ")
        while not self.isfloat(x):
            x = input("Insere o teu balance inicial $: ")
        self.player.darBalance(x)

        while keepGoing == True:
            if self.player.balance == 0:
                print("Esgotou o balance")
                keepGoing = False
                break
            bet = input("Quanto queres apostar? ")
            while not self.isfloat(bet) or (round(self.player.playerBalance() - float(bet),2) < 0):
                bet = input("Quanto queres apostar? ")
            self.player.retirarBalance(bet)

            self.resetCards()

            self.player.darCarta(self.retirar_carta_baralho())
            self.player.darCarta(self.retirar_carta_baralho())
            self.dealer.darCarta(self.retirar_carta_baralho())
            self.dealer.darCarta(self.retirar_carta_baralho())

            self.print_mesa(revealLastDealerCard=False)
            x = input("DECISAO: ")
            while x != "hit" and x != "stand":
                x = input("DECISAO: ")
            
            if x == "hit":
                while x != "stand" and self.player.sum[1] < 22:
                    # dar carta
                    self.player.darCarta(self.retirar_carta_baralho())
                    self.print_mesa(revealLastDealerCard=False)

                    if self.player.isPlayerBusted():
                        self.player_loss(self.player, bet)
                        break
                    elif self.player.sum[1] == self.player.sum[0] == 21 :
                        x = "stand"
                        break
                    x = input("DECISAO: ")
                else:
                    x = "stand"
            if x == "stand":
                self.print_mesa() # virar carta do dealer

                while self.dealer.sum[1] < 17 and not self.dealer.isPlayerBusted(): # or (self.dealer.sum[1] < self.player.sum[1])
                    time.sleep(2)
                    self.dealer.darCarta(self.retirar_carta_baralho())
                    self.print_mesa()

                if self.dealer.isPlayerBusted():
                    self.player_win(self.player, bet,blackjack=self.player.hasPlayerBlackjack())
                elif self.dealer.sum[1] > self.player.sum[1]:
                    self.player_loss(self.player, bet)
                elif self.dealer.sum[1] == self.player.sum[1]:
                    self.push(self.player, bet)
                elif self.dealer.sum[1] > self.player.sum[1]:
                    self.player_loss(self.player, bet)
                elif self.dealer.sum[1] < self.player.sum[1]:
                    self.player_win(self.player, bet)
                else:
                    raise ValueError("Nao foi possivel concluir o estado do jogo")
            
            # depois de jogo ter acabado
            print("SALDO: " + str(self.player.playerBalance()) + " $")
            keepGoing = input("Queres continuar? s/n\n") == 's'
            
        print("JOGO ACABOU")

            


class Player:
    def __init__(self):
        self.hand = []
        self.sum = []
        self.balance = 0


    def retirarBalance(self, num):
        self.balance -= round(float(num),2)

    def darBalance(self, num):
        self.balance += round(float(num),2)

    def playerBalance(self):
        return round(float(self.balance),2)

    def darCarta(self, carta):
        self.hand.append(carta)
        self.sum = self.getSumOfHand(self.hand)

    #Funcao auxiliar
    def playerHand(self):
        return self.hand


    #Funcao auxiliar
    def playerSum(self):
        return self.sum


    #Funcao auxiliar
    def hasPlayerBlackjack(self):
        try:
            return self.sum[1] == 21 and len(self.hand) == 2
        except:
            return False
        

    #Funcao auxiliar
    def isPlayerBusted(self):
        return self.sum[0] > 21
    
    # Funcao auxiliar    
    def getSumOfHand(self, hand):
        sum = [0,0]

        #if self.hasPlayerBlackjack():
            #return [12,21]
        
        #if len(hand) == 2 and hand[0][1:] == hand[1][1:] == 'A': # caso especifico de mao ter 2 ases
            #time.sleep(100)
            #return [2,22]

        for card in hand:
            if card[1:] in ['Q','J','K']:
                #sum = list(map(lambda x: x + 10, sum))
                sum = [sum[0] + 10, sum[1] + 10]
            elif card[1:] == 'A':
                if sum[1] + 11 > 21:
                    sum = [sum[0] + 1, sum[1] + 1] # se houver 2 ases, dá 1/12
                else:
                    sum = [sum[0] + 1, sum[1] + 11]

            else:
                #sum = list(map(lambda x: x + int(card[1:]), sum))
                sum = [sum[0] + int(card[1:]), sum[1] + int(card[1:])]

        if sum[1] > 21: # no caso de 18/28 fica 18/18
            sum[1] = sum [0]

        return sum
        
sys = Sistema()
sys.comecar_jogo()

# MTER AO LADO DO SALDO A BET
# FAZER CHEAT CODE BAIXO CIMA QUADRADO BOLA E TEM BALANCE INFINITO