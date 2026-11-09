import random
EM_ANDAMENTO = "Período em andamento"


class Jogador:
    def __init__(self, dinheiro=350, energia=100, xp=0, nivel=1, xp_por_nivel=120):
        self.dinheiro = dinheiro
        self.energia = energia
        self.xp = xp
        self.nivel = nivel
        self.xp_por_nivel = xp_por_nivel

    # getters

    def get_energia(self):
        return self.energia

    def get_dinheiro(self):
        return self.dinheiro

    def get_xp(self):
        return self.xp

    def get_nivel(self):
        return self.nivel

    def pode_gastar_dinheiro(self, valor):
        return 0 <= valor <= self.dinheiro

    def pode_gastar_energia(self, valor):
        return 0 <= valor <= self.energia

    # metodos dinheiro

    def ganhar_dinheiro(self, valor):
        if valor < 0:
            return False
        self.dinheiro += valor
        return True

    def gastar_dinheiro(self, valor):
        if not self.pode_gastar_dinheiro(valor):
            return False
        self.dinheiro -= valor
        return True

    # metodos xp

    def ganhar_xp(self, valor):
        if valor < 0:
            return False

        self.xp += valor
        while self.xp >= self.xp_por_nivel:
            self.xp -= self.xp_por_nivel
            self.nivel += 1
        return True

    # metodos energia

    def ganhar_energia(self, valor):
        if valor < 0:
            return False
        self.energia = min(100, self.energia + valor)
        return True

    def gastar_energia(self, valor):
        if not self.pode_gastar_energia(valor):
            return False
        self.energia -= valor
        return True


class Atividade:
    def __init__(self, nome, custo_energia, custo_turno, custo_dinheiro=0,
                 ganho_xp=0, ganho_dinheiro=0, ganho_energia=0):
        self.nome = nome
        self.custo_energia = custo_energia
        self.custo_turno = custo_turno
        self.custo_dinheiro = custo_dinheiro
        self.ganho_xp = ganho_xp
        self.ganho_dinheiro = ganho_dinheiro
        self.ganho_energia = ganho_energia

    def executar(self, jogador):
        # 1º verifica tudo, sem gastar nada
        if not jogador.pode_gastar_energia(self.custo_energia):
            return False
        if not jogador.pode_gastar_dinheiro(self.custo_dinheiro):
            return False

        # 2º cobra os custos
        jogador.gastar_energia(self.custo_energia)
        jogador.gastar_dinheiro(self.custo_dinheiro)

        # 3º aplica os ganhos
        jogador.ganhar_xp(self.ganho_xp)
        jogador.ganhar_dinheiro(self.ganho_dinheiro)
        jogador.ganhar_energia(self.ganho_energia)
        return True

    def descricao(self):
        partes = []
        if self.custo_energia > 0:
            partes.append(f"custa {self.custo_energia} de energia")
        if self.custo_turno > 0:
            partes.append(f"{self.custo_turno} turno(s)")
        if self.custo_dinheiro > 0:
            partes.append(f"custa R${self.custo_dinheiro}")
        if self.ganho_xp > 0:
            partes.append(f"ganha {self.ganho_xp} de XP")
        if self.ganho_dinheiro > 0:
            partes.append(f"ganha R${self.ganho_dinheiro}")
        if self.ganho_energia > 0:
            partes.append(f"ganha {self.ganho_energia} de energia")

        return f"{self.nome} ({', '.join(partes)})"


class Estudar(Atividade):
    def __init__(self):
        super().__init__("Estudar", custo_energia=15, custo_turno=1, ganho_xp=15)


class Aula(Atividade):
    def __init__(self):
        super().__init__("Aula", custo_energia=10, custo_turno=1,
                         custo_dinheiro=60, ganho_xp=30)


class Trabalhar(Atividade):
    def __init__(self):
        super().__init__("Trabalhar", custo_energia=25, custo_turno=2,
                         ganho_dinheiro=100)


class Descansar(Atividade):
    def __init__(self):
        super().__init__("Descansar", custo_energia=0, custo_turno=1,
                         ganho_energia=25)


class Lazer(Atividade):
    def __init__(self):
        super().__init__("Lazer", custo_energia=0, custo_turno=1,
                         custo_dinheiro=40, ganho_energia=35)


