class Deck:
    """
    A classe Deck representa instâncias de baralhos de cartas descritos pelos atributos de suits, faces,
    e o baralho que resulta da combinação das primeiras duas, formando o baralho standard de 52 cartas.
    """
    def __init__(omeuprimoarmando):
        """
        Construtor da classe Deck
        """
        omeuprimoarmando.suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        omeuprimoarmando.faces = ["Ace", "Jack", "King", "Queen"] + [str(i) for i in range(2, 11)]
        omeuprimoarmando.baralho = [f'{face} of {suit}'
                                    for suit in omeuprimoarmando.suits
                                    for face in omeuprimoarmando.faces]



    def get_baralho(omeuprimoarmando) -> list:
        """
        Getter do baralho de uma instância de Deck
        :return: list do baralho
        """
        return omeuprimoarmando.baralho

    def remove_baralho(omeuprimoarmando, card: str) -> None:
        """
        Remove do baralho duma instância de Deck uma carta
        :param card: string da carta a ser removida
        :return: None
        """
        omeuprimoarmando.baralho.remove(card)

    def __len__(omeuprimoarmando) -> int:
        """
        Overriding do len method para uma len(instance_de_deck) devolver a length do seu baralho
        :return: int da length do baralho da instance de Deck
        """
        return len(omeuprimoarmando.baralho)

