# Pique ECA — Guardiões do Maio Laranja

Projeto acadêmico desenvolvido em Python com foco em conscientização sobre o Maio Laranja, prevenção ao abuso infantil, direitos da criança e do adolescente e canais de denúncia.

O projeto possui duas formas de execução:

1. **Versão terminal**: roda com `main.py`, mantendo o estilo original do grupo.
2. **Versão web**: roda com `app.py`, integrando a interface visual enviada em HTML/CSS.

---

## Estrutura do projeto

```text
Pique_eca_interface_integrada/
│
├── app.py                         # Versão web com Flask
├── main.py                        # Versão terminal
├── menu.py                        # Abertura e menu terminal
├── cadastro_usuario.py            # Cadastro terminal
├── orientacoes_e_campanha.py      # Textos de campanha e orientações terminal
├── canais_denuncias.py            # Canais de denúncia terminal
├── perguntas.py                   # Perguntas do quiz
├── quiz.py                        # Quiz terminal
├── ranking.py                     # Ranking local com JSON
├── utilitarios.py                 # Funções auxiliares
├── requirements.txt               # Dependências da versão web
├── data/
│   └── ranking.json               # Ranking salvo localmente
├── templates/                     # Telas HTML da versão web
├── static/
│   └── style.css                  # Estilo visual da interface
└── docs/interface_referencia/     # Referências visuais da interface enviada
```

---

## Como rodar a versão terminal

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

---

## Como rodar a versão web

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rode o servidor:

```bash
python app.py
```

Abra no navegador:

```text
http://127.0.0.1:5000
```

Para acessar pelo celular na mesma rede, use o IP do computador que está rodando o Flask, por exemplo:

```text
http://192.168.0.10:5000
```

---

## Funcionalidades

- Cadastro de jogador.
- Separação por faixa etária.
- Menu principal.
- Informações sobre a campanha Maio Laranja.
- Orientações de prevenção.
- Canais de denúncia.
- Mini-game com perguntas.
- Pontuação por dificuldade.
- Cronômetro do quiz.
- Ranking local salvo em JSON.
- Ranking web com atualização automática.

---

## Conceitos usados

- Variáveis.
- Condicionais.
- Laços de repetição.
- Listas.
- Dicionários.
- Funções.
- Manipulação de arquivo JSON.
- Estruturação de projeto.
- Introdução a rotas web com Flask.
- HTML, CSS e JavaScript simples.
