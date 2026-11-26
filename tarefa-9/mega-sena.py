# EXERCÍCIO: Implementar um sistema de jogo da mega sena.
# ALUNAS: Sophia Santos e Lorena Luvizotto

from random import randint

jogos = []
jogo = []
for j in range(1, 11):
    cont = 1    
    while cont <= 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    jogos.append(sorted(jogo))
    jogo.clear()

i = 1
gaba = []
while i <= 6:
    num = int(input('Número certo: '))
    if (num not in gaba) and 1 <= num <= 60:
        gaba.append(num)
        i +=1
    else:
        print('Repita! Número repetido ou fora do intervalo!')
        
        
gaba = sorted(gaba)
print(f'\nGABARITO: {gaba}')


for ind, j in enumerate(jogos):
    acerto = 0
    for idx, a in enumerate(j):
        if a in gaba:
            acerto +=1
    
    print(f'Jogo {ind + 1}: {j} - Acertos: {acerto}')
    
    