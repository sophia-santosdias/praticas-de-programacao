# EXERCÍCIO: Elabore um programa para gerar a tabuada de 1 a 10.
# ALUNA: Sophia Santos

for i in range(1,11):
    print(f'TABUADA DO {i}')
    for p in range(1,11):
        print(f'{i} X {p} = {i*p}')
