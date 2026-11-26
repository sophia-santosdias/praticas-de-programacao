# EXERCÍCIO: Elaborar um programa para validar um CPF, verificando se é válido ou inválido.
# ALUNAS: Sophia Santos e Lorena Luvizotto

resp = 'sim'

def ValidaCPF(cpf):
    soma1 = soma2 = 0
    if len(cpf) != 11:
        return 'CPF INVÁLIDO'

    for i, v in enumerate(cpf):
        if cpf[1] == cpf[i]:
            if i == len(cpf) - 1:
                return 'CPF INVÁLIDO'
            else:
                continue
        else:
            break

    for i, v in enumerate(cpf[0:9]):
        valor = int(v) * (10-i)
        soma1 += valor
    n = soma1 % 11
    if n < 2:
        dv1 = 0
    else:
        dv1 = 11 - n

    for i, v in enumerate(cpf[0:10]):
        valor = int(v) * (11-i)
        soma2 += valor
    n = soma2 % 11
    if n < 2:
        dv2 = 0
    else:
        dv2 = 11 - n

    if dv1 != int(cpf[9]) or dv2 != int(cpf[10]):
        return 'CPF INVÁLIDO'
    else:
        return 'CPF VÁLIDO'

while resp == 'sim':
    cpf = input('Digite um CPF: ')
    print(ValidaCPF(cpf))
    resp = input('Quer continuar digitando? ')
        
