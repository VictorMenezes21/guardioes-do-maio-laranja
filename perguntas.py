"""
Arquivo: perguntas.py
Projeto: Pique ECA / Guardiões do Maio Laranja
Função do arquivo: armazenar as perguntas do mini-game.

Este arquivo mantém as perguntas criadas originalmente pelo grupo,
mas organiza cada pergunta em dicionários para funcionar com o quiz.py.

Cada pergunta possui:
- nivel: dificuldade da pergunta.
- pergunta: enunciado.
- opcoes: alternativas exibidas ao jogador.
- resposta: letra correta.
- justificativa: explicação educativa exibida após a resposta.
"""

# Pontuação usada pelo quiz de acordo com a dificuldade da pergunta.
PONTOS_POR_NIVEL = {
    "Fácil": 10,
    "Médio": 20,
    "Difícil": 30
}


# =====================================================
# PERGUNTAS PARA MENORES DE IDADE
# =====================================================
# Estas perguntas foram mantidas com base no arquivo original do grupo.
perguntas_menores = [
    {
        "nivel": "Fácil",
        "pergunta": "O que representa a campanha Maio Laranja?",
        "opcoes": [
            "A) Combate ao trabalho infantil",
            "B) Combate ao abuso e à exploração sexual de crianças e adolescentes",
            "C) Combate ao bullying escolar",
            "D) Combate à evasão escolar"
        ],
        "resposta": "B",
        "justificativa": "O Maio Laranja é uma campanha de conscientização, prevenção e combate ao abuso e à exploração sexual de crianças e adolescentes."
    },
    {
        "nivel": "Fácil",
        "pergunta": "Qual número pode ser utilizado para denunciar violações dos direitos das crianças e adolescentes?",
        "opcoes": [
            "A) 180",
            "B) 190",
            "C) 100",
            "D) 193"
        ],
        "resposta": "C",
        "justificativa": "O Disque 100 é um canal utilizado para receber denúncias de violações de direitos humanos, incluindo casos envolvendo crianças e adolescentes."
    },
    {
        "nivel": "Fácil",
        "pergunta": "Segundo o ECA, toda criança tem direito a:",
        "opcoes": [
            "A) Proteção, educação e saúde",
            "B) Trabalhar desde cedo",
            "C) Abandonar a escola",
            "D) Ficar sem acompanhamento familiar"
        ],
        "resposta": "A",
        "justificativa": "O ECA garante direitos fundamentais, como proteção, educação, saúde, respeito e convivência familiar."
    },
    {
        "nivel": "Médio",
        "pergunta": "Se uma criança estiver sofrendo algum tipo de violência, ela deve:",
        "opcoes": [
            "A) Guardar segredo",
            "B) Contar a um adulto de confiança",
            "C) Fugir de casa",
            "D) Não falar com ninguém"
        ],
        "resposta": "B",
        "justificativa": "Ao passar por uma situação de violência ou desconforto, a criança ou adolescente deve procurar um adulto de confiança para receber ajuda."
    },
    {
        "nivel": "Médio",
        "pergunta": "Quem deve proteger as crianças e adolescentes?",
        "opcoes": [
            "A) Apenas os pais",
            "B) Apenas a escola",
            "C) Apenas o governo",
            "D) Família, sociedade e Estado"
        ],
        "resposta": "D",
        "justificativa": "A proteção de crianças e adolescentes é responsabilidade da família, da sociedade e do Estado."
    },
    {
        "nivel": "Médio",
        "pergunta": "O Maio Laranja acontece em qual mês?",
        "opcoes": [
            "A) Março",
            "B) Abril",
            "C) Maio",
            "D) Junho"
        ],
        "resposta": "C",
        "justificativa": "A campanha Maio Laranja acontece durante o mês de maio, com destaque para o dia 18 de maio."
    },
    {
        "nivel": "Difícil",
        "pergunta": "A escola pode ajudar na proteção das crianças?",
        "opcoes": [
            "A) Sim",
            "B) Não",
            "C) Apenas em alguns casos",
            "D) Nunca"
        ],
        "resposta": "A",
        "justificativa": "A escola pode ajudar observando sinais de alerta, acolhendo os alunos e encaminhando situações suspeitas aos órgãos responsáveis."
    },
    {
        "nivel": "Difícil",
        "pergunta": "O abuso infantil deve ser denunciado?",
        "opcoes": [
            "A) Não",
            "B) Apenas pelos pais",
            "C) Sim",
            "D) Apenas pela escola"
        ],
        "resposta": "C",
        "justificativa": "Situações de abuso ou suspeita de violência devem ser denunciadas para que a criança ou adolescente receba proteção."
    },
    {
        "nivel": "Difícil",
        "pergunta": "Qual destes é um direito garantido pelo ECA?",
        "opcoes": [
            "A) Educação",
            "B) Trabalho infantil",
            "C) Violência",
            "D) Exploração"
        ],
        "resposta": "A",
        "justificativa": "A educação é um direito garantido às crianças e adolescentes. Trabalho infantil, violência e exploração não são direitos."
    }
]


