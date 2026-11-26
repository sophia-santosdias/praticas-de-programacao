# EXERCÍCIO: Implementar um sistema de criptografia de cesar usando a biblioteca turtle.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import string

def criptografa(c):
    if c == ' ':
        return '@'
    else:
        pos = alf.index(c)
        return alf[pos + 10]

def decriptografa(c):
    if c == '@':
        return ' '
    else:
        pos = alf.index(c)
        return alf[pos - 10]

alf = string.ascii_uppercase*2
texto = 'ENCONTRO AS DEZESSETE HORAS EM PARIS NO CAFE DE LA PAIX NO CHAMPS ELISEES'
msgCrip = msgDecrip = ''
    
for i in texto:
    c = criptografa(i)
    msgCrip += c
    
for i in msgCrip:
    c = decriptografa(i)
    msgDecrip += c
    
print(f'TEXTO ORIGINAL: {texto}')
print(f'MENSAGEM CRIPTOGRAFADA: {msgCrip}')
print(f'MENSGEM DECRIPTOGRAFADA: {msgDecrip}')    
    