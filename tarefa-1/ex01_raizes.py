# EXERCÍCIO 1: Calcular raízes
# ALUNAS: Sophia Santos e Lorena Luvizotto

a = int(input("Insira o coeficiente de x²: "))
b = int(input("Insira o coeficiente de x: "))
c = int(input("Insira o coeficiente c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não há raiz real")
elif delta == 0:
    raiz0 = (-b + delta**0.5) / (2*a)
    print(f'A equação possui uma raiz real no valor de {raiz0}')
else:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes são {raiz1} e {raiz2}")