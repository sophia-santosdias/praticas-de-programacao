# EXERCÍCIO: Implementar um jogo da forca.
# ALUNAS: Sophia Santos e Lorena Luvizotto

p = input('Digite a palavra secreta: ')
traco = list('-'*len(p))


c = len(p)
while c > 0:
    print('Palavra: ', end='')
    for j in traco:
        print(j, end='')
      
    
    letra = input('\nDigite uma letra: ')
    if letra in p:
        print('CERTO!')
        for i, l in enumerate(p):
            if letra == l:
                traco[i] = l
    else:
        print('ERROU!')
    if '-' not in traco:
        print(f'\nPARABÉNS!!! Palavra certa: {p}')
        break
    c = c - 1
    print(f'\nTentativas restantes: {c}')
    
if c == 0:
    print(f'\nFIM DAS TENTATIVAS! Palavra certa: {p}')














































