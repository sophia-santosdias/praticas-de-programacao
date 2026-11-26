# EXERCÍCIO: Escreva um programa que simule uma calculadora eletrônica.
# ALUNA: Sophia Santos

resp = 's'

while resp == 's':
    print(f'CALCULADORA ELETRÔNICA')
    a = int(input('Digite o primeiro Operando: '))
    b = int(input('Digite o segundo Operando: '))
    oper = input('Digite o Operador (+, -, *, /, ^ ou %): ')

    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    elif oper == '*':
        result = a * b
    elif oper == '/':
        result = a / b
    elif oper == '^':
        result = a ** b
    elif oper == '%':
        result = a % b

    print(f'{a} {oper} {b} = {result}')

    resp = input('Deseja realizar outra operação? (s/n) ')
    
    





    
