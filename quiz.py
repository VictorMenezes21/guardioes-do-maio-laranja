"""
Arquivo: quiz.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: executar o mini-game de perguntas e respostas.

Este arquivo usa:
- perguntas.py para buscar as perguntas;
- time para medir o tempo do jogador;
- utilitarios.py para validar opções e formatar o tempo.
"""

# Importa o módulo time para implementar o cronômetro.
import time

# Importa as perguntas e a pontuação por nível.
from perguntas import obter_perguntas_por_grupo, calcular_pontuacao_maxima, PONTOS_POR_NIVEL

# Importa funções auxiliares de interface.
from utilitarios import limpar_tela, linha, ler_opcao, converter_tempo, pausar


def definir_mensagem_por_aproveitamento(aproveitamento):
    """Define uma mensagem final com base no percentual de aproveitamento do jogador."""

    # Aproveitamento alto: o jogador foi muito bem no quiz.
    if aproveitamento >= 80:
        return "Excelente! Você demonstrou ótimo conhecimento sobre o tema."

    # Aproveitamento intermediário: o jogador acertou uma boa parte, mas ainda pode aprender mais.
    if aproveitamento >= 50:
        return "Muito bem! Você foi bem e ainda pode continuar aprendendo."

    # Aproveitamento baixo: a mensagem incentiva o aprendizado sem constranger o jogador.
    return "Você concluiu o desafio. Continue se informando sobre o Maio Laranja."

def mostrar_resultado(resultado):
    """Mostra o resultado final do quiz."""

    # Exibe cabeçalho da tela de resultado.
    linha()
    print("RESULTADO FINAL".center(60))
    linha()

    # Mostra os dados principais da partida.
    print(f"Jogador: {resultado['nome']}")
    print(f"Grupo: {resultado['grupo']}")
    print(f"Acertos: {resultado['acertos']}")
    print(f"Erros: {resultado['erros']}")
    print(f"Pontuação: {resultado['pontuacao']} pontos")
    print(f"Aproveitamento: {resultado['aproveitamento']:.1f}%")
    print(f"Tempo: {converter_tempo(resultado['tempo_segundos'])}")
    # A medalha não aparece aqui porque ela depende da posição no ranking.
    # Exemplo: se só uma pessoa jogou, ela deve ser ouro por estar em 1º lugar.
    # Por isso, a medalha é calculada no ranking.py, e não no resultado individual.
    print("Medalha: definida pela colocação no ranking")

    # Mensagem final personalizada de acordo com o aproveitamento do jogador.
    print(f"\n{definir_mensagem_por_aproveitamento(resultado['aproveitamento'])}")


def iniciar_quiz(jogador):
    """
    Executa o quiz para o jogador informado.

    Parâmetro:
    - jogador: dicionário criado no cadastro_usuario.py.

    Retorno:
    - dicionário com resultado da partida.
    """

    # Limpa a tela para começar o quiz organizado.
    limpar_tela()

    # Busca as perguntas de acordo com o grupo do jogador.
    perguntas = obter_perguntas_por_grupo(jogador["grupo"])

    # Calcula a maior pontuação possível para esse conjunto de perguntas.
    pontuacao_maxima = calcular_pontuacao_maxima(perguntas)

    # Inicializa contadores da partida.
    pontuacao = 0
    acertos = 0
    erros = 0

    # Tela inicial do mini-game.
    linha()
    print("MINI-GAME — PIQUE ECA".center(60))
    linha()
    print(f"Jogador: {jogador['nome']}")
    print(f"Grupo: {jogador['grupo']}")
    print(f"Total de perguntas: {len(perguntas)}")
    print("Pontuação: Fácil = 10 | Médio = 20 | Difícil = 30")
    print("\nResponda digitando apenas a letra da alternativa.")
    pausar("\nPressione ENTER para iniciar o quiz...")

    # Marca o horário inicial do quiz.
    inicio = time.time()

    # Percorre cada pergunta da lista.
    for numero, pergunta in enumerate(perguntas, 1):

        # Limpa a tela a cada pergunta para não ficar poluído.
        limpar_tela()

        # Mostra cabeçalho da pergunta atual.
        linha()
        print(f"PERGUNTA {numero}/{len(perguntas)} — NÍVEL {pergunta['nivel'].upper()}".center(60))
        linha()

        # Mostra o enunciado.
        print(pergunta["pergunta"])
        print()

        # Mostra todas as alternativas.
        for opcao in pergunta["opcoes"]:
            print(opcao)

        # Lê uma resposta válida.
        resposta_usuario = ler_opcao("\nResposta: ", ["A", "B", "C", "D"])

        # Verifica se a resposta está correta.
        if resposta_usuario == pergunta["resposta"]:

            # Busca quantos pontos vale a pergunta pelo nível.
            pontos_da_pergunta = PONTOS_POR_NIVEL[pergunta["nivel"]]

            # Soma os pontos da pergunta na pontuação total.
            pontuacao += pontos_da_pergunta

            # Soma um acerto.
            acertos += 1

            # Mostra feedback positivo.
            print(f"\nCorreto! Você ganhou {pontos_da_pergunta} pontos.")
        else:

            # Soma um erro.
            erros += 1

            # Mostra a resposta correta.
            print(f"\nResposta incorreta. A resposta correta era {pergunta['resposta']}.")

        # Mostra a justificativa em qualquer caso, para manter o objetivo educativo.
        print(f"Justificativa: {pergunta['justificativa']}")

        # Pausa antes de ir para a próxima pergunta.
        pausar("\nPressione ENTER para continuar...")

    # Marca o horário final do quiz.
    fim = time.time()

    # Calcula o tempo total gasto.
    tempo_total = fim - inicio

    # Calcula o percentual de aproveitamento.
    aproveitamento = (pontuacao / pontuacao_maxima) * 100 if pontuacao_maxima > 0 else 0

    # Cria um dicionário com o resultado completo.
    resultado = {
        "nome": jogador["nome"],
        "idade": jogador["idade"],
        "grupo": jogador["grupo"],
        "pontuacao": pontuacao,
        "pontuacao_maxima": pontuacao_maxima,
        "acertos": acertos,
        "erros": erros,
        "aproveitamento": aproveitamento,
        "tempo_segundos": tempo_total
    }

    # Limpa a tela para mostrar apenas o resultado final.
    limpar_tela()

    # Exibe o resultado final.
    mostrar_resultado(resultado)

    # Pausa para leitura.
    pausar()

    # Retorna o resultado para o main.py poder atualizar o ranking.
    return resultado
