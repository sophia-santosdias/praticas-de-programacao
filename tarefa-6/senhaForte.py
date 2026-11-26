# EXERCÍCIO: Elaborar um programa que determine se uma senha é forte ou não. Uma senha é considerada forte se ela tiver no mínimo 8 caracteres, pelo menos uma letra maiúscula, pelo menos uma letra minúscula, pelo menos um número e pelo menos um caractere especial.
# ALUNAS: Sophia Santos e Lorena Luvizotto

def determinaSenha(senha):
    if len(senha) < 8:
        return False
    elif senha.islower():
        return False
    elif senha.isupper():
        return False
    elif senha.isalnum():
        return False
    elif not any(char.isnumeric() for char in senha) or not any(char.isalpha() for char in senha):
        return False
    else:
        return True
    

senha = input('Digite a senha: ')
print(determinaSenha(senha))

