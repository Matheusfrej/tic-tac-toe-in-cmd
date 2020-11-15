from random import randint
from time import sleep

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
rodada = 1


def MostrarJogo():
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] == 0:
                print('[   ]', end='')
            elif matriz[l][c] == 1:
                print('[ X ]', end='')
            elif matriz[l][c] == -1:
                print('[ O ]', end='')
            else:
                print(f'[{matriz[l][c]:^3}]', end='')
        print()


def MenuJogador():
    global rodada
    print('='*30)
    print(f'{f"Rodada {rodada}":^30}')
    print('='*30)
    rodada += 1
    print(f'Vez de {nome}:')
    while True:
        linha = int(input('Escolha a linha: '))
        coluna = int(input('Escolha a coluna: '))
        if matriz[linha-1][coluna-1] == 0:
            matriz[linha-1][coluna-1] = 1
            MostrarJogo()
            resultado = Verificar()
            if resultado != 1:
                MenuComputador()
            sleep(0.5)
            break
        else:
            print('A posição que você tentou jogar já está ocupada!')


def MenuComputador():
    print('Vez do Computador:')
    sleep(1)
    while True:
        linhapc = randint(1, 3)
        colunapc = randint(1, 3)
        if matriz[linhapc - 1][colunapc - 1] == 0:
            matriz[linhapc - 1][colunapc - 1] = -1
            MostrarJogo()
            Verificar()
            sleep(0.5)
            break


def Verificar():
    cont = 0
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] == 0:
                cont += 1
    if sum(matriz[0]) == 3 or sum(matriz[1]) == 3 or sum(matriz[2]) == 3:
        JogadorVenceu()
        return 1
    elif sum(matriz[0]) == -3 or sum(matriz[1]) == -3 or sum(matriz[2]) == -3:
        ComputadorVenceu()
        return 1
    elif matriz[0][0] + matriz[1][0] + matriz[2][0] == 3 or matriz[0][1] + matriz[1][1] + matriz[2][1] == 3 or matriz[0][2] + matriz[1][2] + matriz[2][2] == 3:
        JogadorVenceu()
        return 1
    elif matriz[0][0] + matriz[1][0] + matriz[2][0] == -3 or matriz[0][1] + matriz[1][1] + matriz[2][1] == -3 or matriz[0][2] + matriz[1][2] + matriz[2][2] == -3:
        ComputadorVenceu()
        return 1
    elif matriz[0][0] + matriz[1][1] + matriz[2][2] == 3 or matriz[0][2] + matriz[1][1] + matriz[2][0] == 3:
        JogadorVenceu()
        return 1
    elif matriz[0][0] + matriz[1][1] + matriz[2][2] == -3 or matriz[0][2] + matriz[1][1] + matriz[2][0] == -3:
        ComputadorVenceu()
        return 1
    else:
        if (matriz[0].count(0) + matriz[1].count(0) + matriz[2].count(0)) % 2 != 0:
            MenuJogador()
    if cont == 0:
        print('Deu Velha! Obrigado por jogar!')
        return 1
    cont = 0


def JogadorVenceu():
    print(f'{nome} venceu! Obrigado por jogar!')


def ComputadorVenceu():
    print('Computador venceu! Mais sorte da próxima vez.')


nome = input('Qual o seu nome? ').capitalize().strip()
MenuJogador()
