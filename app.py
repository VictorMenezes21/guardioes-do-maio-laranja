"""
Arquivo: app.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função: rodar a versão web do projeto usando Flask.

Por que criar este arquivo?
- O projeto original estava funcionando no terminal.
- A interface enviada está em HTML/CSS.
- Para juntar Python + interface, usamos Flask como ponte entre o backend e as telas.

Como executar:
1. Instalar Flask: pip install -r requirements.txt
2. Rodar: python app.py
3. Abrir no navegador: http://127.0.0.1:5000
"""

# Importa o módulo time para controlar o cronômetro do quiz.
import time

# Importa Flask e recursos usados para criar páginas, redirecionamentos e sessão.
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

# Importa perguntas e pontuação do projeto original.
from perguntas import obter_perguntas_por_grupo, calcular_pontuacao_maxima, PONTOS_POR_NIVEL

# Importa funções do ranking local em JSON.
from ranking import atualizar_ranking, obter_ranking_formatado

# Importa função que converte segundos em texto amigável.
from utilitarios import converter_tempo


# Cria a aplicação Flask.
app = Flask(__name__)

# Chave usada pelo Flask para guardar dados temporários na sessão do navegador.
# Para projeto acadêmico/local, pode ser simples. Em sistema real, seria uma chave secreta forte.
app.secret_key = "pique-eca-guardioes-maio-laranja"


# Conteúdo da campanha, mantendo a ideia e o texto bonito do arquivo do grupo.
CAMPANHA = {
    "titulo": "Campanha Maio Laranja",
    "icone": "🧡",
    "subtitulo": "Informar, orientar e proteger.",
    "blocos": [
        {
            "titulo": "🌼 O que é o Maio Laranja?",
            "texto": "O Maio Laranja é uma campanha nacional de conscientização e combate ao abuso e à exploração sexual de crianças e adolescentes."
        },
        {
            "titulo": "📅 Por que o dia 18 de maio é importante?",
            "texto": "O dia 18 de maio é lembrado como o Dia Nacional de Combate ao Abuso e à Exploração Sexual de Crianças e Adolescentes."
        },
        {
            "titulo": "🎯 Objetivos da campanha",
            "itens": [
                "Informar a população sobre o tema.",
                "Incentivar a prevenção.",
                "Estimular denúncias responsáveis.",
                "Fortalecer a rede de proteção.",
                "Garantir os direitos das crianças e adolescentes."
            ]
        },
        {
            "titulo": "🛡️ Mensagem principal",
            "texto": "Toda criança merece crescer com segurança, respeito e dignidade. A conscientização é uma das principais ferramentas de prevenção."
        }
    ]
}


# Conteúdo das orientações, adaptado do arquivo orientacoes_e_campanha.py.
ORIENTACOES = {
    "titulo": "Orientações importantes",
    "icone": "🛡️",
    "subtitulo": "Proteção começa com informação e diálogo.",
    "blocos": [
        {
            "titulo": "👦👧 Crianças e adolescentes têm direito à proteção",
            "itens": [
                "Seu corpo é seu e ninguém pode tocar em você sem sua permissão.",
                "Caso alguém faça você se sentir desconfortável, com medo ou ameaçado, procure ajuda imediatamente.",
                "Nunca guarde segredos que causem tristeza, medo ou insegurança.",
                "Converse com pais, responsáveis, professores ou outro adulto de confiança.",
                "Na internet, nunca compartilhe informações pessoais com desconhecidos.",
                "Pedir ajuda é um ato de coragem."
            ]
        },
        {
            "titulo": "👨‍👩‍👧 Orientações para pais e responsáveis",
            "itens": [
                "Mantenha diálogo constante com seus filhos.",
                "Demonstre interesse pela rotina, amizades e atividades realizadas por eles.",
                "Oriente sobre segurança na internet e redes sociais.",
                "Observe mudanças repentinas de comportamento, isolamento ou medo excessivo.",
                "Escute sem julgar e acolha qualquer relato de desconforto ou violência.",
                "Em caso de suspeita, não ignore os sinais. Procure ajuda especializada."
            ]
        },
        {
            "titulo": "🧡 Mensagem final",
            "texto": "Proteger é um ato de amor. Seja um Guardião da Infância: sua atitude pode fazer a diferença."
        }
    ]
}


