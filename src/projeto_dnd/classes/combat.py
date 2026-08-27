from .abilities import recuperar_folego
from .dados import d20, d2
from .characters import PJ, Ameaca
from time import sleep
import os

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
        os.system("cls" if os.name == "nt" else "clear")
        print("----------------------------------------")
        print(f'Turno de {personagem.nome}!')
        sleep(1)
        if isinstance(personagem, PJ):
            acoes = ["A", "AB"]
            mostrar_acoes(personagem, ameacas, acoes)
            iniciativas.append(iniciativas.pop(0))
        
        ###LINHA TEMPORÁRIA PARA TESTE
        else:
            pass
            iniciativas.append(iniciativas.pop(0))

def mostrar_acoes(character, ameacas: list, acoes: list):
    print(f"Você tem: {acoes}")
    print("1. Atacar")
    if character.habilidades != None:
        print("2. Usar Habilidade")
    if character.truques != None:
        print("3. Usar Truque")
    if character.magias != None:
        print("4. Usar Magia")
    print("5. Encerrar Turno")

    try:
        acao = int(input("O que você deseja fazer? "))
    except:
        print("Input Inválido, tente novamente")
        sleep(1)
        mostrar_acoes(character, ameacas)
    else:
        if acao == 1:
            print("----------------------")
            print("Inimigos Disponíveis:")
            for i, ameaca in enumerate(ameacas, start=1):
                print(f'{i}. {ameaca.nome}')

            try:
                escolha = int(input("Qual inimigo você deseja atacar? "))
                if not 1 <= escolha <= len(ameacas):
                    raise ValueError
            except ValueError:
                print("Inimigo inválido.")
                return

            sleep(1)
            personagem_alvo = ameacas[escolha - 1]
            character.ataque_fisico(personagem_alvo)
            acoes.remove("A")
            if acoes:
                sleep(1)
                mostrar_acoes(character, ameacas, acoes)

        elif acao == 2:
            sleep(1)
            print("Suas habilidades:")
            for i, (nome, (descricao, usos)) in enumerate(character.habilidades.items(), start=1):
                print(f'{i}. {nome}: {descricao} ({usos} Usos)')
            """
            Execucao de teste
            """
            recuperar_folego(character, acoes)
            sleep(5)


            """
            Criar função para procurar a habilidade pelo nome, e executar a função específica

            Adicionar a opção de não executar nenhuma ação e retornar ao mostrar_acoes()

            Programar funcao e opção semelhante para truques e magias
            """


        elif acao == 5:
            pass