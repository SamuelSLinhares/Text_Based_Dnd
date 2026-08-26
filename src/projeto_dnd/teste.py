from time import sleep
from .classes.characters import jorge as p1, cammila as p2

# PYTHONPATH=src python -m projeto_dnd.teste

def main():
    while True:
        sleep(2)
        p2.ataque_magico(p1)

        if p1.hp_atual == 0:
            print(f'{p1.nome} morreu!')
            break

        sleep(2)
        p1.ataque_fisico(p2)

        if p2.hp_atual == 0:
            print(f'{p2.nome} morreu!')
            break

        sleep(1)
        print(f'{p2.nome} está com ({p2.hp_atual}/{p2.hp_max})PVs')
        sleep(1)
        print(f'{p1.nome} está com ({p1.hp_atual}/{p1.hp_max})PVs')

if __name__ == '__main__':
    main()