# Canais de denúncia mantendo os dados do arquivo canais_denuncias.py.
CANAIS_DENUNCIA = [
    {
        "nome": "Disque 100",
        "numero": "0800 55 0140",
        "funcao": "Denúncia anônima de abuso sexual, maus-tratos e exploração",
        "disponibilidade": "24h, todos os dias"
    },
    {
        "nome": "Polícia Militar",
        "numero": "190",
        "funcao": "Emergência policial",
        "disponibilidade": "24h, todos os dias"
    },
    {
        "nome": "Conselho Tutelar",
        "numero": "Consulte sua cidade",
        "funcao": "Proteção e orientação à criança",
        "disponibilidade": "Horário comercial"
    },
    {
        "nome": "Ligue 180",
        "numero": "180",
        "funcao": "Atendimento à mulher e à criança",
        "disponibilidade": "24h, todos os dias"
    },
    {
        "nome": "Samu",
        "numero": "192",
        "funcao": "Emergência médica",
        "disponibilidade": "24h, todos os dias"
    }
]


def jogador_logado():
    """Verifica se existe um jogador cadastrado na sessão atual."""

    # A sessão guarda dados temporários do navegador enquanto a pessoa usa o sistema.
    return "jogador" in session


def obter_jogador():
    """Retorna o jogador salvo na sessão."""

    # get evita erro caso a chave ainda não exista.
    return session.get("jogador")


def definir_grupo_por_idade(idade):
    """Define se o jogador entra no grupo de menores ou adultos."""

    # Menores de 18 anos recebem perguntas de crianças/adolescentes.
    if idade < 18:
        return "Crianças e Adolescentes"

    # Maiores ou iguais a 18 anos recebem perguntas de adultos/responsáveis.
    return "Adultos e Responsáveis"


@app.route("/")
def abertura():
    """Mostra a tela inicial do projeto."""

    # Renderiza a página inicial inspirada na interface enviada.
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    """Mostra e processa o cadastro do jogador."""

    # Se o usuário enviou o formulário, processa os dados.
    if request.method == "POST":
        # Captura o nome digitado; se vier vazio, usa um nome padrão.
        nome = request.form.get("nome", "").strip() or "Guardião Anônimo"

        # Captura idade como texto para validar antes de converter.
        idade_texto = request.form.get("idade", "").strip()

        # Valida se idade contém apenas números.
        if not idade_texto.isdigit():
            return render_template("cadastro.html", erro="Digite uma idade válida usando apenas números.")

        # Converte idade para inteiro após validar.
        idade = int(idade_texto)

        # Garante uma faixa de idade aceitável.
        if idade < 1 or idade > 120:
            return render_template("cadastro.html", erro="Digite uma idade entre 1 e 120 anos.")

        # Lê as respostas adicionais do cadastro.
        tem_filhos = request.form.get("tem_filhos", "N")
        convive_criancas = request.form.get("convive_criancas", "N")

        # Define o grupo do jogador de acordo com a idade.
        grupo = definir_grupo_por_idade(idade)

        # Salva o jogador na sessão do navegador.
        session["jogador"] = {
            "nome": nome,
            "idade": idade,
            "tem_filhos": tem_filhos,
            "convive_criancas": convive_criancas,
            "grupo": grupo
        }

        # Limpa dados antigos de quiz, caso outro jogador use o mesmo navegador.
        session.pop("quiz", None)
        session.pop("resultado", None)
        session.pop("resultado_salvo", None)

        # Depois do cadastro, manda para o menu principal.
        return redirect(url_for("menu"))

    # Se for GET, apenas mostra o formulário.
    return render_template("cadastro.html")


