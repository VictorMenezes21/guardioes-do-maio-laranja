"""
Arquivo: menu.py
Projeto: MINI-GAME — Maio Laranja (Pique ECA)
Função do arquivo: exibir a abertura e o menu principal do sistema.

Ajuste feito na integração:
- Mantivemos a ideia original do menu com emojis e mensagem de missão.
- Transformamos o menu em função para o main.py conseguir controlar as opções.
"""

# Importa o módulo time para dar uma pequena pausa na abertura.
import time


def linhas(tamanho=50):
    """Imprime uma linha para separar visualmente as partes do menu."""

    print("=" * tamanho)


def mostrar_abertura():
    """Mostra a tela inicial do projeto antes do cadastro."""

    linhas()
    print('🧡 GUARDIÕES DA INFÂNCIA - MAIO LARANJA 🧡'.center(50))
    linhas()
    print("SEJA BEM-VINDO(A)! SUA MISSÃO É AJUDAR NA CONSCIENTIZAÇÃO!")

    # Pausa curta para dar sensação de abertura de jogo.
    time.sleep(1.0)

    # Pausa manual para ninguém perder a leitura da tela inicial.
    input("\nPressione ENTER para iniciar a missão...")


def mostrar_menu(jogador):
    """Exibe o menu principal do sistema."""

    linhas()
    print('CENTRAL DOS GUARDIÕES:'.center(50))
    linhas()

    # Mostra quem está jogando no momento.
    print(f"Jogador(a): {jogador['nome']}")
    print(f"Grupo: {jogador['grupo']}\n")

    print("1 - Orientações e prevenção")
    print("2 - Canal de denúncia")
    print("3 - Mini-game")
    print("4 - Informações sobre a campanha")
    print("5 - Ranking")
    print("6 - Novo jogador")
    print("7 - Encerrar missão")
