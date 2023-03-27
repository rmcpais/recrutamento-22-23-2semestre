from Deck import deck
import random

# Funções


# Variaveis
gameover = False
round_counter = 0
N_players = 2  # user 2 é o dealer
deck = deck()
y1 = 0  # n precisas de inicializar variaveis, especialmente se lhes vais dar nomes estilo batalha naval
y2 = 0
cards = []
# podes usar _ como nome de variável nestes casos, _ atira a variável para o lixo
N_cards = [0 for i in range(N_players)]
score = [0 for i in range(N_players)]

# cheira-me que nao precisas de pre alocar estas listas, podes so fazer append de um player novo quando precisares
# C Habits die hard
User = [None for i in range(N_players)]
As = [0 for i in range(N_players)]
In_deck = 52               # Nº cartas ainda no deck
for i in range(N_players):
    cards.append([])


# Get info
User[0] = input("Insira o seu username? ")
Money_inicial = 0
while Money_inicial <= 0:
    Money_inicial = int(
        input("Bem vindo " + User[0] + "!!! \nQual o valor que pretendes apostar? "))
User[N_players-1] = "Dealer"
# Tenta usar um try, except block para guarantires que a conversão acontece
Money = int(Money_inicial)


# game
while not gameover:

    # inicio da ronda
    round_counter += 1
    end_of_round = 0
    print("------------------------------------------------------\n                       Round " +
          str(round_counter) + ":\n------------------------------------------------------")  # podes usar f-strings e dividir isto em varios strings
    print("\n* Dealer - " + User[0] + " o teu Saldo é " + str(Money) + "$\n")
    round_bet = 0
    while round_bet <= 0:
        round_bet = int(
            input("* " + User[0] + " quando queres apostar nesta ronda? "))
    Money -= round_bet
    for x in range(N_players):
        score[x] = 0
        As[x] = 0
        N_cards[x] = 0

    for x in range(4):
        for y in range(13):
            deck.cards[x][y] = 0

    # atribuiçao de cartas iniciais
    y = 0
    for x in range(N_players):
        cards[x].append([])
        for u in range(2):  # u é usado para???? sera que podia ser _, ou uma alternativa melhor
            y = 0
            # trying to make it so cards aren't repeats??
            # maybe there's a better way to go about doing this
            # like keeping a list with only the cards that our card is "not in" that list somehow
            while y == 0:
                y1 = random.randint(0, 3)
                y2 = random.randint(0, 12)
                # this if statement is very ugly
                if deck.cards[y1][y2] != 0:
                    y = 0
                else:
                    y = 1
                # maybe we can replace it with this
                # y = 0 if deck.cards[y1][y2] != 0 else 1
            deck.cards[y1][y2] = x+1

            if 0 < y2 < 10:
                score[x] += y2+1
            elif y2 == 0:
                As[x] += 1
            else:
                score[x] += 10

            cards[x][round_counter-1].append((y1, y2))
            N_cards[x] += 1

    for x in range(N_players):
        print("\n" + User[x] + " as tuas cartas são:")
        l = 2
        if x == N_players-1:
            l = 1
        for y in range(l):
            (y1, y2) = cards[x][round_counter - 1][y]
            print("* " + deck.Card_translator(y1, y2))

    for x in range(N_players-1):

        # escolha do valor dos as
        # E suposto o valor dos As ser sempre o que beneficia mais o jogador a quem eles pertencem
        if As[x] > 0:
            for y in range(As[x]):
                g = 0
                while g != 11 and g != 1:
                    g = int(input("\n* Dealer - " + User[x] + " tens um As, o teu score atual é " + str(
                        score[x]) + ", qual o valor que lhe pretendes atribuir? 1 ou 11?"))

                score[x] += g

        # blackjack inicial
        if score[x] == 21 and score[N_players-1] != 21: #score[N_players-1] é igual a score[-1], -1 acede ao ultimo elemento da lista
            print("\n* Dealer - " +
                  User[x] + " Blackjack!!! Parabéns!!! ganhaste " + str(2.5 * round_bet) + "$")
            Money += 2.5 * round_bet

        # pedir cartas
        more_cards = 1
        while more_cards == 1:

            more_cards = int(
                input("\n* Dealer - " + User[x] + " queres mais cartas? (1 se Sim e 0 se Não)"))
            if more_cards == 0:
                continue

            # nova carta
            #oh look duplicate code, if only there was something that you can put duplicate code and run it from different places
            # maybe something where we ask for nova_carta() and it gives us one
            y = 0
            while y == 0: 
                y1 = random.randint(0, 3)
                y2 = random.randint(0, 12)
                if deck.cards[y1][y2] != 0:
                    y = 0
                else:
                    y = 1
            deck.cards[y1][y2] = x + 1
            # DEJA VU, i have read this code before, higher on the file and i know there's a place to go
            if 0 < y2 < 10:
                score[x] += y2 + 1
            elif y2 == 0:
                As[x] += 1
            else:
                score[x] += 10

            cards[x][round_counter - 1].append((y1, y2))

            N_cards[x] += 1

            print("\n" + User[x] + " as tuas cartas são:")
            for y in range(N_cards[x]):
                (y1, y2) = cards[x][round_counter - 1][y]
                print("* " + deck.Card_translator(y1, y2))

            # verificar se deu bust

            if score[x] > 21 and As[x] > 0:
                score[x] = 0
                for y in range(N_cards[x]):
                    (y1, y2) = cards[x][round_counter - 1][y]
                    if y2 == 0:
                        continue
                    # All around me are familiar faces
                    if 0 < y2 < 10:
                        score[x] += y2 + 1
                    elif y2 == 0:
                        As[x] += 1
                    else:
                        score[x] += 10

                for y in range(As[x]):
                    g = 0
                    while g != 11 and g != 1:
                        g = int(input(
                            "\n* Dealer - " + User[x] + " Bust!!! tens um As, podes reatribuir um valor a ele, qual o valor que lhe pretendes atribuir? 1 ou 11?"))
                    score[x] += g

            if score[x] > 21:
                print("\n* Dealer - " +
                      User[x] + " Bust!!! perdeste " + str(round_bet) + "$")
                end_of_round = 1
                break

            # verificar se é blackjack

            if score[x] == 21:
                print(
                    "*\nDealer - " + User[x] + " Blackjack!!! Parabéns!!! ganhaste " + str(2.5 * round_bet) + "$")
                Money += 2.5 * round_bet
                end_of_round = 1
                break

    if end_of_round == 1:
        if Money <= 0:
            New_bet = int(input(
                "\n* Dealer - " + User[x] + " Não tens saldo queres apostar mais? Qual o valor que queres apostar?"))
            if New_bet < 1:
                gameover = True
            Money += New_bet
            continue

        New_bet = int(
            input("\n* Dealer - " + User[x] + " Queres aumentar o teu saldo? Qual o valor que queres apostar?"))
        Money += New_bet
        more = int(input("\n* Dealer - " +
                   User[x] + " queres jogar mais uma ronda? (1 para Sim e 0 para Não)"))
        if more == 0:
            gameover = True

        continue

    # dealer revela a sua 2º carta

    print("\n*Dealer - As Minhas cartas são:")
    for y in range(N_cards[N_players-1]):
        (y1, y2) = cards[N_players-1][round_counter - 1][y]
        print("* " + deck.Card_translator(y1, y2))

    if As[N_players - 1] > 0:
        for y in range(As[N_players - 1]):
            if score[N_players - 1] + 11 > 21:
                score[N_players - 1] += 1
            else:
                score[N_players - 1] += 11

    # Dealer precisa de mais cartas

    while score[N_players - 1] < 17:
        eas = 0
        # https://www.youtube.com/watch?v=CduA0TULnow
        y = 0
        while y == 0:
            y1 = random.randint(0, 3)
            y2 = random.randint(0, 12)
            if deck.cards[y1][y2] != 0:
                y = 0
            else:
                y = 1
        deck.cards[y1][y2] = N_players - 1 + 1

        if 0 < y2 < 10:
            score[N_players - 1] += y2 + 1
        elif y2 == 0:
            As[N_players - 1] += 1
            eas = 1
        else:
            score[N_players - 1] += 10

        cards[N_players - 1][round_counter - 1].append((y1, y2))

        N_cards[N_players - 1] += 1

        print("\n" + User[N_players - 1] + " as tuas cartas são:")
        for y in range(N_cards[N_players - 1]):
            (y1, y2) = cards[N_players - 1][round_counter - 1][y]
            print("* " + deck.Card_translator(y1, y2))

        if eas == 1:
            for y in range(As[N_players - 1]):
                if score[N_players - 1] + 11 > 21:
                    score[N_players - 1] += 1
                else:
                    score[N_players - 1] += 11

        if As[N_players-1] > 0 and score[N_players-1] == 21:
            score[N_players-1] = 0

            for y in range(N_cards[N_players-1]):
                (y1, y2) = cards[N_players-1][round_counter - 1][y]
                if y2 == 0:
                    continue
                if 0 < y2 < 10:
                    score[N_players-1] += y2 + 1
                elif y2 == 0:
                    As[N_players-1] += 1
                else:
                    score[N_players-1] += 10

            for y in range(As[N_players-1]):
                if score[N_players-1] > 21:
                    break
                else:
                    score[N_players - 1] += 1

    for x in range(N_players-1):
        if score[N_players-1] > 21:
            print("* Dealer - " +
                  User[x] + " Dealer Bust!!! ganhaste " + str(2 * round_bet) + "$")
            Money += 2 * round_bet

        elif score[N_players-1] < score[x]:
            print("* Dealer - " +
                  User[x] + " Blackjack!!! ganhaste " + str(2*round_bet) + "$")
            Money += 2 * round_bet

        else:
            print("* Dealer - " + User[x] +
                  " perdeste " + str(round_bet) + "$ !!!")

    if Money <= 0:
        New_bet = int(input(
            "\n* Dealer - " + User[x] + " Não tens saldo queres apostar mais? Qual o valor que queres apostar?"))
        if New_bet < 1:
            gameover = True
        Money += New_bet
        continue

    more = int(input("\n* Dealer - " +
               User[x] + " queres jogar mais uma ronda? (1 para Sim e 0 para Não)"))
    if more == 0:
        gameover = True
    New_bet = int(input("\n* Dealer - " +
                  User[x] + " Queres aumentar o teu saldo? Qual o valor que queres apostar?"))
    Money += New_bet

print("\n------------------------------------------------------")
net = Money - int(Money_inicial)
if net > 0:
    print("\n* Dealer - Parabéns !!! Ganhaste " + str(net) + "$")
elif net < 0:
    print("\n* Dealer - Mais sorte para a proxima !!! perdeste " + str(abs(net)) + "$")
else:
    print("\n* Dealer - Sais com o mesmo que entraste")

print("* Dealer - " + User[0] + " obrigado por jogares! Volta sempre")

# Can i get some funtions pwease?
#   👀
#  👉👈
