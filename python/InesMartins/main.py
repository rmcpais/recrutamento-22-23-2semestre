from cards import cards
from pessoa import pessoa


budget = input("Inserir valor a colocar em jogo: ")

round = 1

#Situação inicial, sem vitórias (w), ou perdas(l).
w = False
l = False

#Inicialização dos módulos
jogador = pessoa()
dealer = pessoa()
SetofCards = cards()

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
        jogador.addCard(int(SetofCards.ultimoValor()))
        i = i+1
    print(jogador.seeCards())

    print()
    print("Dealer's cards:")
    print(SetofCards.newCard())
    dealer.addCard(int(SetofCards.ultimoValor()))
    print("★: ? of ? - Value: ?")
    
    print(jogador.sum())

    hitOrSettle = input("Hit(H) or Settle(S)? (H/S)")
    