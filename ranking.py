"""
Arquivo: ranking.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: controlar o ranking local usando JSON.

Este arquivo agora atende as duas versões do projeto:
- versão terminal, chamada pelo main.py;
- versão web, chamada pelo app.py.

A medalha não é salva no JSON, porque ela depende da posição atual no ranking.
Exemplo: se uma pessoa está em 1º lugar, ela aparece como Ouro. Se outra pessoa
fizer mais pontos depois, o ranking é reordenado e a medalha muda automaticamente.
"""

# Importa json para ler e escrever dados no arquivo ranking.json.
import json

# Importa os para montar caminhos de arquivos de forma segura.
import os

# Importa datetime para registrar a data e horário da partida.
from datetime import datetime

# Importa funções auxiliares usadas na versão terminal.
from utilitarios import limpar_tela, linha, converter_tempo, pausar


# Guarda o caminho absoluto da pasta onde este arquivo ranking.py está.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define a pasta onde o arquivo de ranking ficará salvo.
PASTA_DADOS = os.path.join(BASE_DIR, "data")

# Define o caminho completo do arquivo JSON do ranking.
ARQUIVO_RANKING = os.path.join(PASTA_DADOS, "ranking.json")


def garantir_arquivo_ranking():
    """Garante que a pasta data e o arquivo ranking.json existam."""

    # Cria a pasta data se ela ainda não existir.
    os.makedirs(PASTA_DADOS, exist_ok=True)

    # Se o arquivo ranking.json ainda não existir, cria uma lista vazia.
    if not os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)


def carregar_ranking():
    """Carrega o ranking salvo no arquivo JSON."""

    # Garante que o arquivo exista antes de tentar abrir.
    garantir_arquivo_ranking()

    # Abre o arquivo em modo leitura.
    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as arquivo:
        try:
            # Transforma o JSON em uma lista Python.
            return json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio/corrompido, evita quebrar o sistema.
            return []


def salvar_ranking(ranking):
    """Salva a lista de ranking no arquivo JSON."""

    # Garante que a pasta data exista antes de salvar.
    garantir_arquivo_ranking()

    # Abre o arquivo em modo escrita e grava a lista atualizada.
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as arquivo:
        json.dump(ranking, arquivo, ensure_ascii=False, indent=4)


def ordenar_ranking(ranking):
    """Ordena por maior pontuação e, em empate, menor tempo."""

    # -pontuacao coloca maior pontuação primeiro.
    # tempo_segundos coloca quem fez em menor tempo na frente em caso de empate.
    # nome.lower() deixa a ordenação estável caso pontuação e tempo sejam iguais.
    return sorted(
        ranking,
        key=lambda item: (-item["pontuacao"], item["tempo_segundos"], item["nome"].lower())
    )


def definir_medalha_por_posicao(posicao):
    """Define medalha com base na posição atual do jogador."""

    if posicao == 1:
        return "Ouro"

    if posicao == 2:
        return "Prata"

    if posicao == 3:
        return "Bronze"

    return "Participante"


def atualizar_ranking(resultado):
    """Adiciona o resultado do jogador ao ranking e salva no JSON."""

    # Carrega o ranking já existente.
    ranking = carregar_ranking()

    # Monta um registro com os dados reais da partida.
    # A medalha não entra aqui porque ela muda conforme a posição no ranking.
    registro = {
        "nome": resultado["nome"],
        "idade": resultado["idade"],
        "grupo": resultado["grupo"],
        "pontuacao": resultado["pontuacao"],
        "pontuacao_maxima": resultado["pontuacao_maxima"],
        "acertos": resultado["acertos"],
        "erros": resultado["erros"],
        "aproveitamento": round(resultado["aproveitamento"], 1),
        "tempo_segundos": round(resultado["tempo_segundos"], 2),
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    # Adiciona a nova partida ao ranking.
    ranking.append(registro)

    # Ordena o ranking atualizado.
    ranking = ordenar_ranking(ranking)

    # Salva a lista ordenada no JSON.
    salvar_ranking(ranking)

    # Retorna o ranking atualizado para uso em outras telas.
    return ranking


def obter_ranking_formatado(limite=10):
    """Retorna o ranking pronto para terminal, API ou template web."""

    # Carrega e ordena os dados atuais do ranking.
    ranking = ordenar_ranking(carregar_ranking())

    # Lista que receberá os jogadores já com posição, medalha e tempo formatado.
    ranking_formatado = []

    # Percorre o ranking limitado ao TOP desejado.
    for posicao, jogador in enumerate(ranking[:limite], start=1):
        # Copia o dicionário para não alterar diretamente os dados carregados do JSON.
        item = jogador.copy()

        # Adiciona a colocação atual.
        item["posicao"] = posicao

        # Calcula medalha de acordo com a colocação atual.
        item["medalha"] = definir_medalha_por_posicao(posicao)

        # Adiciona uma versão amigável do tempo para exibição.
        item["tempo_formatado"] = converter_tempo(jogador["tempo_segundos"])

        # Adiciona o item final à lista formatada.
        ranking_formatado.append(item)

    return ranking_formatado


def exibir_ranking(limite=10):
    """Exibe o ranking no terminal."""

    # Limpa a tela para mostrar o ranking com mais destaque.
    limpar_tela()

    # Busca o ranking já formatado.
    ranking = obter_ranking_formatado(limite)

    # Cabeçalho da tela.
    linha()
    print("RANKING DOS GUARDIÕES".center(60))
    linha()

    # Se ainda não houver jogadores, informa o usuário.
    if len(ranking) == 0:
        print("Nenhum jogador no ranking ainda.")
        pausar()
        return

    # Mostra cada jogador do ranking.
    for jogador in ranking:
        print(f"{jogador['posicao']}º lugar - {jogador['nome']}")
        print(f"   Medalha: {jogador['medalha']}")
        print(f"   Pontuação: {jogador['pontuacao']}/{jogador['pontuacao_maxima']} pontos")
        print(f"   Acertos: {jogador['acertos']} | Erros: {jogador['erros']}")
        print(f"   Tempo: {jogador['tempo_formatado']}")
        print(f"   Grupo: {jogador['grupo']}")
        print()

    # Pausa para leitura antes de voltar ao menu.
    pausar()


# Permite testar este arquivo sozinho pelo terminal.
if __name__ == "__main__":
    exibir_ranking()
