from .dados import d20, d2
from .characters import PJ, Ameaca
from time import sleep
from os import name

def combat(pjs: list, ameacas: list):
    iniciativas = []
    for pj in pjs:
        iniciativa = (d20(1) + pj.iniciativa)
        iniciativas.append((iniciativa, pj))

    for ameaca in ameacas:
        iniciativa = (d20(1) + ameaca.iniciativa)
        iniciativas.append((iniciativa, ameaca))

    iniciativas.sort(key=lambda item: item[0], reverse=True)

    while True:
        personagem = iniciativas[0][1]
        print(f'Turno de {personagem.nome}!')
        sleep(1)
        if isinstance(personagem, PJ):
            mostrar_acoes(personagem, ameacas)
            iniciativas.append(iniciativas.pop(0))
        
        ###LINHA TEMPORÁRIA PARA TESTE
        else:
            pass
            iniciativas.append(iniciativas.pop(0))

def mostrar_acoes(character, ameacas: list):
    print("1. Atacar")
    if character.habilidades != None:
        print("2. Usar Habilidade")
    if character.truques != None:
        print("3. Usar Truque")
    if character.magias != None:
        print("4. Usar Magia")

    try:
        acao = int(input("O que você deseja fazer? "))
    except:
        print("Input Inválido, tente novamente")
        sleep(1)
        mostrar_acoes(character, ameacas)
    else:
        if acao == 1:
            sleep(1)
            for i, ameaca in enumerate(ameacas, start=1):
                print(f'{i}. {ameaca.nome}')

            try:
                escolha = int(input("Qual inimigo você deseja atacar? "))
                if not 1 <= escolha <= len(ameacas):
                    raise ValueError
            except ValueError:
                print("Inimigo inválido.")
                return

            personagem_alvo = ameacas[escolha - 1]
            character.ataque_fisico(personagem_alvo)
                