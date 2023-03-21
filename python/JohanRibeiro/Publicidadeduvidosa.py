import random


class Scam(object):
    """
    Provavelmente a melhor classe que já verás. Penso que esta descrição basta
    """
    def __init__(self):
        self.publicidades = ["LUÍS FIGO PERDE TUDO!!!", "MULHERES DIVORCIADAS A 50 METROS DE SI!!",
                             "INTERNSHIP NA NASA PARA INICIANTES!!!",
                             "MENINAS ESCOTEIRAS A VENDER BOLACHAS A 50 METROS DE SI!!",
                             "PEDRO REIS SANTOS É PRESO POR TRÁFICO DE ALGORITMOS",
                             "PRÍNCIPE NIGERIANO PEDE A SUA AJUDA!!",
                             "SUPER SECRET KRABBY PATTY FORMULA LEAKED!!",
                             "JUNTE-SE À BETCLICK POR 50€ GRÁTIS!!"]

    def deploy_sponsor(self):

        n = random.randint(0, len(self.publicidades)-1)
        print(f"E PARA O PATROCÍNIO DESTA RONDA:\n"
              f"{self.publicidades[n]}\n")


