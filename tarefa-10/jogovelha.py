# EXERCÍCIO: Implementar um jogo da velha.
# ALUNAS: Sophia Santos e Lorena Luvizotto

matriz = [['[ ]', '[ ]','[ ]'], ['[ ]', '[ ]','[ ]'], ['[ ]', '[ ]','[ ]']]

def verificaVit(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
        
    for c in range(0, 3):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] == jogador:
            return True
        
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == jogador or matriz[2][0] == matriz[1][1] == matriz[0][2] == jogador:
        return True
    
    return False

def verificaEmp(tabuleiro):
    for linha in tabuleiro:
        if '[ ]' in linha:
            return False
    return True


jogadorAtual = '[X]'
    
while True:
    # Mostra tabuleiro
    for l in matriz:
        for e in l:
            print(e, end='  ')
        print()
        print()
    
    print(f'Vez do Jogador {jogadorAtual}')
    
    linha = int(input('Digite linha da jogada (0 a 2): '))
    coluna = int(input('Digite coluna da jogada (0 a 2): '))
    print()
    
    if matriz[linha][coluna] == '[ ]':            
        matriz[linha][coluna] = jogadorAtual
    else:
        print('Espaço ocupado! Tente novamente!')
        continue
    
    if verificaVit(matriz, jogadorAtual):
        print()
        print(f'Jogador {jogadorAtual} venceu!!')
        break
    
    if verificaEmp(matriz):
        print()
        print('Empate!!')
        break
    
    if jogadorAtual == '[X]':
        jogadorAtual = '[O]'
    else: 
        jogadorAtual = '[X]'
    
print()
for l in matriz:
    for e in l:
        print(e, end='  ')
    print()
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    