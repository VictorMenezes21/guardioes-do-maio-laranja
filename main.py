"""
Arquivo: main.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: integrar todas as partes do sistema.

Este é o arquivo principal.
É ele que chama:
- cadastro do jogador;
- menu;
- orientações;
- canais de denúncia;
- quiz;
- ranking;
- encerramento.

Para executar o projeto, rode no terminal:
python main.py
"""

# Importa funções de apoio para interface e validação.
from utilitarios import limpar_tela, linha, ler_opcao, pausar

# Importa a função de cadastro do jogador.
from cadastro_usuario import cadastrar_jogador

# Importa a função que mostra o menu principal.
from menu import mostrar_abertura, mostrar_menu

# Importa as funções de campanha e orientações.
from orientacoes_e_campanha import mostrar_campanha, mostrar_orientacoes

# Importa a função que mostra os canais de denúncia.
from canais_denuncias import mostrar_menu_denuncia

# Importa a função que executa o quiz.
from quiz import iniciar_quiz

# Importa as funções de ranking.
from ranking import atualizar_ranking, exibir_ranking


def encerrar_sistema():
    """Mostra a mensagem final do sistema."""

    # Limpa a tela antes da mensagem final.
    limpar_tela()

    # Cabeçalho de encerramento.
    linha()
    print("MISSÃO ENCERRADA".center(60))
    linha()

    # Mensagem final solicitada para a parte do Victor.
    print("Parabéns, Guardião!")
    print("Obrigado por participar do Pique ECA.")
    print("Informar é conscientizar. Denunciar é proteger.")

    # Linha final decorativa.
    linha()

    # Pausa para a mensagem final não sumir rápido quando o programa terminar.
    pausar("\nPressione ENTER para finalizar o sistema...")


def main():
    """Função principal do sistema."""

    # Exibe a abertura original do grupo uma vez no início.
    mostrar_abertura()

    # Cadastra o primeiro jogador.
    jogador = cadastrar_jogador()

    # Pausa para a pessoa ver que o cadastro foi feito.
    pausar("\nPressione ENTER para abrir o menu...")

    # Laço principal do programa.
    # Ele mantém o menu rodando até o usuário escolher encerrar.
    while True:

        # Limpa a tela antes de mostrar o menu.
        limpar_tela()

        # Mostra o menu com o jogador atual.
        mostrar_menu(jogador)

        # Lê a opção do usuário já validando as opções permitidas.
        opcao = ler_opcao("\nEscolha uma opção: ", ["1", "2", "3", "4", "5", "6", "7"])

        # Opção 1: orientações de prevenção.
        if opcao == "1":
            mostrar_orientacoes()

        # Opção 2: canais de denúncia.
        elif opcao == "2":
            mostrar_menu_denuncia()

        # Opção 3: mini-game.
        elif opcao == "3":

            # Executa o quiz e recebe o resultado final.
            resultado = iniciar_quiz(jogador)

            # Atualiza o ranking local com o resultado do jogador.
            atualizar_ranking(resultado)

        # Opção 4: informações sobre a campanha.
        elif opcao == "4":
            mostrar_campanha()

        # Opção 5: ranking.
        elif opcao == "5":
            exibir_ranking()

        # Opção 6: novo jogador.
        elif opcao == "6":
            jogador = cadastrar_jogador()
            pausar("\nNovo jogador cadastrado. Pressione ENTER para voltar ao menu...")

        # Opção 7: encerrar missão.
        elif opcao == "7":
            encerrar_sistema()
            break


# Este bloco garante que o programa só execute automaticamente quando rodarmos main.py diretamente.
if __name__ == "__main__":
    main()