class Simulacao:
    def __init__(self, jogador, semana_atual=1, total_semanas=12, turnos_por_semana=8, conta_mensal=220, semanas_por_mes=4, nota_minima=7, niveis_esperados=(2, 3, 4)):
        self.jogador = jogador
        self.semana_atual = semana_atual
        self.total_semanas = total_semanas
        self.turnos_por_semana = turnos_por_semana
        self.turnos_restantes = turnos_por_semana
        self.conta_mensal = conta_mensal
        self.semanas_por_mes = semanas_por_mes
        self.nota_minima = nota_minima
        self.niveis_esperados = niveis_esperados
        self.notas = []
        self.status = EM_ANDAMENTO
        self.atividades = [
            Estudar(),
            Aula(),
            Trabalhar(),
            Descansar(),
            Lazer(),
        ]

    # estado do jogo
    def acabou(self):
        return self.status != EM_ANDAMENTO

    def derrota(self, motivo):
        self.status = f"Derrota: {motivo}"
        print(f"Você não atingiu os objetivos do período ({motivo}).")

    def vitoria(self):
        self.status = "Vitória"
        print("Parabéns! Você passou de período, boa sorte no próximo!")

    def mostrar_estado(self):
        print(
            f"Semana {self.semana_atual}/{self.total_semanas} | "f"Turnos restantes: {self.turnos_restantes}")
        print(f"Dinheiro: R$ {self.jogador.get_dinheiro()} | "f"Energia: {self.jogador.get_energia()} | "f"XP: {self.jogador.get_xp()} | "f"Nível: {self.jogador.get_nivel()}")

    #  ações do jogador

    def tentar_atividade(self, atividade):
        if self.acabou():
            print("O período já acabou.")
            return False

        if self.turnos_restantes < atividade.custo_turno:
            print("Não há turnos suficientes para realizar a atividade.")
            return False

        if not atividade.executar(self.jogador):
            if not self.jogador.pode_gastar_energia(atividade.custo_energia):
                print("Você não tem energia suficiente.")
            elif not self.jogador.pode_gastar_dinheiro(atividade.custo_dinheiro):
                print("Não tem dinheiro suficiente para realizar o pagamento.")
            return False

        self.turnos_restantes -= atividade.custo_turno
        return True

    # passagem do tempo

    def fechar_mes(self):
        # 1. cobra a conta; se falhar, o jogo acaba aqui
        if not self.jogador.gastar_dinheiro(self.conta_mensal):
            self.derrota("não conseguiu pagar a conta mensal")
            return

        # 2. prova: o jogador vê a conta e a nota ANTES do resultado final
        nota = self.fazer_prova()
        print(f"Fim do mês! Conta de R${self.conta_mensal} paga. "
              f"Nota da prova {self.posicao_da_prova() + 1}: {nota}")

        # 3. na última semana, a média decide o jogo
        if self.semana_atual >= self.total_semanas:
            media = sum(self.notas) / len(self.notas)
            if media >= self.nota_minima:
                self.vitoria()
            else:
                self.derrota(f"média {media:.2f} abaixo de {self.nota_minima}")

    def avancar_semana(self):
        # jogo que já acabou não anda
        if self.acabou():
            return False

        # fim de mês: conta + prova
        if self.semana_atual % self.semanas_por_mes == 0:
            self.fechar_mes()

        # acabou agora (derrota/vitória) ou era a última semana: não avança
        if self.acabou() or self.semana_atual >= self.total_semanas:
            return False

        # vira a semana
        self.semana_atual += 1
        self.turnos_restantes = self.turnos_por_semana
        return True

    # parte da prova

    def sortear_nota(self, minimo, maximo):
        return round(random.uniform(minimo, maximo), 1)

    def posicao_da_prova(self):
        return self.semana_atual // self.semanas_por_mes - 1

    def fazer_prova(self):
        posicao = self.posicao_da_prova()
        esperado = self.niveis_esperados[posicao]
        nivel = self.jogador.get_nivel()

        if nivel < esperado:
            minimo = 4.5
            maximo = 6.0
        elif nivel == esperado:
            minimo = 6.0
            maximo = 10
        else:
            minimo = 8.5
            maximo = 10

        nota = self.sortear_nota(minimo, maximo)
        self.notas.append(nota)
        return nota

    def mostrar_menu(self):
        print("\nEscolha uma atividade:")
        for numero, atividade in enumerate(self.atividades, start=1):
            print(f"{numero}. {atividade.descricao()}")

        opcao_extra = len(self.atividades) + 1
        print(f"{opcao_extra}. Avançar semana")
        print(f"{opcao_extra + 1}. Mostrar estado atual")
        print(f"{opcao_extra + 2}. Sair do jogo")

    def ler_opcao(self):
        while True:
            try:
                opcao = int(input("Digite o número da opção desejada: "))
                if 1 <= opcao <= len(self.atividades) + 3:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def jogar(self):
        while not self.acabou():

            self.mostrar_estado()
            self.mostrar_menu()
            opcao = self.ler_opcao()

            if 1 <= opcao <= len(self.atividades):
                atividade = self.atividades[opcao - 1]
                sucesso = self.tentar_atividade(atividade)

                if sucesso:
                    print(f"Você realizou a atividade: {atividade.nome}")
                print("")

            elif opcao == len(self.atividades) + 1:
                self.avancar_semana()
                print("")

            elif opcao == len(self.atividades) + 2:
                self.mostrar_estado()

            elif opcao == len(self.atividades) + 3:
                print("Saindo do jogo...")

                break

        if self.acabou():
            print(f"Fim do período! Status final: {self.status}")


# ---------- testes ----------
class SimulacaoNota5(Simulacao):
    """Só pra teste: toda prova tira 5."""

    def fazer_prova(self, nota_fixa=5):
        self.notas.append(nota_fixa)
        return nota_fixa


def rodar_12_semanas(sim):
    for _ in range(12):
        sim.avancar_semana()
    print(f"-> status: {sim.status} | semana: {sim.semana_atual} | "
          f"dinheiro: {sim.jogador.get_dinheiro()} | notas: {sim.notas}\n")


# Rodar o code
if __name__ == "__main__":
    Simulacao(Jogador()).jogar()


# print("Teste 1: jogador rico, nivel 6 (esperado: Vitória, semana 12, dinheiro 9340)")
# rodar_12_semanas(Simulacao(Jogador(dinheiro=10000, nivel=6)))

# print("Teste 2: jogador sem fazer nada (esperado: derrota por contas, semana 8, UMA mensagem)")
# rodar_12_semanas(Simulacao(Jogador()))

# print("Teste 3: jogador rico, nivel 1 (esperado: derrota por média)")
# rodar_12_semanas(SimulacaoNota5(Jogador(dinheiro=10000, nivel=1)))
