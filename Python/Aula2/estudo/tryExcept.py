# try:
#     x1 = int(input("Digite um valor: ")) 
#     x2 = int(input("Digite o segundo valor: ")) 

#     resultado = (x1 / x2)
#     print(resultado)

# except ValueError:
#     print("Digite um valor inteiro.")

# except ZeroDivisionError:
#     print("N da pra dividir por zero n irmao")

# try:
#     numero = int(input("Digite um número: "))

# except ValueError:
#     print("Você não digitou um inteiro!")

# else:
#     print("Número válido:", numero)

# try:
#     numero = int(input("Digite um número: "))
#     print("Número:", numero)

# except ValueError:
#     print("Entrada inválida!")

# finally:
#     print("Programa finalizado.")

try:
    x1 = int(input("Digite um valor inteiro: "))
    print("Número válido!")

except ValueError:
    print("Entrada inválida!")

finally:
    print("Fim do programa.")