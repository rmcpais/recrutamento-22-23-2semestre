from time import sleep
class Jogador:
    """
    A classe jogador representa uma instância (jogador) que possui um montante no banco, um conjunto de cartas(baralho),
    um score de blackjack, uma aposta colocada, e uma vontade definitivamente não influenciada pelas garras tiranas,
    totalitárias e greedy dos Casinos Solverde
    """
    def __init__(omeuprimocarlos):
        """
        Construtor da classe jogador
        """
        omeuprimocarlos.montante = 0
        omeuprimocarlos.baralho = []
        omeuprimocarlos.blackjack_score = 0
        omeuprimocarlos.bet = 0
        omeuprimocarlos.suits_dict = {"Hearts": "♡",
                                       "Diamonds": "♢",
                                       "Spades": "♤",
                                       "Clubs": "♧"}


    def get_montante(omeuprimocarlos) -> float:
        """
        Getter do montante de uma instância de jogador
        :return: float que representa o montante no banco do jogador
        """
        return omeuprimocarlos.montante

    def change_montante(omeuprimocarlos, amount: float or int) -> None:
        """
        Setter do montante de uma instância de jogador
        :param amount: int ou float de quantidade de dinheiro a ser removido ou adicionado ao montante
        :return: None
        """
        omeuprimocarlos.montante += amount

    def get_baralho(omeuprimocarlos) -> list:
        """
        Getter do conjunto de cartas de uma instância de jogador
        :return: list do baralho do jogador
        """
        return omeuprimocarlos.baralho

    def add_baralho(omeuprimocarlos, carta: str) -> None:
        """
        Adiciona ao grupo de cartas de uma instância de jogador uma nova carta
        :param carta: string da carta a ser adicionada no baralho do jogador
        :return: None
        """
        omeuprimocarlos.baralho.append(carta)

    def reset_baralho(omeuprimocarlos) -> None:
        """
        Reseta o baralho dos jogadores para cada nova jogada
        :return: None
        """
        omeuprimocarlos.baralho = []

    def get_score(omeuprimocarlos) -> int:
        """
        Getter do score de blackjack duma instância de jogador
        :return: int que representa o score de blackjack do jogador
        """
        return omeuprimocarlos.blackjack_score

    def calcular_score(omeuprimocarlos) -> None:
        """
        Calculadora de scores para instâncias de jogadores
        :return: None
        """
        for card in omeuprimocarlos.baralho:
            # Se carta for um digito e nao face, somo o digito
            if card.split(" ")[0].isdigit():
                omeuprimocarlos.blackjack_score += int(card.split(" ")[0])
            # Se for face, pode ser Ás (1 ou 11) ou um 10
            else:
                if card.split(" ")[0] == "Ace":
                    score_escolhido = int(input("Calhou-te um Ás! Qual o valor que lhe dás (1 ou 11)? "))
                    while score_escolhido != 1 and score_escolhido != 11:
                        score_escolhido = int(input("O valor do Ás pode ser 1 ou 11! Não aldrabes! "))
                    omeuprimocarlos.blackjack_score += score_escolhido
                else:
                    omeuprimocarlos.blackjack_score += 10

    def limpa_score(omeuprimocarlos) -> None:
        """
        Reseta o blackjack score de uma instância de jogador
        :return: None
        """
        omeuprimocarlos.blackjack_score = 0

    def get_bet(omeuprimocarlos) -> int or float:
        """
        Getter da aposta colocada por uma instância de jogador
        :return: int or float da aposta
        """
        return omeuprimocarlos.bet

    def set_bet(omeuprimocarlos, new_bet: int or float) -> None:
        """
        Setter de uma nova aposta a ser colocada por uma instância de jogador
        :param new_bet: int or float da nova aposta
        :return: None
        """
        omeuprimocarlos.bet = new_bet

    def stringue(omeuprimocarlos):
        """
        Pseudo - Overriding do método str (estava a dar none type error nao me julguem)
        :return: str
        """
        print("Tirando as cartas"); sleep(0.5); print("."); sleep(0.5); print("."); sleep(0.5); print(".");sleep(0.5)
        print(f'------// ------ O TEU BARALHO ------ // ------')
        for card in omeuprimocarlos.baralho:
            if card.split(" ")[0].isdigit():
                print(f'┌────────────┐\n'
                      f'│{card.split(" ")[0]}           │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│     {omeuprimocarlos.suits_dict[card.split(" ")[2]]}      │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│      {card.split(" ")[0]}     │\n'
                      f'└────────────┚')
            else:
                print(f'┌────────────┐\n'
                      f'│{card.split(" ")[0]}        │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│     {omeuprimocarlos.suits_dict[card.split(" ")[2]]}      │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│   {card.split(" ")[0]}     │\n'
                      f'└────────────┚')
            sleep(1)
        res = ""
        for card in omeuprimocarlos.baralho:
            res += " | " + card
        return res + " |"


class Dealer(Jogador):

    def calcular_score(omeuprimocarlos) -> None:
        """
        Calculadora de scores para instâncias de dealers (override)
        :return: None
        """
        for card in omeuprimocarlos.baralho:
            # Se carta for um digito e nao face, somo o digito
            if card.split(" ")[0].isdigit():
                omeuprimocarlos.blackjack_score += int(card.split(" ")[0])

            # Se for face, pode ser Ás (1 ou 11) ou um 10
            else:
                if card.split(" ")[0] == "Ace":
                    if omeuprimocarlos.get_score() < 11:
                        omeuprimocarlos.blackjack_score += 11
                    else:
                        omeuprimocarlos.blackjack_score += 1
                else:
                    omeuprimocarlos.blackjack_score += 10

    def stringue(omeuprimocarlos):
        """
        Pseudo - Overriding do método str (estava a dar none type error nao me julguem)
        :return: str
        """
        sleep(0.5);print(".");sleep(0.5);print(".");sleep(0.5);print(".");sleep(0.5) #screw pylint
        print(f'------// ------ BARALHO DO DEALER ------ // ------')
        for card in omeuprimocarlos.baralho:
            if card.split(" ")[0].isdigit():
                print(f'┌────────────┐\n'
                      f'│{card.split(" ")[0]}           │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│     {omeuprimocarlos.suits_dict[card.split(" ")[2]]}      │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│         {card.split(" ")[0]}  │\n'
                      f'└────────────┚')
            else:
                print(f'┌────────────┐\n'
                      f'│{card.split(" ")[0]}        │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│     {omeuprimocarlos.suits_dict[card.split(" ")[2]]}      │\n'
                      f'│            │\n'
                      f'│            │\n'
                      f'│   {card.split(" ")[0]}     │\n'
                      f'└────────────┚')
            sleep(1)
        res = ""
        for card in omeuprimocarlos.baralho:
            res += " | " + card
        return res + " |"
