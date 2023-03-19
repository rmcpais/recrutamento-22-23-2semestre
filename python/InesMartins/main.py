from cards import cards
from pessoa import pessoa
from money import money


budget = input("Inserir valor a colocar em jogo: ")

round = 1

#Situação inicial, sem vitórias (w), ou perdas(l).
w = False
l = False

#Inicialização dos módulos
jogador = pessoa()
dealer = pessoa()
SetofCards = cards()
bank = money()

while (not w) and (not l) and (budget != 0):

    #Nova ronda
    bet = input("inserir valor de aposta: ")
    print("-------------------------------------")
    print("Round " + str(round))
    print( )

    i= 0
    print("Your cards:")
    while (i!=2):
        print(SetofCards.newCard())
        jogador.addCard(SetofCards.ultimoValor())
        i = i+1
    print("Os teus pontos: " + str(jogador.sum()))

    print()
    print("Dealer's cards:")
    print(SetofCards.newCard())
    dealer.addCard(int(SetofCards.ultimoValor()))
    print("★: ? of ? - Value: ?")
    
    print()

    if jogador.wChecker():
        print("BlackJack!")
        w = True
    #Hit Or Settle?
    elif jogador.sum() < 21:
        HitOrSettle = input("Hit(H) or Settle(S)? (H/S)")

        #Hit
        if HitOrSettle == "H":
            #Nova carta para o jogador
            print(SetofCards.newCard())

            #Adição do valor da nova carta ao conjunto do jogador
            jogador.addCard(int(SetofCards.ultimoValor()))

            #Atualização dos pontos
            print("Os teus pontos: " + str(jogador.sum()))
        
        #Settle
        else:
            #Mostra a carta do dealer
            print(SetofCards.newCard())
            #Adiciona-a ao conjunto do dealer
            dealer.addCard(int(SetofCards.ultimoValor()))
    #Jogador passou do limite
    else:
        print("Bust!")

    if dealer.sum() < 17:
        #Nova carta do dealer
        print(SetofCards.newCard())
        #Adiciona-a ao conjunto do dealer
        dealer.addCard(int(SetofCards.ultimoValor()))


    print("Os teus pontos: " + str(jogador.sum()))
    print("Os pontos do dealer: " + str(dealer.sum()))

    