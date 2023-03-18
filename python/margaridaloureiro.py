import random
simb =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
naipe =['Espadas','Corações','Ouros','Paus']
class Blackjack:
    def __init__(self, din):
        self.din = din
        self.jog = 0
        self.dealer = 0
        self.valor = 0
        self.saiu = []
        self.aposta = 0
        self.vencedor = True
        self.continuar = True
    def inicio(self):
        self.jog = 0
        self.dealer = 0
        self.valor = 0
        self.saiu = []
        self.aposta = 0
        self.vencedor = True
        self.continuar = True
    def auxcartas(self):
        naiperand = random.choice(naipe)
        simbrand = random.choice(simb)
        carta = [naiperand, simbrand]
        if carta not in self.saiu:
            self.saiu.append(carta)
            if simbrand in 'KQJ':
                self.valor = 10
            elif simbrand in '23456789' or simbrand == '10':
                self.valor = int(simbrand)
            else:
                self.valor = 11
        else:
            Blackjack.auxcartas(self)
    def jogador(self):
        Blackjack.auxcartas(self)
        print('A tua carta é',self.saiu[-1])
        if self.valor == 11:
            self.valor = int(input('Saiu um ÁS! Queres que valha como 1 ou 11? '))
        self.jog += self.valor
        self.valor = 0
    def dealercartas(self):
        Blackjack.auxcartas(self)
        if self.valor == 11:
            if (self.dealer + 11) > 21:
                self.valor = 1
        self.dealer += self.valor
        self.valor = 0
        if len(self.saiu) != 4:
            print('A carta do dealer é',self.saiu[-1])
        else:
            print('A segunda carta do dealer foi retirada')
    def maiscartas(self):
        mais = str(input('Queres mais uma carta? (Responde apenas S ou N) '))
        if mais == 'S':
            Blackjack.jogador(self)
        else:
            self.continuar = False
    def final(self):
        if self.vencedor:
            self.din += self.aposta
            print('Ganhaste! Agora tens', self.din)
            again = str(input('Queres continuar a jogar? (Responde apenas S ou N) '))
            if again == 'S':
                Blackjack.inicio(self)
                Blackjack.jogada(self)
            else:
                print('Adeus')
        elif self.vencedor == 'nada':
            print('Empate! Agora tens', self.din)
            again = str(input('Queres continuar a jogar? (Responde apenas S ou N) '))
            if again == 'S':
                Blackjack.inicio(self)
                Blackjack.jogada(self)
            else:
                print('Adeus')
        else:
            self.din -= self.aposta
            if self.din <= 0:
                print('Perdeste! O teu montante inicial chegou a 0. Volta noutro dia.')
            else:
                print('Perdeste! Agora tens', self.din)
                again = str(input('Queres continuar a jogar? (Responde apenas S ou N) '))
                if again == 'S':
                    Blackjack.inicio(self)
                    Blackjack.jogada(self)
                else:
                    print('Adeus')
    def jogada(self):
        if not self.saiu:
            print('Vamos começar!')
            num = int(input('Quanto queres apostar? '))
            if num <= self.din:
                self.aposta = num
                Blackjack.jogador(self)
                Blackjack.dealercartas(self)
                Blackjack.jogador(self)
                if self.jog == 21:
                    self.din += self.aposta*1.5
                    print('BLACKJACK! Agora tens', self.din)
                    again = str(input('Queres continuar a jogar? (Responde apenas S ou N) '))
                    if again == 'S':
                        Blackjack.inicio(self)
                        Blackjack.jogada(self)
                    else:
                        print('Adeus')
                else:
                    Blackjack.dealercartas(self)
                    Blackjack.jogada(self)
            else:
                print('Não tens essa quantia!')
        else:
            while self.jog < 21 and self.continuar:
                Blackjack.maiscartas(self)
            if self.jog > 21:
                self.vencedor = False
                Blackjack.final(self)
            else:
                print('A segunda carta do dealer é: ', self.saiu[3])
                while self.dealer < 17:
                    Blackjack.dealercartas(self)
                if self.dealer > 21:
                    Blackjack.final(self)
                elif self.jog < self.dealer:
                    self.vencedor = False
                    Blackjack.final(self)
                else:
                    self.vencedor = 'nada'
                    Blackjack.final(self)

dinheiro = int(input('Montante inicial: '))
x = Blackjack(dinheiro)
x.jogada()
