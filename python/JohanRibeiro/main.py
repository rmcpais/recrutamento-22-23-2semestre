import random
from Jogador import *
from Deck import *
import esqueleto
from Publicidadeduvidosa import Scam
import os
from time import sleep
print("|---------//---------- BEM-VINDO AO CASINO SOLVERDE!!!! ----------//----------|\n"
      "|   PRETENDE JOGAR BLACKJACK? VAMOS JOGAR BLACKJACK. VOCÊ ADORARÁ BLACKJACK!  |")
print("|BLACKJACK É O MELHOR JOGO DO UNIVERSO!!!! BLACKJACK!! BLACKJACK!! BLACKJACK!!|\n"
      "|_____________________________________________________________________________|\n")

# Inicializo jogador, deck, ronda, publicidades e montante
jogador = Jogador()
dealer = Dealer()
deckzao = Deck()
scam = Scam()
ronda = 1
esqueleto.set_montante(jogador)

# Continuar a jogar até o montante ser 0
while jogador.get_montante() > 0:

    # Shuffle do baralho para maximizar randomness
    random.shuffle(deckzao.get_baralho())

    print(f"--------//----- RONDA {ronda} | MONTANTE: {jogador.get_montante()} -----//-------- ")
    scam.deploy_sponsor()
    esqueleto.starting_game_inator(jogador, dealer, deckzao)
    if jogador.get_montante() <= 0:
        break
    play_again = input("Queres continuar a jogar?? SÓ PODES PERDER 100% DOS"
                       " TEU DINHEIRO MAS GANHAR INFINITOS %!!! (Y/N)")
    print("\n\n")
    jogador.reset_baralho()
    dealer.reset_baralho()
    ronda += 1
    if play_again.lower() != "y":
        break

    os.system('cls' if os.name == 'nt' else 'clear')
print(f"JOGASTE {ronda} RONDA(S).\n"
      f"--------//----- GAME OVER -----//-------- ")




