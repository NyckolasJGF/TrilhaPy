# Q2 - Funcionario
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return (self.salario_base)


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return (self.salario_base + self.bonus)


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, vendas, comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return (self.salario_base + self.vendas * (self.comissao / 100))


gerente1 = Gerente("Carlos", 5000, 1500)
gerente2 = Gerente("Pedro", 2000, 3000)

Vendedor1 = Vendedor("Ana", 2000, 10000, 0.1)
Vendedor2 = Vendedor("Caio", 3000, 5000, 0.5)

for f in [gerente1, gerente2, Vendedor1, Vendedor2]:
    print(f"{f.nome}: R$ {f.calcular_salario():.2f}")