# =====================================================
# PERGUNTAS PARA MAIORES DE IDADE
# =====================================================
# Estas perguntas também seguem o arquivo original do grupo.
perguntas_maiores = [
    {
        "nivel": "Fácil",
        "pergunta": "O que significa a sigla ECA?",
        "opcoes": [
            "A) Estatuto da Criança e do Adolescente",
            "B) Escola da Criança Assistida",
            "C) Estatuto de Convivência Adolescente",
            "D) Educação da Criança Assistida"
        ],
        "resposta": "A",
        "justificativa": "ECA significa Estatuto da Criança e do Adolescente, lei que trata dos direitos e da proteção de crianças e adolescentes no Brasil."
    },
    {
        "nivel": "Fácil",
        "pergunta": "Qual é o principal objetivo do Maio Laranja?",
        "opcoes": [
            "A) Promover atividades esportivas",
            "B) Combater o abuso e a exploração sexual infantil",
            "C) Incentivar o turismo",
            "D) Promover campanhas eleitorais"
        ],
        "resposta": "B",
        "justificativa": "O principal objetivo do Maio Laranja é conscientizar a sociedade sobre a prevenção e o combate ao abuso e à exploração sexual infantil."
    },
    {
        "nivel": "Fácil",
        "pergunta": "O dia 18 de maio é lembrado nacionalmente por ser:",
        "opcoes": [
            "A) Dia da Educação",
            "B) Dia Nacional de Combate ao Abuso e à Exploração Sexual de Crianças e Adolescentes",
            "C) Dia da Família",
            "D) Dia dos Direitos Humanos"
        ],
        "resposta": "B",
        "justificativa": "O dia 18 de maio é a data nacional de combate ao abuso e à exploração sexual de crianças e adolescentes."
    },
    {
        "nivel": "Médio",
        "pergunta": "Ao suspeitar de abuso contra uma criança, a atitude mais adequada é:",
        "opcoes": [
            "A) Ignorar por falta de certeza",
            "B) Divulgar nas redes sociais",
            "C) Comunicar aos órgãos competentes",
            "D) Confrontar a vítima"
        ],
        "resposta": "C",
        "justificativa": "Em caso de suspeita, a atitude correta é buscar ajuda e comunicar aos órgãos competentes, evitando exposição da vítima."
    },
    {
        "nivel": "Médio",
        "pergunta": "Segundo o ECA, considera-se criança a pessoa com idade de:",
        "opcoes": [
            "A) Até 10 anos incompletos",
            "B) Até 12 anos incompletos",
            "C) Até 14 anos incompletos",
            "D) Até 16 anos incompletos"
        ],
        "resposta": "B",
        "justificativa": "Segundo o ECA, criança é a pessoa com até 12 anos incompletos. De 12 a 18 anos incompletos, é considerada adolescente."
    },
    {
        "nivel": "Médio",
        "pergunta": "O Disque 100 é um canal destinado a:",
        "opcoes": [
            "A) Solicitação de documentos",
            "B) Denúncias de violações dos direitos humanos",
            "C) Atendimento médico emergencial",
            "D) Registro de boletins escolares"
        ],
        "resposta": "B",
        "justificativa": "O Disque 100 é um canal de denúncia de violações de direitos humanos, incluindo situações envolvendo crianças e adolescentes."
    },
    {
        "nivel": "Difícil",
        "pergunta": "Qual princípio do ECA estabelece prioridade aos direitos das crianças e adolescentes?",
        "opcoes": [
            "A) Livre iniciativa",
            "B) Proteção integral e prioridade absoluta",
            "C) Autonomia econômica",
            "D) Responsabilidade individual"
        ],
        "resposta": "B",
        "justificativa": "O ECA trabalha com a ideia de proteção integral e prioridade absoluta para crianças e adolescentes."
    },
    {
        "nivel": "Difícil",
        "pergunta": "A denúncia ao Disque 100 pode ser feita de forma:",
        "opcoes": [
            "A) Apenas presencial",
            "B) Apenas por advogados",
            "C) Anônima",
            "D) Apenas por familiares"
        ],
        "resposta": "C",
        "justificativa": "O Disque 100 permite denúncias de forma anônima, o que ajuda a proteger quem denuncia."
    },
    {
        "nivel": "Difícil",
        "pergunta": "A exploração sexual de crianças e adolescentes é:",
        "opcoes": [
            "A) Permitida em alguns casos",
            "B) Um crime",
            "C) Uma infração leve",
            "D) Apenas um problema social"
        ],
        "resposta": "B",
        "justificativa": "A exploração sexual de crianças e adolescentes é crime e deve ser denunciada aos órgãos responsáveis."
    }
]


def obter_perguntas_por_grupo(grupo):
    """Retorna a lista de perguntas de acordo com o grupo do jogador."""

    # Se o jogador for menor de idade, o cadastro define este grupo.
    if grupo == "Crianças e Adolescentes":
        return perguntas_menores

    # Caso contrário, o sistema usa as perguntas para adultos e responsáveis.
    return perguntas_maiores


def calcular_pontuacao_maxima(lista_perguntas):
    """Calcula a maior pontuação possível para uma lista de perguntas."""

    # Variável acumuladora que começa em zero.
    total = 0

    # Percorre pergunta por pergunta da lista recebida.
    for pergunta in lista_perguntas:
        # Soma a pontuação correspondente ao nível de dificuldade da pergunta.
        total += PONTOS_POR_NIVEL[pergunta["nivel"]]

    # Retorna a pontuação máxima possível.
    return total
