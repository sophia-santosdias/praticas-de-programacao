# EXERCÍCIO 3: Ler matrícula e nota, calcular maior e menor.
# ALUNAS: Sophia Santos e Lorena Luvizotto

for i in range(1,11):
    mat = int(input(f'Digite a matrícula do Aluno {i}: '))
    nota = float(input(f'Digite a nota do Aluno {i}: '))
    print('-'*40)

    if i == 1:
        menor = nota
        matMenor = mat
        maior = nota
        matMaior = mat
    else: 
        if nota < menor:
            menor = nota
            matMenor = mat
            
        if nota > maior:
            maior = nota
            matMaior = mat
            
            
print(f'A maior nota é {maior} do aluno de matrícula {matMaior}')
print(f'A menor nota é {menor} do aluno de matrícula {matMenor}')
