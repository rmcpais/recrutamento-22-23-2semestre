from cards import cards
from pessoa import pessoa
from money import money

budget = input("Inserir valor a colocar em jogo: ")

round = 1

#Situação inicial, sem vitórias (w), ou perdas(l).
keepPlaying = True

#Inicialização dos módulos
jogador = pessoa()
dealer = pessoa()
SetofCards = cards()

while (keepPlaying) and (budget != 0):

    #Nova ronda
    bet = input("inserir valor de aposta: ")
    while int(bet) > int(budget):
        print("Impossível! A aposta deve ser menor que o dinheiro em jogo.")
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
    #Cartas do dealer
    print("Dealer's cards:")
    print(SetofCards.newCard())

    #Adicionar carta do dealer
    dealer.addCard(SetofCards.ultimoValor())
    print("★: ? of ? - Value: ?")
    
    print()

    if jogador.sum() == 21:
        print("BlackJack!")

    if SetofCards.naturalTest():
        print("Natural!")
        #Adicionar lucro do natural
        budget = budget + (2.5)*(bet)
        print("Your money: " + str(budget))

    #Hit Or Settle?
    if jogador.sum() < 21:
        settle = False
        while not settle:
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
                print()
                print("A outra carta do dealer:")
                #Mostra a carta do dealer
                print(SetofCards.newCard())

                #Adiciona-a ao conjunto do dealer
                dealer.addCard(int(SetofCards.ultimoValor()))

                #Acaba com pedidos de Hit or Settle
                settle = True

    #Jogador passou do limite
    if jogador.sum() > 21:
        print("Bust")


    if dealer.sum() < 17:
        #Aviso:
        print()
        print("O dealer tem menos de 17 pontos, recebe nova carta!")
        #Nova carta do dealer
        print(SetofCards.newCard())

        #Adiciona-a ao conjunto do dealer
        dealer.addCard(int(SetofCards.ultimoValor()))

    print()
    print("Os teus pontos: " + str(jogador.sum()))
    print("Os pontos do dealer: " + str(dealer.sum()))

    if jogador.sum() == 21:
        print("BlackJack!")
        w = True

        #Adição do dinheiro
        budget = int(budget) + (2.5)*(int(bet))

        #Atualizar valor do dinheiro
        print("Your money:" + str(budget))


    elif dealer.sum() == 21:
        print()
        #Dealer ganha com blackjack
        print("Dealer ganha com Blackjack!")

        #Atualização do dinheiro
        budget = int(budget) - int(bet)
        print("O teu dinheiro: " + str(budget))
    else:
        #Comparação da proximidade dos pontos a 21
        JogPontos = abs(21 - jogador.sum())
        DealerPontos = abs(21 - dealer.sum())

        #Se o jogador estiver mais perto:
        if JogPontos > DealerPontos:
            print("O dealer ganha!")
            budget = int(budget) - int(bet)
            print()
            print("Your Money:" + str(budget))

        elif JogPontos < DealerPontos:
            print("O jogador ganha!")
            budget = int(budget) + 2*(int(bet))
            print()
            print("Your Money:" + str(budget))

    print("End of round " + str(round) + "!")
    round = 2
    question = input("Continuar a jogar? (S/N)")
    if question == "S":
        keepPlaying = True

        #Retirar histórico de jogadas
        jogador.clear()
        dealer.clear()
        SetofCards.clear()
    else:
        keepPlaying == False

    

if (budget <= 0):
    print("Acabou o dinheiro. Não podes continuar a jogar.")

if not keepPlaying:
    print("Obrigada por jogar!")


    