"""
Arquivo: cadastro_usuario.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: cadastrar o jogador antes do mini-game começar.

Este arquivo aproveita a ideia original do grupo:
- pedir nome;
- pedir idade;
- perguntar se possui filhos;
- perguntar se convive com crianças.

A mudança principal foi transformar o código solto em função.
Isso permite que o main.py chame o cadastro no momento certo.
"""

# Importa funções auxiliares para validar respostas e organizar a tela.
from utilitarios import limpar_tela, linha, ler_opcao


def ler_idade():
    """Lê a idade do jogador e garante que seja um número inteiro válido."""

    # O laço continua até o usuário digitar uma idade válida.
    while True:

        # Lê a idade como texto para evitar erro caso a pessoa digite letras.
        idade_texto = input("Digite sua idade: ").strip()

        # isdigit() verifica se o texto contém apenas números.
        if idade_texto.isdigit():

            # Converte o texto para inteiro após validar que só tem números.
            idade = int(idade_texto)

            # Garante que a idade esteja em uma faixa aceitável para o sistema.
            if 1 <= idade <= 120:
                return idade

        # Mensagem exibida quando a idade não passa nas validações.
        print("Idade inválida. Digite apenas números, por exemplo: 16")


def cadastrar_jogador():
    """Cadastra o jogador e retorna um dicionário com seus dados."""

    # Limpa a tela para deixar o cadastro mais organizado.
    limpar_tela()

    # Cabeçalho do cadastro.
    linha()
    print("CADASTRO DO JOGADOR".center(60))
    linha()

    # Lê o nome e remove espaços extras.
    nome = input("Digite seu nome: ").strip()

    # Se o usuário não digitar nome, o sistema usa um nome padrão.
    if nome == "":
        nome = "Guardião Anônimo"

    # Lê a idade usando uma função própria para evitar erro com letras.
    idade = ler_idade()

    # Pergunta se possui filhos, aceitando apenas S ou N.
    tem_filhos = ler_opcao("Você possui filhos? (S/N): ", ["S", "N"])

    # Por padrão, considera que a pessoa não convive com crianças.
    convive_criancas = "N"

    # Se a pessoa não tem filhos, pergunta se ela convive com crianças.
    if tem_filhos == "N":
        convive_criancas = ler_opcao("Você convive com crianças? (S/N): ", ["S", "N"])

    # Define o grupo do jogador de acordo com a idade.
    if idade < 18:
        grupo = "Crianças e Adolescentes"
    else:
        grupo = "Adultos e Responsáveis"

    # Cria um dicionário com todos os dados do jogador.
    jogador = {
        "nome": nome,
        "idade": idade,
        "tem_filhos": tem_filhos,
        "convive_criancas": convive_criancas,
        "grupo": grupo
    }

    # Confirma o cadastro na tela.
    print("\nCadastro realizado com sucesso!")
    print(f"Jogador: {jogador['nome']}")
    print(f"Grupo: {jogador['grupo']}")

    # Retorna o dicionário para ser usado no restante do sistema.
    return jogador
