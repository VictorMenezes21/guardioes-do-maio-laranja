# Relatório de Mudanças — Pique ECA

Este arquivo resume as mudanças feitas no projeto e traz um roteiro simples para cada integrante explicar sua parte durante a apresentação.

A ideia principal da organização foi manter o trabalho original do grupo, mas transformar as partes separadas em um sistema único, funcionando pelo arquivo `main.py`.

---

# Visão geral do projeto

O projeto é um mini-game educativo sobre o Maio Laranja, com foco em conscientização, prevenção, canais de denúncia e perguntas sobre o tema.

O sistema possui:

- tela de abertura;
- cadastro do jogador;
- menu principal;
- orientações e informações sobre a campanha;
- canais de denúncia;
- mini-game com perguntas por faixa etária;
- cronômetro interno do quiz;
- pontuação por dificuldade;
- ranking local salvo em JSON;
- mensagem final de encerramento.

---

# Por que a integração foi necessária?

Antes, o grupo já tinha várias partes importantes prontas, mas elas estavam separadas. Ou seja, existia menu, cadastro, perguntas, orientações e canais de denúncia, mas ainda faltava um arquivo principal chamando tudo na ordem correta.

A integração foi feita para que o programa funcionasse como uma aplicação completa:

```text
Abertura
   ↓
Cadastro do jogador
   ↓
Menu principal
   ↓
Opções do sistema
   ↓
Quiz / Orientações / Denúncias / Ranking
   ↓
Encerramento
```

---

# Ordem sugerida para apresentação

Esta é a ordem mais fácil para explicar o sistema:

1. `main.py` — fluxo principal do sistema;
2. `utilitarios.py` — funções de apoio usadas pelo sistema;
3. `menu.py` — abertura e menu principal;
4. `cadastro_usuario.py` — cadastro do jogador;
5. `orientacoes_e_campanha.py` — parte educativa;
6. `canais_denuncias.py` — canais de denúncia;
7. `perguntas.py` — banco de perguntas do quiz;
8. `quiz.py` — funcionamento do mini-game;
9. `ranking.py` — ranking local em JSON;
10. `README.md` e `RELATORIO_MUDANCAS.md` — documentação.

---

# Roteiro por arquivo

## 1. main.py — Victor

### Função do arquivo

O `main.py` é o arquivo principal do projeto. Ele é responsável por iniciar o sistema e conectar todas as outras partes.

### O que ele faz

- mostra a abertura do projeto;
- chama o cadastro do jogador;
- mantém o menu funcionando dentro de um laço `while`;
- lê a opção escolhida pelo usuário;
- chama a função correta de acordo com a opção;
- envia o resultado do quiz para o ranking;
- permite cadastrar um novo jogador;
- encerra o sistema com a mensagem final.

### Roteiro para falar

> O `main.py` é o arquivo que liga todas as partes do projeto. Ele funciona como o centro do sistema. Primeiro ele mostra a abertura, depois chama o cadastro do jogador e, em seguida, mantém o menu principal rodando. Conforme o usuário escolhe uma opção, o `main.py` chama o arquivo responsável por aquela funcionalidade, como orientações, denúncias, quiz ou ranking. Isso foi feito para que cada parte do projeto ficasse separada, mas funcionando em conjunto.

### Conceitos usados

- importação de funções;
- função principal `main()`;
- laço de repetição `while`;
- estruturas condicionais `if`, `elif` e `else`;
- integração entre arquivos.

---

## 2. utilitarios.py — Victor

### Função do arquivo

O `utilitarios.py` guarda funções pequenas que são usadas em várias partes do sistema.

### O que ele faz

- limpa a tela do terminal;
- cria pausas com `input`;
- imprime linhas decorativas;
- valida opções digitadas pelo usuário;
- converte o tempo do quiz de segundos para um formato mais fácil de ler.

### Roteiro para falar

> O `utilitarios.py` foi criado para evitar repetição de código. Em vez de escrever a mesma lógica várias vezes em arquivos diferentes, colocamos funções auxiliares em um único lugar. Por exemplo, a função de pausar o sistema, limpar a tela e validar opções pode ser usada pelo menu, pelo quiz, pelo ranking e por outras partes. A função `converter_tempo()` transforma o tempo do quiz, que é calculado em segundos, em uma mensagem mais legível para o usuário.

### Conceitos usados

- funções;
- reaproveitamento de código;
- validação de entrada;
- uso dos módulos `os` e `time`.

---

## 3. menu.py — Responsável pelo Menu Principal

### Função do arquivo

O `menu.py` exibe a abertura do projeto e o menu principal do sistema.

