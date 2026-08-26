from .dados import d20, d12, d10, d8, d6, d4, d2

class Weapon:
    def __init__(self, nome: str, dado_dano, qtd_dados: int):
        self.nome = nome
        self.dado_dano = dado_dano
        self.qtd_dados = qtd_dados

    def rolar_dano(self) -> int:
        return self.dado_dano(self.qtd_dados)

espada_longa = Weapon("Espada Longa", d8, 1)

toque_vampírico = Weapon("Toque Vampírico", d4, 2)