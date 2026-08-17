"""
Arquivo: utilitarios.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: guardar funções pequenas que ajudam o sistema inteiro.

Por que este arquivo existe?
- Para evitar repetição de código.
- Para deixar o main.py mais limpo.
- Para concentrar funções de apoio, como limpar tela, pausar e validar entrada.
"""

# Importa o módulo os para executar comandos do sistema operacional.
import os

# Importa o módulo time para usar pequenas pausas no programa.
import time


def limpar_tela():
    """Limpa a tela do terminal no Windows, Linux ou macOS."""

    # Se estiver no Windows, usa o comando cls.
    if os.name == "nt":
        os.system("cls")

    # Se estiver em Linux/macOS com terminal configurado, usa clear.
    elif os.environ.get("TERM"):
        os.system("clear")

    # Se o terminal não permitir limpar a tela, apenas pula algumas linhas.
    else:
        print("\n" * 5)


def pausar(mensagem="\nPressione ENTER para voltar ao menu..."):
    """Pausa o programa até o usuário pressionar ENTER."""

    # O input segura o programa para a pessoa conseguir ler o conteúdo da tela.
    input(mensagem)


def linha(tamanho=60):
    """Imprime uma linha de separação para organizar visualmente o terminal."""

    # Multiplica o caractere '=' pelo tamanho escolhido.
    print("=" * tamanho)


def exibir_logo():
    """Exibe a logo em ASCII do projeto.

    Esta função foi mantida apenas como recurso opcional.
    A abertura principal agora fica em menu.py, usando a mensagem original do grupo.
    """

    limpar_tela()

    print(r"""
__________                    ___.                         
\______   \_____ ____________ \_ |__   ____   ____   ______
 |     ___/\__  \\_  __ \__  \ | __ \_/ __ \ /    \ /  ___/
 |    |     / __ \|  | \// __ \| \_\ \  ___/|   |  \___ \ 
 |____|    (____  /__|  (____  /___  /\___  >___|  /____  >
                \/           \/    \/     \/     \/     \/ 
  ________                       .___.__                   
 /  _____/ __ _______ _______  __| _/|__|____    ____      
/   \  ___|  |  \__  \\_  __ \/ __ | |  \__  \  /  _ \     
\    \_\  \  |  // __ \|  | \/ /_/ | |  |/ __ \(  <_> )    
 \______  /____/(____  /__|  \____ | |__(____  /\____/     
        \/           \/           \/         \/             
""")

    linha()
    print("MINI-GAME — MAIO LARANJA (PIQUE ECA)".center(60))
    print("Informar é conscientizar. Denunciar é proteger.".center(60))
    linha()

    input("\nPressione ENTER para continuar...")

def ler_opcao(mensagem, opcoes_validas):
    """
    Lê uma opção digitada pelo usuário e só retorna quando ela for válida.

    Parâmetros:
    - mensagem: texto exibido no input.
    - opcoes_validas: lista com as opções aceitas, por exemplo ["1", "2", "3"].
    """

    # O while True cria uma repetição que só termina quando o usuário digitar uma opção válida.
    while True:

        # Lê a opção, remove espaços nas pontas e transforma em maiúscula.
        opcao = input(mensagem).strip().upper()

        # Se a opção estiver na lista de opções válidas, ela é retornada para quem chamou a função.
        if opcao in opcoes_validas:
            return opcao

        # Se chegou aqui, significa que a opção não era válida.
        print("Opção inválida. Tente novamente.")


def converter_tempo(segundos):
    """Converte segundos em um texto no formato 'X min Y s'."""

    # int() remove casas decimais para facilitar a exibição.
    segundos = int(segundos)

    # // faz divisão inteira para descobrir os minutos completos.
    minutos = segundos // 60

    # % pega o resto da divisão, ou seja, os segundos que sobraram.
    segundos_restantes = segundos % 60

    # Retorna uma string formatada para mostrar o tempo ao usuário.
    return f"{minutos} min {segundos_restantes} s"