### O que ele faz

- mostra a tela inicial do projeto;
- exibe uma mensagem de boas-vindas;
- mostra o nome do jogador atual;
- mostra o grupo do jogador;
- apresenta as opções do sistema.

### Roteiro para falar

> Minha parte foi organizar o menu principal do sistema. O menu mostra as opções que o usuário pode acessar, como orientações, canais de denúncia, mini-game, informações da campanha, ranking, novo jogador e encerramento. A abertura foi mantida com uma mensagem mais chamativa para dar a ideia de mini-game. O menu não executa as opções sozinho; ele apenas mostra as opções. Quem decide o que fazer com a escolha do usuário é o `main.py`.

### O que mudou

Antes o menu era mais isolado. Agora ele foi transformado em funções para ser chamado pelo `main.py`.

### Conceitos usados

- funções;
- `print` para exibição no terminal;
- organização visual da interface.

---

## 4. cadastro_usuario.py — Responsável pelo Cadastro

### Função do arquivo

O `cadastro_usuario.py` cadastra o jogador antes do início do mini-game.

### O que ele faz

- pede o nome do jogador;
- pede a idade;
- pergunta se possui filhos;
- pergunta se convive com crianças;
- define automaticamente o grupo do jogador.

### Roteiro para falar

> Minha parte foi o cadastro do jogador. O sistema pede informações simples, como nome e idade. A idade é importante porque define qual grupo de perguntas será usado no quiz. Se a pessoa tiver menos de 18 anos, ela entra no grupo de crianças e adolescentes. Se tiver 18 anos ou mais, entra no grupo de adultos e responsáveis. No final, os dados são guardados em um dicionário e enviados para o restante do sistema.

### O que mudou

O cadastro foi organizado em função e passou a devolver os dados do jogador para o `main.py`.

### Conceitos usados

- variáveis;
- `input`;
- validação de idade;
- condicionais;
- dicionário.

---

## 5. orientacoes_e_campanha.py — Responsável por Orientações e Informações

### Função do arquivo

O `orientacoes_e_campanha.py` apresenta a parte educativa do projeto.

### O que ele faz

- explica o que é o Maio Laranja;
- mostra orientações de prevenção;
- orienta crianças, adolescentes, pais e responsáveis;
- reforça a importância da denúncia;
- apresenta mensagens educativas no terminal.

### Roteiro para falar

> Minha parte foi a área de informações e orientações sobre a campanha. Esse arquivo mostra textos educativos sobre o Maio Laranja, explicando a importância da prevenção, da atenção aos sinais de risco e da denúncia responsável. Essa parte é importante porque o projeto não é apenas um jogo; ele também tem o objetivo de conscientizar. As mensagens foram mantidas com uma linguagem mais acolhedora para combinar com o tema.

### O que mudou

Os textos foram preservados, mas organizados em funções para que o menu principal consiga chamar cada parte no momento certo.

### Conceitos usados

- funções;
- exibição de texto;
- organização de conteúdo educativo;
- pausa para leitura do usuário.

---

## 6. canais_denuncias.py — Jeniffer

### Função do arquivo

O `canais_denuncias.py` mostra os canais oficiais e formas de buscar ajuda.

### O que ele faz

- apresenta o Disque 100;
- mostra o número 190 para emergência;
- cita o Conselho Tutelar;
- cita a Polícia Civil;
- organiza os canais de denúncia de forma acessível.

### Roteiro para falar

> Minha parte foi organizar os canais de denúncia. Essa função mostra ao usuário onde buscar ajuda em caso de suspeita ou situação de risco. O principal canal apresentado é o Disque 100, que recebe denúncias de violações de direitos humanos. Também aparecem outros canais, como Polícia Militar, Conselho Tutelar e Polícia Civil. Essa parte é importante porque o projeto não deve apenas informar sobre o problema, mas também mostrar caminhos corretos para denunciar.

### O que mudou

As mensagens originais foram mantidas, mas o arquivo foi ajustado para funcionar junto com o `main.py`.

### Conceitos usados

- funções;
- `print`;
- organização de informações;
- menu informativo.

---

## 7. perguntas.py — Responsáveis pelas Perguntas

### Função do arquivo

O `perguntas.py` armazena as perguntas usadas no mini-game.

### O que ele faz

- guarda perguntas para menores de idade;
- guarda perguntas para maiores de idade;
- separa perguntas por dificuldade;
- guarda alternativas;
- guarda resposta correta;
- guarda justificativa;
- informa a pontuação de cada nível.

### Roteiro para falar