@app.route("/menu")
def menu():
    """Mostra o menu principal da versão web."""

    # Se não houver jogador cadastrado, manda para o cadastro.
    if not jogador_logado():
        return redirect(url_for("cadastro"))

    # Renderiza o menu com os dados do jogador.
    return render_template("menu.html", jogador=obter_jogador())


@app.route("/campanha")
def campanha():
    """Mostra as informações sobre a campanha."""

    return render_template("conteudo.html", conteudo=CAMPANHA)


@app.route("/orientacoes")
def orientacoes():
    """Mostra as orientações de prevenção."""

    return render_template("conteudo.html", conteudo=ORIENTACOES)


@app.route("/denuncias")
def denuncias():
    """Mostra os canais oficiais de denúncia."""

    return render_template("denuncias.html", canais=CANAIS_DENUNCIA)


@app.route("/quiz/iniciar")
def iniciar_quiz_web():
    """Prepara o quiz para o jogador atual."""

    # Se não existir jogador, não tem como iniciar quiz.
    if not jogador_logado():
        return redirect(url_for("cadastro"))

    # Busca o jogador salvo na sessão.
    jogador = obter_jogador()

    # Busca as perguntas de acordo com o grupo do jogador.
    perguntas = obter_perguntas_por_grupo(jogador["grupo"])

    # Salva o estado inicial do quiz na sessão.
    session["quiz"] = {
        "indice": 0,
        "pontuacao": 0,
        "acertos": 0,
        "erros": 0,
        "inicio": time.time(),
        "pontuacao_maxima": calcular_pontuacao_maxima(perguntas)
    }

    # Remove resultado antigo, se existir.
    session.pop("resultado", None)
    session.pop("resultado_salvo", None)

    # Direciona para a primeira pergunta.
    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    """Mostra a pergunta atual do quiz."""

    # Se não tiver jogador ou quiz iniciado, redireciona para o local certo.
    if not jogador_logado():
        return redirect(url_for("cadastro"))

    if "quiz" not in session:
        return redirect(url_for("iniciar_quiz_web"))

    # Busca jogador e estado atual do quiz.
    jogador = obter_jogador()
    estado_quiz = session["quiz"]

    # Busca as perguntas do grupo do jogador.
    perguntas = obter_perguntas_por_grupo(jogador["grupo"])

    # Identifica a pergunta atual.
    indice = estado_quiz["indice"]

    # Se o índice passar do final, finaliza o quiz.
    if indice >= len(perguntas):
        return redirect(url_for("finalizar_quiz"))

    # Calcula o tempo decorrido para mostrar o cronômetro na tela.
    tempo_decorrido = int(time.time() - estado_quiz["inicio"])

    # Renderiza a tela de pergunta.
    return render_template(
        "quiz.html",
        jogador=jogador,
        pergunta=perguntas[indice],
        numero=indice + 1,
        total=len(perguntas),
        tempo_decorrido=tempo_decorrido,
        pontos_nivel=PONTOS_POR_NIVEL[perguntas[indice]["nivel"]]
    )


