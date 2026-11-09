Simulador de Vida de Estudante

Jogo de terminal feito em Python onde a ideia é você conseguir sobreviver à reta final de um **período letivo de 12 semanas**, equilibrando **tempo, energia e dinheiro**. É preciso estudar para passar nas provas, cada prova no final do mês, mas também trabalhar para pagar as contas.

> Mini projeto do primeiro bloco da trilha de Python (variáveis, condicionais, repetição, funções, exceções, listas, OOP).

##Como rodar:

Requisito: Python 3.8 ou superior.

```
python simulador.py
```

Exemplo da tela principal do sistema:

```
Semana 1/12 | Turnos restantes: 8
Dinheiro: R$ 350 | Energia: 100 | XP: 0 | Nível: 1

Escolha uma atividade:
1. Estudar (custa 15 de energia, 1 turno(s), ganha 15 de XP)
2. Aula (custa 10 de energia, 1 turno(s), custa R$60, ganha 30 de XP)
3. Trabalhar (custa 25 de energia, 2 turno(s), ganha R$100)
4. Descansar (1 turno(s), ganha 25 de energia)
5. Lazer (1 turno(s), custa R$40, ganha 35 de energia)
6. Avançar semana
7. Mostrar estado atual
8. Sair do jogo
```

##Regras

**Recursos do jogador:** começa com R$ 350, 100 de energia (que é o valor máximo), 0 de XP e nível 1.
A cada **120 XP** o nível sobe.

**Cada semana tem 8 turnos.** Toda atividade gasta valores determinados de turnos, e a semana só avança quando você escolhe *Avançar semana*.

| Atividade | Turnos | Energia | Dinheiro | XP  |
|---        |---     |---      |---       |---  |
| Estudar   | 1      | -15     |          | +15 |
| Aula      | 1      | -10     | -R$ 60   | +30 |
| Trabalhar | 2      | -25     | +R$ 100  |     |
| Descansar | 1      | +25     |          |     |
| Lazer     | 1      | +35     | -R$ 40   |     |

**Contas e provas** acontecem juntas, no fim das semanas **4, 8 e 12**:

- **Conta mensal de R$ 220.** Se você não tiver o dinheiro, o jogo acaba em derrota.
- **Prova.** A nota (0 a 10) é sorteada de acordo com o seu nível em relação ao esperado para aquela prova:

| Prova | Nível esperado | Nível abaixo | Nível igual | Nível acima |
|---|---|---|---|---|
| 1 (semana 4) | 2 | 4,5 a 6,0 | 6,0 a 10 | 8,5 a 10 |
| 2 (semana 8) | 3 | 4,5 a 6,0 | 6,0 a 10 | 8,5 a 10 |
| 3 (semana 12) | 4 | 4,5 a 6,0 | 6,0 a 10 | 8,5 a 10 |

**Vitória:** média das três provas **igual ou maior que 7**. Ir mal em uma prova não elimina: dá pra recuperar nas outras.

##Estrutura do código

| Classe | Responsabilidade |
|---|---|
| `Jogador` | Guarda dinheiro, energia, XP e nível. Só muda por métodos que validam os valores (`ganhar_*`, `gastar_*`, `pode_gastar_*`) |
| `Atividade` | Classe base com custos e ganhos. O método `executar` **verifica tudo antes de cobrar** qualquer coisa |
| `Estudar`, `Aula`, `Trabalhar`, `Descansar`, `Lazer` | Herdam de `Atividade`; só definem seus próprios números |
| `Simulacao` | Onde o jogo "acontece" de verdade: semanas, turnos, contas, provas, menu e o loop principal |

Conceitos usados: classes e objetos, herança, validação de entrada com `try/except`, listas, `enumerate`, f-strings e o módulo `random`.


##Balanceamento

O arquivo `balanceamento.py` simula **1000 partidas por estratégia** para medir a taxa de vitória (sem eventos aleatórios):

```
python balanceamento.py
```

| Estratégia (repetida toda semana) | Vitória |
|---|---|
| Equilibrada (1 trabalho, 3 estudos, 2 descansos, 1 lazer) | 100% |
| Estudiosa (1 trabalho, 4 estudos, 1 descanso, 1 lazer) | 94% |
| Rica com aula (2 trabalhos, 1 aula, 2 descansos, 1 lazer) | 93% |
| Só lazer (1 trabalho, 2 estudos, 2 descansos, 2 lazeres) | 0% |

A ideia foi de conseguir ter **mais de um caminho viável** pra vencer, e fazer com que ignorar os estudos ou o dinheiro leve à derrota.

Ideia de próximos passos

- [ ] Eventos aleatórios (bons e ruins, com os ruins mais frequentes, pq infelizmente é assim na faculdade)
- [ ] Salvar um ranking das partidas em arquivo
- [ ] Tornar os atributos do `Jogador` privados (encapsulamento completo)
- [ ] Testes automáticos

##Autor

Feito por **[Nyckolas José]**