> Nossa parte foi organizar as perguntas do quiz. As perguntas foram separadas em dois grupos: menores de idade e maiores de idade. Cada pergunta possui nível de dificuldade, alternativas, resposta correta e justificativa. Usamos listas e dicionários porque isso deixa o código mais organizado. A lista guarda várias perguntas e cada pergunta é um dicionário com suas informações. Assim, o `quiz.py` consegue percorrer as perguntas automaticamente.

### O que mudou

As perguntas criadas pelo grupo foram mantidas como base, mas foram organizadas em listas de dicionários para funcionar com o mini-game refinado.

### Conceitos usados

- listas;
- dicionários;
- strings;
- funções;
- pontuação por dificuldade.

---

## 8. quiz.py — Victor

### Função do arquivo

O `quiz.py` executa o mini-game de perguntas e respostas.

### O que ele faz

- busca as perguntas de acordo com o grupo do jogador;
- mostra cada pergunta e suas alternativas;
- lê a resposta do usuário;
- verifica se a resposta está correta;
- soma a pontuação de acordo com a dificuldade;
- mostra justificativa após cada pergunta;
- calcula acertos, erros e aproveitamento;
- mede o tempo total do jogador;
- devolve o resultado completo para o ranking.

### Roteiro para falar

> O `quiz.py` é a parte que executa o mini-game. Ele recebe o jogador cadastrado, identifica o grupo dele e busca as perguntas corretas no arquivo `perguntas.py`. Durante o quiz, o sistema mostra as perguntas, valida as respostas e soma pontos conforme a dificuldade. Também usamos um cronômetro interno com o módulo `time`, que marca o início e o fim do quiz. No final, o arquivo gera um resultado completo com nome, grupo, pontuação, acertos, erros, aproveitamento e tempo.

### O que mudou

O quiz foi integrado ao cadastro e ao ranking. Antes ele funcionava mais isolado; agora ele devolve um resultado para ser salvo no ranking.

### Conceitos usados

- `for`;
- `if` e `else`;
- variáveis acumuladoras;
- listas e dicionários;
- funções;
- módulo `time`;
- retorno de dados com `return`.

---

## 9. ranking.py — Victor

### Função do arquivo

O `ranking.py` controla o ranking local do mini-game.

### O que ele faz

- cria o arquivo `ranking.json` se ele ainda não existir;
- carrega os resultados salvos;
- salva novos resultados;
- ordena os jogadores por maior pontuação;
- usa menor tempo como critério de desempate;
- mostra o TOP 10 jogadores;
- define medalhas pela posição no ranking.

### Roteiro para falar

> O `ranking.py` foi criado para salvar a pontuação dos jogadores mesmo depois que o programa fecha. Para isso usamos um arquivo JSON, que é simples e não precisa instalar banco de dados. Quando alguém termina o quiz, o resultado é salvo no arquivo `data/ranking.json`. O ranking é ordenado primeiro pela maior pontuação e, em caso de empate, pelo menor tempo. As medalhas não ficam salvas no JSON, porque elas dependem da posição atual. Então o primeiro lugar aparece como Ouro, o segundo como Prata e o terceiro como Bronze.

### O que mudou

Foi criado um ranking persistente usando JSON. A lógica das medalhas também foi corrigida para depender da colocação atual, e não de um valor fixo salvo no arquivo.

### Conceitos usados

- listas;
- dicionários;
- arquivos JSON;
- ordenação com `sorted`;
- funções;
- critérios de desempate.

---

## 10. README.md — Victor

### Função do arquivo

O `README.md` explica o projeto para quem acessar o repositório no GitHub.

### Roteiro para falar

> O README é a documentação inicial do projeto no GitHub. Ele explica o objetivo do sistema, como executar o programa, quais arquivos existem e quais conceitos de lógica foram usados. Isso ajuda tanto na apresentação quanto na organização do repositório.

---

## 11. RELATORIO_MUDANCAS.md — Victor

### Função do arquivo

O `RELATORIO_MUDANCAS.md` explica as mudanças feitas na integração e ajuda cada integrante a entender sua parte.

### Roteiro para falar

> O relatório de mudanças foi criado para registrar o que foi alterado no projeto e por quê. Ele também serve como guia para cada integrante explicar seu arquivo durante a apresentação.

---

# Resumo para o grupo

Cada integrante não precisa decorar o código inteiro. O mais importante é saber explicar:

1. qual arquivo ficou sob sua responsabilidade;
2. qual é a função desse arquivo no sistema;
3. o que foi organizado ou alterado;
4. quais conceitos de lógica aparecem na sua parte;
5. como essa parte se conecta ao `main.py`.

---

# Frase geral para apresentação

