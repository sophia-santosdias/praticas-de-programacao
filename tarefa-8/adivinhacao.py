# EXERCÍCIO: Implementar um sistema de adivinhação de números entre 1 e 1023.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import random

def usuarioTenta():
    comp = random.randint(1, 1023)
    cont = 0
    while True:
        tentativa = int(input('Qual o número? '))
        cont += 1
        if comp < tentativa:
            print('-1')
        elif comp > tentativa:
            print('1')
        else:
            print('0')
            break
        
    print(f'\nNúmero de tentativas: {cont}')
    print(f'Número certo: {comp}')

def termoMedio(i, f):
    meio = ((f - i) // 2) + i
    return meio 

def compTenta():
    i = 1
    f = 1023
    tenta = 0
    while True:
        comp = termoMedio(i, f)
        tenta += 1
        print(f'Computador: {comp}')
        resp = int(input('O seu número é maior(1), menor (-1) ou igual(0)? '))
        if resp == 1:
            i = comp
        elif resp == -1:
            f = comp
        else:
            break
    print(f'\nNúmero de tentativas: {tenta}')
    print(f'Número certo: {comp}')

quem = int(input('Quem vai adivinhar (usuario=0, computador=1)? '))

if quem == 0:
    usuarioTenta()
else:
    compTenta()











































