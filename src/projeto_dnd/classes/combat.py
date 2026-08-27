from .spells import *
from .cantrips import *
from .abilities import *
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
    if "A" in acoes:
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
    except ValueError:
        print("Input Inválido, tente novamente")
        sleep(1)
        mostrar_acoes(character, ameacas, acoes)
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
            try:
                escolha = int(input("Qual habilidade deseja usar? (0 para voltar) "))
                if escolha == 0:
                    mostrar_acoes(character, ameacas, acoes)
                    return
                nome, (descricao, usos) = list(character.habilidades.items())[escolha - 1]
            except (ValueError, IndexError):
                print("Habilidade inválida.")
                return

            habilidade = buscar_habilidade(nome)
            if habilidade is None:
                print("Essa habilidade ainda não está implementada.")
                return
            if usos <= 0:
                print("Você não tem usos disponíveis para essa habilidade.")
                return

            if not executar_acao(habilidade, character, ameacas, acoes):
                return
            character.habilidades[nome] = (descricao, usos - 1)
            if acoes:
                mostrar_acoes(character, ameacas, acoes)
            sleep(1)

        elif acao == 3:
            sleep(1)
            print("Seus truques:")
            for i, (nome, (descricao, usos)) in enumerate(character.truques.items(), start=1):
                print(f'{i}. {nome}: {descricao}')
            try:
                escolha = int(input("Qual truque deseja usar? (0 para voltar) "))
                if escolha == 0:
                    mostrar_acoes(character, ameacas, acoes)
                    return
                nome, (descricao, usos) = list(character.truques.items())[escolha - 1]
            except (ValueError, IndexError):
                print("Truque inválido.")
                return

            truque = buscar_truque(nome)
            if truque is None:
                print("Esse truque ainda não está implementada.")
                return

            executar_acao(truque, character, ameacas, acoes)
    
            if acoes:
                mostrar_acoes(character, ameacas, acoes)
            sleep(1)

        elif acao == 4:
            sleep(1)
            print("Suas magias:")
            for i, (nome, (descricao, usos)) in enumerate(character.magias.items(), start=1):
                print(f'{i}. {nome}: {descricao}')
            try:
                escolha = int(input("Qual magia deseja usar? (0 para voltar) "))
                if escolha == 0:
                    mostrar_acoes(character, ameacas, acoes)
                    return
                nome, (descricao, usos) = list(character.magias.items())[escolha - 1]
            except (ValueError, IndexError):
                print("Magia inválida.")
                return
            
            magia = buscar_magia(nome)
            if magia is None:
                print("Essa magia ainda não está implementada.")
                return
            
            if character.espaço_magia.get("Nível 1") >= 1:
                executar_acao(magia, character, ameacas, acoes)

            else:
                print("Você não tem espaços de magia suficientes para conjurar!")
            if acoes:
                mostrar_acoes(character, ameacas, acoes)
            sleep(1)

        elif acao == 5:
            pass

def buscar_habilidade(nome):
    return ability_registry.get(nome)

def buscar_truque(nome):
    return cantrip_registry.get(nome)

def buscar_magia(nome):
    return spells_registry.get(nome)

def executar_acao(acao, character, ameacas: list, acoes: list):
    funcao, tipo_alvo, acao_necessaria = acao
    if acao_necessaria not in acoes:
        print("Você não tem recursos o suficiente para realizar essa ação!")
        return False
    if tipo_alvo == "self":
        alvo = character
    elif tipo_alvo == "inimigo":
        alvo = selecionar_inimigo(ameacas)
        if alvo is None:
            return False
    elif tipo_alvo == "nenhum":
        alvo = None
    else:
        print("Tipo de alvo inválido.")
        return False

    funcao(character, alvo, acoes)
    return True

def selecionar_inimigo(ameacas: list):
    print("Inimigos Disponíveis:")
    for i, ameaca in enumerate(ameacas, start=1):
        print(f'{i}. {ameaca.nome}')

    try:
        escolha = int(input("Qual inimigo deseja selecionar? "))
        if not 1 <= escolha <= len(ameacas):
            raise ValueError
    except ValueError:
        print("Inimigo inválido.")
        return None

    return ameacas[escolha - 1]