import io
import contextlib

from Simulador import Simulacao, Jogador, Estudar, Aula, Trabalhar, Descansar, Lazer

ESTRATEGIAS = {
    "Equilibrada (1 trabalho, 3 estudos, 2 descansos, 1 lazer)":
        [Trabalhar, Estudar, Estudar, Estudar, Descansar, Descansar, Lazer],
    "Estudiosa (1 trabalho, 4 estudos, 1 descanso, 1 lazer)":
        [Trabalhar, Estudar, Estudar, Estudar, Estudar, Descansar, Lazer],
    "Rica com aula (2 trabalhos, 1 aula, 2 descansos, 1 lazer)":
        [Trabalhar, Trabalhar, Aula, Descansar, Descansar, Lazer],
    "Só lazer (1 trabalho, 2 estudos, 2 descansos, 2 lazeres)":
        [Trabalhar, Estudar, Estudar, Descansar, Descansar, Lazer, Lazer],
}


def jogar_com_plano(plano):
    with contextlib.redirect_stdout(io.StringIO()):
        sim = Simulacao(Jogador())
        for _ in range(sim.total_semanas):
            for classe in plano:
                sim.tentar_atividade(classe())
            sim.avancar_semana()
    return sim.status


def taxa_de_vitoria(plano, jogos=1000):
    vitorias = sum(1 for _ in range(jogos) if jogar_com_plano(plano) == "Vitória")
    return vitorias / jogos


if __name__ == "__main__":
    print("Taxa de vitória por estratégia (1000 partidas cada):\n")
    for nome, plano in ESTRATEGIAS.items():
        print(f"{taxa_de_vitoria(plano):5.0%}  {nome}")