> O projeto foi organizado em arquivos separados para facilitar o desenvolvimento em grupo. Cada arquivo ficou responsável por uma parte do sistema, como menu, cadastro, orientações, canais de denúncia, perguntas, quiz e ranking. O `main.py` faz a integração de todas essas partes e permite que o programa funcione como uma aplicação única.

---

# Observação sobre as perguntas

As perguntas usadas no arquivo `perguntas.py` foram mantidas com base no material criado pelo próprio grupo. A principal mudança foi estruturar essas perguntas em listas e dicionários, acrescentando dificuldade, justificativa e pontuação para que funcionassem melhor dentro do mini-game.

---

# Observação sobre o ranking

O ranking é salvo localmente no arquivo `data/ranking.json`. Isso permite que os resultados continuem disponíveis mesmo depois que o sistema é fechado.

A medalha é calculada na hora de exibir o ranking:

```text
1º lugar → Ouro
2º lugar → Prata
3º lugar → Bronze
4º em diante → Participante
```

Essa escolha foi feita porque a posição de cada jogador pode mudar conforme novas pessoas jogam.

---

# Integração com Interface Web

## O que foi adicionado

Foi criada uma versão web do projeto usando `Flask`, mantendo a versão de terminal já existente.

Arquivos adicionados:

```text
app.py
requirements.txt
templates/
static/style.css
docs/interface_referencia/
```

## Por que foi feito assim?

A interface enviada estava em HTML/CSS, mas o projeto principal estava em Python no terminal. Para juntar os dois, foi necessário criar uma ponte entre o Python e as telas. O Flask faz esse papel: ele permite que o Python controle as páginas HTML, receba formulários, processe o quiz e atualize o ranking.

## O que cada arquivo novo faz?

### app.py — Victor

Roteiro de fala:

> O `app.py` é a versão web do nosso projeto. Ele usa Flask para criar as rotas do sistema, como tela inicial, cadastro, menu, campanha, orientações, denúncias, quiz e ranking. Ele reaproveita o `perguntas.py` e o `ranking.py`, então a lógica principal do projeto não foi jogada fora; ela foi adaptada para funcionar com a interface.

Pontos importantes:

- Controla as páginas web.
- Faz o cadastro do jogador.
- Define o grupo pela idade.
- Inicia o quiz.
- Controla o cronômetro.
- Calcula resultado.
- Atualiza o ranking JSON.
- Fornece uma API para o ranking atualizar automaticamente.

### templates/ — Victor

Roteiro de fala:

> A pasta `templates` guarda as telas HTML do projeto web. Cada tela representa uma parte do sistema: abertura, cadastro, menu, conteúdo, denúncias, quiz, feedback, resultado e ranking. Essas páginas usam dados enviados pelo Python através do Flask.

Telas principais:

- `index.html`: abertura.
- `cadastro.html`: cadastro do jogador.
- `menu.html`: menu principal.
- `conteudo.html`: campanha e orientações.
- `denuncias.html`: canais de denúncia.
- `quiz.html`: tela das perguntas.
- `feedback.html`: justificativa após cada resposta.
- `resultado.html`: resultado final.
- `ranking.html`: ranking com atualização automática.

### static/style.css — Victor

Roteiro de fala:

> O `style.css` é responsável pelo visual da versão web. Ele usa cores inspiradas no Maio Laranja, cards, botões, telas responsivas e um estilo parecido com a interface que foi enviada para o grupo.

### requirements.txt — Victor

Roteiro de fala:

> O `requirements.txt` informa qual biblioteca precisa ser instalada para rodar a versão web. Nesse caso, usamos Flask.

### ranking.py — atualizado para terminal e web

Roteiro de fala:

> O `ranking.py` passou a servir tanto para a versão terminal quanto para a versão web. Ele continua salvando os dados em JSON e agora possui uma função que retorna o ranking formatado para ser usado pela interface.

Mudança importante:

- O caminho do `ranking.json` foi ajustado para funcionar mesmo se o projeto for executado de locais diferentes.
- Foi criada a função `obter_ranking_formatado()` para o ranking web.

## Como explicar a versão web na apresentação?

> Além da versão em terminal, também criamos uma versão web para integrar a interface visual ao projeto. Usamos Flask porque ele permite conectar Python com HTML. Assim, o jogador consegue se cadastrar, responder o quiz, ver o tempo, receber feedback e acompanhar o ranking pelo navegador.

## Observação sobre complexidade

A versão terminal continua existindo porque é a versão mais ligada aos conteúdos iniciais de lógica. A versão web é uma melhoria visual e interativa do projeto, mantendo a mesma base de perguntas, pontuação e ranking.
