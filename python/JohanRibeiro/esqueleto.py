from Jogador import *
import random
from Jogador import *
from Deck import *
from time import sleep

def set_montante(jogador):
    montante = input("Quanto dinheiro é que tem no banco?? ")
    while not montante.isdigit() or float(montante) <= 0:
        montante = input("Isso é impossível, coloca um valor válido: ")
    jogador.change_montante(float(montante))


def set_bet(jogador):
    bet = int(input("Quanto é que quer apostar nesta ronda? "))
    while bet > jogador.get_montante():
        bet = int(input("Não tens dinheiro suficiente para apostar isso tudo!! Aposta todo o teu montante ;) "))
    jogador.bet = bet
    jogador.change_montante(-bet)


def tira_carta_inator(deck, player):
    card = deck.get_baralho()[random.randint(0, len(deck)-1)]
    player.add_baralho(card)
    deck.remove_baralho(card)


def end_game_inator(player, dealer, deck):
    """
    End game: momento a partir do qual o dealer dá flip à sua segunda carta
    :param player: jogador
    :param dealer: dealer
    :param deck: baralho
    :return: none
    """

    # Dealer dá flip à segunda carta dele, e recalculo score
    print(f'O dealer revela a sua carta final: um {dealer.get_baralho()[1]}, '
          f'para além do {dealer.get_baralho()[0]} que ele tinha.')

    dealer.limpa_score()
    dealer.calcular_score()
    # Se o seu score, for inferior a 17, ele tira uma nova carta
    if dealer.get_score() < 17:
        print(f'O score do dealer é {dealer.get_score()}, menor que 17. Ele vai tirar outra carta.')
        print("."); sleep(1); print("."); sleep(1); print("."); sleep(1) #sigam me no yt para mais dicas de beleza de código!!

        tira_carta_inator(deck, dealer)
        print(f'O dealer tirou um {dealer.get_baralho()[2]}!')
        dealer.limpa_score()
        dealer.calcular_score()
        # Se após retirar a carta o dealer der bust ;) ele perde, e o jogador ganha 2x a sua aposta
        if dealer.get_score() > 21:
            print(f'O baralho do dealer agora é {dealer.stringue()}.\n'
                  f'Ele tem um score de {dealer.get_score()} - DEALER BUSTED!!!\n')
            player.change_montante(2*player.get_bet())
            print(f'Ganhaste {player.get_bet()} € da tua aposta!!'
                  f'Tens agora {player.get_montante()} € no banco!! JOGA MAIS!!!\n ')

    # Se o dealer não foi busted
    if dealer.get_score() <= 21:
        print(f'O score do dealer é {dealer.get_score()}, com o seu baralho: {dealer.stringue()}\n')
        # Se o score do jogador for maior que o do dealer, o jogador ganha 2x a sua aposta
        if player.get_score() > dealer.get_score():
            player.change_montante(2*player.get_bet())
            print(f'A tua mão tem um score de {player.get_score()}, maior que o score da mão do dealer!!\n'
                  f'Ganhaste {player.get_bet()} € da tua aposta!!'
                  f'Tens agora {player.get_montante()} € no banco!! JOGA MAIS!!!\n')

        # Se o score do jogador não for maior que o do dealer, o jogador perde a sua aposta :(
        else:
            print(f'A tua mão tem um score de {player.get_score()}, não maior ao score da mão do dealer!!\n'
                  f'Perdeste a tua aposta de {player.get_bet()} € :( . '
                  f'Tens agora {player.get_montante()} € no banco!!\n\n'
                  f'NÃO DESANIMES!! DE ACORDO COM A SOLVERDE INC. 90% DOS GAMBLERS '
                  f'PARAM DE JOGAR ANTES DE ATINGIREM O JACKPOT!!!!!!!')
    dealer.limpa_score()


def hit_or_not_inator(player, dealer, deck):
    """
    Mid-game: momento a partir do qual o jogador pode dar hit até o momento que decide dar stay ou perde
    :param player: jogador
    :param dealer: dealer
    :param deck: baralho
    :return: none
    """

    # Verifico se o jogador quer tirar outra carta
    hit_or_not = input("Queres tirar outra carta do baralho? Se sim, escreve 'hit', se não\
 escreve qualquer outra coisa - ")
    player.limpa_score()
    player.calcular_score()
    # Enquanto a resposta for sim, limpo o score do jogador, adiciono-lhe uma carta, e recalculo o score
    while hit_or_not == "hit":

        player.limpa_score()
        card = deck.get_baralho()[random.randint(0, len(deck)-1)]
        player.add_baralho(card)
        deck.remove_baralho(card)
        player.calcular_score()

        print(f'O teu novo baralho: {player.stringue()}\n')
        sleep(1)
        # Se o seu score exceder 21, ele é busted e perde a aposta
        if player.get_score() > 21:
            print(f"BUSTED!!!!!!O TEU SCORE EXCEDEU 21 ({player.get_score()})"
                  f"\nPerdeste a tua aposta de {player.get_bet()} €. "
                  f"Neste momento tens {player.get_montante()} € no banco")
            break

        # Se o seu score for 21 e o do dealer não, ele ganha a aposta
        if player.get_score() == 21 and dealer.get_score() != 21:
            player.change_montante(2*player.bet)
            print(f'O teu score atingiu 21!! Ganhaste {player.get_bet()} € !!! '
                  f'Neste momento tens {player.get_montante()} € no banco!')
            break


        # Repito input até o jogador não querer o hit
        hit_or_not = input("Queres tirar outra carta do baralho? Se sim, escreve 'hit', se não\
 escreve qualquer outra coisa - ")
        print("\n")
    # Quando o jogador parar o hit por vontade própria, executo o endgame.
    if player.get_score() < 21:
        end_game_inator(player, dealer, deck)


def starting_game_inator(player, dealer, deck):
    """
    Early-game : setup das apostas do jogador, do tirar das cartas, e verificação se alguém ganha por blackjack. Se
    não, continuamos pro mid-game
    :param player: jogador
    :param dealer: dealer
    :param deck: baralho
    :return: none
    """
    # Começo por definir aposta
    set_bet(player)

    # 1º carta do jogador
    tira_carta_inator(deck, player)

    # 1º carta do dealer
    tira_carta_inator(deck, dealer)

    # 2º carta do jogador
    tira_carta_inator(deck, player)
    player.calcular_score()

    # 2º carta do dealer
    tira_carta_inator(deck, dealer)
    dealer.calcular_score()

    print(f'O teu baralho: {player.stringue()}')

    # Se o jogador ganhar por blackjack
    if player.get_score() == 21:
        player.change_montante(2.5 * player.get_bet())
        player.set_bet(0)
        print(f" NATURAL!!!! GANHASTE POR BLACKJACK!!! FICASTE AGORA COM {player.get_montante()} € NO BANCO!")

    # Se o dealer ganhar por blackjack
    if player.get_score() != 21 and dealer.get_score() == 21:
        player.set_bet(0)
        print(f" NATURAL!!!! O DEALER GANHOU POR NATURAL COM O SEU BARALHO: {dealer.stringue()}!!!\n "
              f"FICASTE AGORA COM {player.get_montante()} € NO BANCO!"
              f"ACONTECE, MAIS VALE JOGAR OUTRA RONDA PARA RECUPERAR O DINHEIRO PERDIDO!")

    # Se ninguém ganhar por blackjack (hit or stay)
    if player.get_score() != 21 and dealer.get_score() != 21:
        print("A carta do dealer que está virada para cima: ", dealer.get_baralho()[0], "\n")
        sleep(2)
        hit_or_not_inator(player, dealer, deck)
