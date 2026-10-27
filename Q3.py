#Q3
entrada = input()
lista_entrada = entrada.split(" ")
nova_lista = []
i = 0

for x in lista_entrada:
    x = int(x)
    nova_lista.append(x)

nova_lista.sort()

for i in range(0, 3):
    print(nova_lista[i])

print("")

for i in range(0, 3):
    print(lista_entrada[i])