# EXERCÍCIO 2: Ler N e calcular/imprimir a soma dos N primeiros números pares.
# ALUNAS: Sophia Santos e Lorena Luvizotto

n = int(input('Digite um número: '))
i = x = soma = 0
lista = []

while i < n:
    if x % 2 == 0:
        soma += x
        lista.append(x)
        i += 1
    x += 1

print(f'A soma dos {n} primeiros pares é {soma} e eles são os números {lista}')
