from random import randint
from .dados import d20, d12, d10, d8, d6, d4, d2

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
                dano: int, 
                iniciativa: int, 
                espaço_magia: dict,) -> None:
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
        self.dano = dano
        self.iniciativa = iniciativa
        self.espaço_magia = espaço_magia

    def ataque_fisico(self, target) -> None:
        resultado = d20(1)
        if resultado == 20:
            dano = self.dano * 2
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{self.nome} acertou um acerto crítico em {target.nome} e causou {dano}pontos de dano!')

        else:

            if (resultado + self.bonus_ataque_fis) >= target.ca:
                dano = self.dano
                target.hp_atual -= dano
                if target.hp_atual < 0:
                    target.hp_atual = 0
                print(f'{self.nome} acertou {target.nome} e causou {dano} pontos de dano!')

            else:
                print(f'{self.nome} errou o golpe em {target.nome}!')


    def ataque_magico(self, target) -> None:
        resultado = d20(1)
        if resultado == 20:
            dano = self.dano * 2
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{self.nome} acertou um acerto crítico em {target.nome} e causou {dano} pontos de dano!')
        
        else:
        
            if (resultado + self.bonus_ataque_mag) >= target.ca:
                dano = self.dano
                target.hp_atual -= dano
                if target.hp_atual < 0:
                    target.hp_atual = 0
                print(f'{self.nome} acertou {target.nome} e causou {dano} pontos de dano!')
        
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
                dano: int, 
                iniciativa: int, 
                espaço_magia: dict,) -> None:
        super().__init__(forc, des, con, int, sab, car, nome, classe, hp_max, hp_atual, ca, bonus_ataque_fis, bonus_ataque_mag, movimento, cd, dano, iniciativa, espaço_magia)

jorge = PJ(0, 0, 0, 0, 0, 0, "Jorge", "Guerreiro", 29, 29, 16, 6, 0, 6.5, 13, d8(1) + 4, +1, 0)

cammila = PJ(0, 0, 0, 0, 0, 0, "Cammila", "Mago", 23, 23, 13, 1, 5, 9.0, 16, d4(2) + 1, 4, 2)
