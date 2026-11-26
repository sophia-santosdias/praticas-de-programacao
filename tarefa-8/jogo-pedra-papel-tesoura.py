# EXERCÍCIO: Implementar um sistema de jogo de pedra, papel e tesoura.
# ALUNAS: Sophia Santos e Lorena Luvizotto

from random import randint

print('-'*10 + ' JOGO PEDRA, PAPEL E TESOURA ' + '-'*10)

while True:
    jog = int(input('Entre com sua escolha (1-PEDRA. 2- PAPEL. 3-TESOURA: '))
    print()
    if jog in [1, 2, 3]:
        break
    else:
        print('ESCOLHA INVÁLIDA. REPITA!')
    
comp = randint(1, 3)
print(f'ESCOLHA DO COMPUTADOR: {comp}\n')

if jog == 1:
    print('USUÁRIO: PEDRA')

elif jog == 2:
    print('USUÁRIO: PAPEL')
    
elif jog == 3:
    print('USUÁRIO: TESOURA')

if comp == 1:
    print('COMPUTADOR: PEDRA')

elif comp == 2:
    print('COMPUTADOR: PAPEL')
    
elif comp == 3:
    print('COMPUTADOR: TESOURA')
    
print()  
if jog == comp:
    print('RESULTADO: EMPATE')
elif (jog == 1 and comp == 3) or (jog == 2 and comp == 1) or (jog == 3 and comp == 2):
    print('RESULTADO: USUÁRIO GANHA')
else:
    print('RESULTADO: COMPUTADOR GANHA')
