from time import sleep
from .classes.characters import jorge as p1, cammila as p2, goblin
from .classes.abilities import *
from .classes.combat import combat
from .classes.dados import *
# PYTHONPATH=src python -m projeto_dnd.teste

def main():
    while True:
        """sleep(2)
        if p2.hp_atual > 0:
            p2.ataque_magico(goblin)

        if goblin.hp_atual == 0:
            print(f'{goblin.nome} morreu!')
            break

        sleep(2)
        if p1.hp_atual > 0:
            p1.ataque_fisico(goblin)

        if goblin.hp_atual == 0:
            print(f'{goblin.nome} morreu!')
            break

        acao = d2(1)
        sleep(2)
        if acao == 1:
            goblin.ataque_fisico(p1)
        else:
            goblin.ataque_fisico(p2)

        sleep(1)
        print(f'{p2.nome} está com ({p2.hp_atual}/{p2.hp_max})PVs')
        sleep(1)
        print(f'{p1.nome} está com ({p1.hp_atual}/{p1.hp_max})PVs')
        sleep(1)
        print(f'{goblin.nome} está com ({goblin.hp_atual}/{goblin.hp_max})PVs')
"""
        combat([p1, p2], [goblin])

if __name__ == '__main__':
    main()

