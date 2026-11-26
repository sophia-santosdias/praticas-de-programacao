# EXERCÍCIO: Fazer um programa para indicar o número mínimo de notas a serem fornecidas por um caixa eletrônico. 
# As notas disponíveis no caixa são: 100, 50, 20, 10, 5.
# ALUNA: Sophia Santos

valor = int(input('Digite um valor: '))

n100 = valor // 100
r100 = valor % 100
n50 = r100 // 50
r50 = r100 % 50
n20 = r50 // 20
r20 = r50 % 20
n10 = r20 // 10
r10 = r20 % 10
n5 = r10 // 5

print(f'O caixa vai disponibilizar {n100} notas de R$ 100,00')
print(f'O caixa vai disponibilizar {n50} notas de R$ 50,00')
print(f'O caixa vai disponibilizar {n20} notas de R$ 20,00')
print(f'O caixa vai disponibilizar {n10} notas de R$ 10,00')
print(f'O caixa vai disponibilizar {n5} notas de R$ 5,00')
