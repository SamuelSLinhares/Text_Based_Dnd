from .dados import d20, d12, d10, d8, d6, d4, d2
from .characters import *
'''

Habilidades são específicas demais para serem generalizadas, por isso, serão representadas por funções, quando um personagem tentar usar 
uma habilidade, será verificado se ele a possui, e então a função será executada

'''

def recuperar_folego(character, target, acoes):
    cura = (d10(1) + 1)
    target.hp_atual += cura
    if target.hp_atual > target.hp_max:
        target.hp_atual = target.hp_max
    print(f'{character.nome} usou Recuperar Fôlego e curou {cura}PVs ')
    acoes.remove("AB")

def golpe_especial(character, target, acoes):
    dano = character.rolar_dano()
    resultado = d20(1)
    if resultado == 20:
        dano = character.rolar_dano() * 4
        target.hp_atual -= dano
        if target.hp_atual < 0:
            target.hp_atual = 0
        print(f'{character.nome} acertou um acerto crítico em {target.nome} e causou {dano}pontos de dano!')
    
    else:
    
        if (resultado + character.bonus_ataque_fis) >= target.ca:
            dano = character.rolar_dano() * 2
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{character.nome} acertou {target.nome} com {character.arma.nome} e causou {dano} pontos de dano!')
    
        else:
            print(f'{character.nome} errou o golpe em {target.nome}!')
    acoes.remove("A")

#Permite a consulta em combat.py pelo nome exibido em str
ability_registry = {
    "Recuperar Fôlego": (recuperar_folego, "self", "AB"),
    "Golpe Especial": (golpe_especial, "inimigo", "A")
}

all_abilities = set(ability_registry.values())