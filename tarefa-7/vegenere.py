# EXERCÍCIO: Implementar um sistema de criptografia de vigenere usando a biblioteca turtle. 
# ALUNAS: Sophia Santos e Lorena Luvizotto

import string

alf = string.ascii_uppercase

def vigenere(texto, senha):
    msg = ''
    i = p = 0
    
    if len(senha) < len(texto):
        senha = senha * (len(texto) // len(senha) + 1)
        
    while i < len(texto):
        if texto[i] != ' ':
            c = alf[(alf.index(texto[i]) + alf.index(senha[p])) % 26]
            p += 1
        else:
            c = '@'
        i += 1    
        msg += c        
        
    return msg

def dec_vigenere(textoCrip, senha):
    msg = ''
    i = p = 0
    
    if len(senha) < len(textoCrip):
        senha = senha * (len(textoCrip) // len(senha) + 1)
        
    while i < len(textoCrip):
        if textoCrip[i] != '@':
            c = alf[(alf.index(textoCrip[i]) - alf.index(senha[p]) + 26) % 26]
            p += 1
        else:
            c = ' '
        i += 1    
        msg += c        
        
    return msg





textoCrip = vigenere('ENCONTRO NO BAR DO OSWALDO NA BARRA DA TIJUCA AS DEZ HORAS DA NOITE', 'XYZPTO')

textoDecrip = dec_vigenere(textoCrip, 'XYZPTO')


