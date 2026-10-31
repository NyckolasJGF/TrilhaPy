# def saudacao(nome):
#     print(f"Olá: {nome}")

# saudacao(input("Digite seu Nome: "))


# def media(a, b):
#     return (a + b) / 2

# x1 = float(input("Digite a Primeira Nota: "))
# x2 = float(input("Digite a Segunda Nota: "))

# resultado = media(x1, x2)

# print("Resultado da Media é: " + str(resultado))


def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


for i in range(1, 11):
    if eh_par(i) == True:
        print(i)
