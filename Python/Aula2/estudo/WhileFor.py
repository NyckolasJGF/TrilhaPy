# while e for

# while, usado para repetir uma quantidade incerta de
# counter = 1

# while (counter < 6):
#     print("Rodada", counter)

#     counter += 1

# print("Final do Jogo")


# for, usado quando sabemos quantas vezes queremos repetir exatamente tal ação
# frutas = ["banana", "maca", "melancia"]

# for fruta in frutas:
#     print("Tirei a fruta: ", fruta)
#     frutas.pop(-1)
#     print("Frutas restantes: ", frutas)

# for i in range(1, 10):
#     if i == 3:
#         continue    # pula o 3

#     if i == 6:
#         break       # para tudo no 6

#     print(i)        # imprime 1, 2, 4, 5

# num = 7
# i = 0
# for i in range(1, 11):
#     print(num * i)

# contador = 1
# soma = 0

# while (contador <= 100):
#     soma += contador

#     contador += 1
# print(soma)

# range(inicio, fim, passo)

# x = 1
# for i in range(6):
#     print("Dentro do Laço: " + str(x))
#     x += 1

# print("Fora do laço")

# print("Digite a senha correta: ")
# senha = "".join(input().split())  # meio que junta tudo, tira os espaços e tal
# lista_senha = list(senha)

# nova_senha = []
# i = 0

# for digito in lista_senha:
#     digito = int(digito)
#     nova_senha.append(digito)

# print(nova_senha)

# while len(nova_senha) > 2:
#     nova_senha[0] += nova_senha.pop()

#     if nova_senha[0] > 9:
#         nova_senha[1] += (nova_senha[0] - 9)
#         nova_senha[0] = 9

# print(nova_senha)



# soma = 0

# for i in range(1, 21):
#     if i % 2 == 0:
#         soma += i

# print(soma)        



stopper = 0
soma = 0
entrada = int(input())

while entrada != 0:
    soma += entrada
    entrada = int(input())

print(soma)    