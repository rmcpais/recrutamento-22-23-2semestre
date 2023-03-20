from cards import cards
from pessoa import pessoa

#Pedido de dinheiro a colocar em jogo
budget = input("Inserir valor a colocar em jogo: ")

#Ronda inicial
round = 1

#Situação inicial
keepPlaying = True

#Inicialização dos módulos
jogador = pessoa()
dealer = pessoa()
SetofCards = cards()

#Início do jogo
while (keepPlaying) and (budget != 0):

    #Pedido de aposta
    bet = input("inserir valor de aposta: ")

    #Verificação que aposta tem valor inferior ao dinheiro em jogo
    while int(bet) > int(budget):
        print("Impossível! A aposta deve ser menor que o dinheiro em jogo.")
        bet = input("inserir valor de aposta: ")

    #Nova ronda:
    print("-------------------------------------")
    print("Round " + str(round))
    print( )


    #Cartas do jogador
    print("Your cards:")
    i= 0
    #While loop para o processo se repetir uma vez
    while (i!=2):
        #Apresentação da carta
        print(SetofCards.newCard())

        #Adição do valor da carta ao histórico do jogador
        jogador.addCard(SetofCards.ultimoValor())

        i = i+1
    #Apresentação dos pontos:
    print("Os teus pontos: " + str(jogador.sum()))

    print()
    #Cartas do dealer
    print("Dealer's cards:")
    print(SetofCards.newCard())

    #Adicionar carta do dealer
    dealer.addCard(SetofCards.ultimoValor())
    print("★: ? of ? - Value: ?")
    
    print()

    #Verificar se jogador tem Blackjack
    if jogador.sum() == 21:
        print("BlackJack!")

    #Verificar se jogador tem blackjack natural
    if SetofCards.naturalTest():
        print("Natural!")

        #Adicionar lucro do natural
        budget = int(budget) + (2.5)*(int(bet))
        print("Your money: " + str(budget))

    #Hit Or Settle?
    if jogador.sum() < 21:
        #Variável utilizada para repetir pergunta até jogador escolher settle
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

    #Apresentação dos pontos
    print()
    print("Os teus pontos: " + str(jogador.sum()))
    print("Os pontos do dealer: " + str(dealer.sum()))

    #if statements para todos os possíveis resultados
    #Verificar se após HitorSettle o jogador tem blackjack
    if jogador.sum() == 21:
        print("BlackJack!")

        #Adição do dinheiro
        budget = int(budget) + (2.5)*(int(bet))

        #Atualizar valor do dinheiro
        print("Your money:" + str(budget))

    #Verificar se o dealer tem blackjack
    elif dealer.sum() == 21:
        print()
        #Dealer ganha com blackjack
        print("Dealer ganha com Blackjack!")

        #Atualização do dinheiro
        budget = int(budget) - int(bet)
        print("O teu dinheiro: " + str(budget))

    #Nenhum tem blackjack:
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

    #Fim da ronda
    print("End of round " + str(round) + "!")
    round = round + 1

    #Continuar ou não a jogar
    question = input("Continuar a jogar? (S/N)")

    #Sim
    if question == "S":
        keepPlaying = True

        #Retirar histórico de jogadas
        jogador.clear()
        dealer.clear()
        SetofCards.clear()
    #Não
    elif question == "N":
        keepPlaying = False
        
print()
if (budget <= 0):
    print("Acabou o dinheiro. Não podes continuar a jogar.")

if not keepPlaying:
    print("Obrigada por jogar!")

print("Dinheiro final: " + str(budget))


    