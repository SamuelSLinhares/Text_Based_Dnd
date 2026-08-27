from .dados import d20, d12, d10, d8, d6, d4, d2

'''

Habilidades são específicas demais para serem generalizadas, por isso, serão representadas por funções, quando um personagem tentar usar 
uma habilidade, será verificado se ele a possui, e então a função será executada

'''

def recuperar_folego(self):
    cura = (d10(1) + 1)
    self.hp_atual += cura
    if self.hp_atual > self.hp_max:
        self.hp_atual = self.hp_max
    print(f'{self.nome} usou Recuperar Fôlego e curou {cura}PVs ')