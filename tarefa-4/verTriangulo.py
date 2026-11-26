# EXERCÍCIO: Elaborar um programa para ler os valores de 3 lados de uma figura e verificar se, com esses valores, é possível formar um triângulo.
# ALUNA: Sophia Santos

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar triângulo')
else:
    print('Não é possível formar triângulo')

