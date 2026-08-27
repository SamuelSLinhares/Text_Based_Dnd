from .dados import d20, d12, d10, d8, d6, d4, d2
from .characters import *

def infligir_ferimentos(character, target, acoes):
    resultado = d20(1)
    if resultado == 20:
        dano = d10(2) * 2
        target.hp_atual -= dano
        if target.hp_atual < 0:
            target.hp_atual = 0
        print(f'{character.nome} acertou um acerto crítico em {target.nome} e causou {dano} pontos de dano!')
        
    else:
        
        if (resultado + character.bonus_ataque_fis) >= target.ca:
            dano = d10(2) 
            target.hp_atual -= dano
            if target.hp_atual < 0:
                target.hp_atual = 0
            print(f'{target.nome} foi atingido por energia necrótica e recebeu {dano} pontos de dano!')
        
        else:
            print(f'{target.nome} desviou da magia!')
    acoes.remove("A")
    character.espaço_magia["Nível 1"] -= 1

spells_registry = {
    "Infligir Ferimentos": (infligir_ferimentos, "inimigo", "A")
}