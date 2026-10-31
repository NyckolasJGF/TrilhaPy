# Q4
def fizzbuzz(n):
    resposta = []
    for i in range(1, n + 1):
        if i % 15 == 0:          
            resposta.append("FizzBuzz")

        elif i % 3 == 0:
            resposta.append("Fizz")

        elif i % 5 == 0:
            resposta.append("Buzz")

        else:
            resposta.append(str(i))
    return resposta

entrada = int(input())
print(fizzbuzz(entrada))