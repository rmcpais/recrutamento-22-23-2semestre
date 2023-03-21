import random

#baralho de cartas / mao do jogador

baralho = [2,3,4,5,6,7,8,9,10 , 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10,
        'J' , 'Q', 'K', 'A','J' , 'Q', 'K', 'A','J' , 'Q', 'K', 'A','J' , 'Q', 'K', 'A']
mao_jogador= []
mao_dealer = []


dinheiro = float(input("Quanto dinheiro quer entrar no jogo:\n"))

#dar cartas
def dar_cartas(mao):
    carta = random.choice(baralho)
    mao.append(carta) 


#calcular o total de cada mão
def total(mao):
    total = 0
    figuras= ['J' , 'Q', 'K']
    for carta in mao:
        if carta in range (1,11):
            total += carta
        elif carta in figuras:
            total += 10
        else:
            if total > 10:
                total +=1
            else:
                total += 11
    return total


# ver vencedor
def  dealer_mao():
    if len(mao_dealer) == 2:
        return mao_dealer[0]
    elif len(mao_dealer) > 2:
        return mao_dealer[0],mao_dealer[1]


#Se quer continuar a jogar ou não

def exit(dinheiro):
    if dinheiro <= 0:
        print("O jogo terminou pois não tem mais dinheiro!")
        return 0
    jogar_sair = float(input("1: Jogar\n2: Sair\n"))
    if jogar_sair == 2:
        print("Vemo-nos no próximo jogo tchau!!!")
        return 0
    if jogar_sair == 1:
        aposta = float(input("Quanto quere apostar:"))
    dinheiro -= aposta
    return [dinheiro, jogar_sair, aposta]

#dividir em duas maos




#loop do jogo

def blackjack(dinheiro):
    n = 0
    jogador = True
    dealer = True    
    while jogador or dealer:
        if n == 0:
            print(f"Você tem {dinheiro}$")
            x = exit(dinheiro)
            if x == 0:
                return 0
            dinheiro = x[0]
            jogar_sair = x[1]
            aposta = x[2]
            n+=1
            print(n)
        if jogar_sair ==2:
            print(f"Você sai do jogo com {dinheiro}$" )
            break
        print(f"Dealer tem {dealer_mao()} e X")
        print(f"Você tem {mao_jogador} com um total de {total(mao_jogador)}")
        if jogador:
            ficar_pedir = input("1: Ficar\n2: Pedir\n")
        if total(mao_dealer) > 16:
            dealer = False
        else: dar_cartas(mao_dealer)
        if ficar_pedir == '1' :
            jogador = False
        else:
            dar_cartas(mao_jogador)
        if total(mao_jogador)>=21:
            jogador = False 
            dealer = False
        elif total(mao_dealer) >=21:
            dealer = False
        if jogador == False and dealer == False:
            n = 0
            if total(mao_dealer) == total(mao_jogador):
                dinheiro += aposta 
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ") 
                print("Empate! Recebe o dinheiro de volta!")
                return [dinheiro, jogar_sair]
            elif total(mao_jogador) == 21:
                dinheiro += 2.5*aposta
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print(f"Blackjack! Ganhou {2.5*aposta}$!")
                return [dinheiro, jogar_sair]
            elif total(mao_dealer) ==21:
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print("Blackjack! Dealer ganhou!")
                return [dinheiro, jogar_sair]
            elif total(mao_jogador) > 21:
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print("Você ultrapassou! Dealer ganhou!")
                return [dinheiro, jogar_sair]
            elif total(mao_dealer) > 21:
                dinheiro += 2*aposta
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print(f"Dealer ultrapassou! Ganhou {2*aposta}$!")
                return [dinheiro, jogar_sair]
            elif 21 - total(mao_dealer) < 21 -total(mao_jogador):
                print(f"\n Você tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print("Dealer ganhou!")
                return [dinheiro, jogar_sair]
            elif 21 - total(mao_dealer) > 21 -total(mao_jogador):
                dinheiro += 2*aposta
                print(f"\nVocê tem {mao_jogador} com um total de {total(mao_jogador)} e o dealer tem {mao_dealer} com um total de {total(mao_dealer)} ")
                print(f"Ganhou {2*aposta}$!")
                return [dinheiro, jogar_sair]
            

play = True            
while play:
    for _ in range(2):
        dar_cartas(mao_dealer)
        dar_cartas(mao_jogador)
    x = blackjack(dinheiro)
    if x == 0:
        break
    else:
        dinheiro = x[0]
        jogar_sair = x[1]
        if jogar_sair == 2:
            play = False
        mao_jogador= []
        mao_dealer = []