@app.route("/quiz/responder", methods=["POST"])
def responder_quiz():
    """Recebe a resposta do jogador e prepara a próxima etapa."""

    # Proteção para evitar resposta sem quiz iniciado.
    if not jogador_logado() or "quiz" not in session:
        return redirect(url_for("cadastro"))

    # Busca jogador e estado do quiz.
    jogador = obter_jogador()
    estado_quiz = session["quiz"]

    # Busca perguntas do grupo.
    perguntas = obter_perguntas_por_grupo(jogador["grupo"])

    # Descobre qual pergunta está sendo respondida.
    indice = estado_quiz["indice"]
    pergunta = perguntas[indice]

    # Captura a alternativa escolhida pelo jogador.
    resposta_usuario = request.form.get("resposta", "").strip().upper()

    # Verifica se a resposta está correta.
    acertou = resposta_usuario == pergunta["resposta"]

    # Se acertou, soma pontos e acerto.
    if acertou:
        estado_quiz["pontuacao"] += PONTOS_POR_NIVEL[pergunta["nivel"]]
        estado_quiz["acertos"] += 1
    else:
        estado_quiz["erros"] += 1

    # Avança para a próxima pergunta.
    estado_quiz["indice"] += 1

    # Salva o estado atualizado de volta na sessão.
    session["quiz"] = estado_quiz

    # Verifica se ainda existem perguntas depois desta.
    finalizado = estado_quiz["indice"] >= len(perguntas)

    # Renderiza uma tela de feedback antes da próxima pergunta ou resultado.
    return render_template(
        "feedback.html",
        acertou=acertou,
        pergunta=pergunta,
        resposta_usuario=resposta_usuario,
        finalizado=finalizado
    )


@app.route("/quiz/finalizar")
def finalizar_quiz():
    """Finaliza a partida, calcula o resultado e atualiza o ranking."""

    # Proteção para evitar finalização sem jogador/quiz.
    if not jogador_logado() or "quiz" not in session:
        return redirect(url_for("cadastro"))

    # Busca jogador e dados do quiz.
    jogador = obter_jogador()
    estado_quiz = session["quiz"]

    # Calcula tempo total da partida.
    tempo_total = time.time() - estado_quiz["inicio"]

    # Calcula aproveitamento em porcentagem.
    total_perguntas = estado_quiz["acertos"] + estado_quiz["erros"]
    aproveitamento = (estado_quiz["acertos"] / total_perguntas) * 100 if total_perguntas > 0 else 0

    # Monta resultado final da partida.
    resultado = {
        "nome": jogador["nome"],
        "idade": jogador["idade"],
        "grupo": jogador["grupo"],
        "pontuacao": estado_quiz["pontuacao"],
        "pontuacao_maxima": estado_quiz["pontuacao_maxima"],
        "acertos": estado_quiz["acertos"],
        "erros": estado_quiz["erros"],
        "aproveitamento": aproveitamento,
        "tempo_segundos": tempo_total,
        "tempo_formatado": converter_tempo(tempo_total)
    }

    # Atualiza o ranking apenas uma vez por partida.
    if not session.get("resultado_salvo"):
        atualizar_ranking(resultado)
        session["resultado_salvo"] = True

    # Salva resultado na sessão para poder exibir novamente.
    session["resultado"] = resultado

    # Remove o estado do quiz para evitar duplicidade.
    session.pop("quiz", None)

    # Renderiza a página final.
    return render_template("resultado.html", resultado=resultado)


@app.route("/ranking")
def ranking_web():
    """Mostra a página de ranking com atualização automática."""

    # Renderiza a página. Os dados vêm pela API para atualizar sem F5.
    return render_template("ranking.html")


@app.route("/api/ranking")
def api_ranking():
    """Retorna o ranking em JSON para a tela web atualizar automaticamente."""

    # jsonify transforma a lista Python em resposta JSON para o navegador.
    return jsonify(obter_ranking_formatado())


@app.route("/novo-jogador")
def novo_jogador():
    """Limpa os dados da sessão para cadastrar outra pessoa."""

    # Limpa a sessão atual do navegador.
    session.clear()

    # Redireciona para o cadastro.
    return redirect(url_for("cadastro"))


# Executa o servidor Flask apenas quando este arquivo é rodado diretamente.
if __name__ == "__main__":
    # host 0.0.0.0 permite abrir em outros dispositivos na mesma rede local.
    # Isso ajuda na apresentação se quiser acessar pelo celular usando o IP do notebook.
    app.run(host="0.0.0.0", port=5000, debug=True)
