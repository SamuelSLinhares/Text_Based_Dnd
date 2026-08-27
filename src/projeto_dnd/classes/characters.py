from random import randint
from .dados import d20, d12, d10, d8, d6, d4, d2
from .weapons import *

#from abc import ABC, abstractmethod
"""class Character(ABC):

    Todo personagem deve ser capaz de fazer as seguintes
    ações


    @abstractmethod
    def attack(self):
        pass

    def equip_item(self):
        pass

    def use_item(self):
        pass """

"""

Todo personagem, sendo de Jogador ou CPU, deve ser um objeto da classe
Character

"""

class Character:
    def __init__(self,
                forc: int, 
                des: int, 
                con: int, 
                int: int, 
                sab: int, 
                car: int, 
                nome: str, 
                classe: str,
                hp_max: int, 
                hp_atual: int, 
                ca: int, 
                bonus_ataque_fis: int, 
                bonus_ataque_mag: int, 
                movimento: float, 
                cd: int, 
                bonus_dano: int, 
                iniciativa: int, 
                espaço_magia: dict,
                arma,
                habilidades: dict,
                truques: dict,
                magias: dict) -> None:
        self.forc = forc
        self.des = des
        self.con = con
        self.int = int
        self.sab = sab
        self.car = car
        self.nome = nome
        self.classe = classe
        self.hp_max = hp_max
        self.hp_atual = hp_atual
        self.ca = ca
        self.bonus_ataque_fis = bonus_ataque_fis
        self.bonus_ataque_mag = bonus_ataque_mag
        self.movimento = movimento
        self.cd = cd
        self.bonus_dano = bonus_dano
        self.iniciativa = iniciativa
        self.espaço_magia = espaço_magia
        self.arma = arma
        self.habilidades = habilidades
        self.truques = truques
        self.magias = magias

    def rolar_dano(self) -> int:
        return self.arma.rolar_dano() + self.bonus_dano

    def ataque_fisico(self, target) -> None:
        resultado = d20(1)
        if resultado == 20:
            dano = self.rolar_dano() * 2
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{self.nome} acertou um acerto crítico em {target.nome} e causou {dano}pontos de dano!')

        else:

            if (resultado + self.bonus_ataque_fis) >= target.ca:
                dano = self.rolar_dano()
                target.hp_atual -= dano
                if target.hp_atual < 0:
                    target.hp_atual = 0
                print(f'{self.nome} acertou {target.nome} com {self.arma.nome} e causou {dano} pontos de dano!')

            else:
                print(f'{self.nome} errou o golpe em {target.nome}!')


    def ataque_magico(self, target) -> None:
        resultado = d20(1)
        if resultado == 20:
            dano = self.rolar_dano() * 2
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{self.nome} acertou um acerto crítico em {target.nome} e causou {dano} pontos de dano!')
        
        else:
        
            if (resultado + self.bonus_ataque_mag) >= target.ca:
                dano = self.rolar_dano()
                target.hp_atual -= dano
                if target.hp_atual < 0:
                    target.hp_atual = 0
                print(f'{self.nome} acertou {target.nome} com {self.arma.nome} e causou {dano} pontos de dano!')
        
            else:
                print(f'{self.nome} errou o golpe em {target.nome}!')

class PJ(Character):
    def __init__(self,
                forc: int, 
                des: int, 
                con: int, 
                int: int, 
                sab: int, 
                car: int, 
                nome: str, 
                classe: str, 
                hp_max: int,
                hp_atual: int, 
                ca: int, 
                bonus_ataque_fis: int, 
                bonus_ataque_mag: int, 
                movimento: float, 
                cd: int, 
                bonus_dano: int, 
                iniciativa: int, 
                espaço_magia: dict,
                arma,
                habilidades: dict,
                truques: dict,
                magias: dict) -> None:
        super().__init__(forc, des, con, int, sab, car, nome, classe, hp_max, hp_atual, ca, bonus_ataque_fis, bonus_ataque_mag, movimento, cd, bonus_dano, iniciativa, espaço_magia, arma, habilidades, truques, magias)


class Ameaca(Character):
    def __init__(self,
                forc: int, 
                des: int, 
                con: int, 
                int: int, 
                sab: int, 
                car: int, 
                nome: str, 
                classe: str, 
                hp_max: int,
                hp_atual: int, 
                ca: int, 
                bonus_ataque_fis: int, 
                bonus_ataque_mag: int, 
                movimento: float, 
                cd: int, 
                bonus_dano: int, 
                iniciativa: int, 
                espaço_magia: dict,
                arma,
                habilidades: dict,
                truques: dict,
                magias: dict) -> None:
        super().__init__(forc, des, con, int, sab, car, nome, classe, hp_max, hp_atual, ca, bonus_ataque_fis, bonus_ataque_mag, movimento, cd, bonus_dano, iniciativa, espaço_magia, arma, habilidades, truques, magias)

"""

PJs e Ameaças de exemplo para testes! Adicionar objetos com valores
mais limpos posteriormente

"""


jorge = PJ(0, 0, 0, 0, 0, 0, "Jorge", "Guerreiro", 29, 29, 16, 6, 0, 6.5, 13, 4, +1, None, espada_longa, {"Recuperar Fôlego": ("Ação Bônus: Recupera 1d10+1 PVs", 2), "Golpe Especial": ("Ação: Causa o dobro de dano caso acerte", 2)}, None, None)

cammila = PJ(0, 0, 0, 0, 0, 0, "Cammila", "Mago", 23, 23, 13, 1, 5, 9.0, 16, 1, 4, {"Nível 1": 2}, toque_vampírico, None, {"Chama Sagrada": ("Acão: Caso acerte, causa 1d8 de dano radiante", 999)}, {"Infligir Ferimentos": ("Ação: Caso acerte, causa 2d10 de dano necrótico", None)})

goblin = Ameaca(0, 0, 0, 0, 0, 0, "Goblin", "Ameaça", 71, 71, 13, 4, -1, 12.0, 12, 2, 3, None, espada_longa, None, None, None)