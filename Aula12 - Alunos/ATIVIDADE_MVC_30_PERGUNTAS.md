# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Bernardo Magalhães Santos (TMJ Janaina)
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

H:\Python\ETAPA_2\Aula12 - Alunos\models

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

streamflix.db

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

base.py = ModeloBase (1)      filme_favorito.py = FilmeFavorito (1)      historico_busca.py = HistoricoBusca (1)      TOTAL = 3

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Herdam da Base.py(ModeloBase(db.Model)) id - data_criacao - data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

__tablename__ serve para inicializar a tabela filmes_favoritos

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id. Sim, unique=True

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Ele adiciona o filme à lista de favoritos. Se já existir ele atualiza a lista

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

HistoricoBusca.py, def ultimas(cls, limite=8):

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

só alguns campos espelhados, titulo, poster_path, nota e ano

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

"ModeloBase", "FilmeFavorito", "HistoricoBusca". Pois não precisa de todas as inforações.
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

Existem 3 blueprints + o inicializador
dashboard_controller.py, favoritos_controller.py e o filmes_controller.py como blueprints e o inicializador, __init__.py

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

A rota está no arquivo filmes_controller.py, o nome da função que responde a essa url é (def melhores:...)

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

API e Service

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

O controller é o filme_controller.py, o model é o HistoricoBusca

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

O método logicamente é o POST (Envio), A URL é: /adicionar/550

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Se a API não encontrar que é equivalente ao retorno none, a página redireciona para a página de filmes populares

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

Os Blueprints são registrados no arquivo de inicialização do Flask, o arquivo é o __init__.py.

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

O controller que cuida da página é o dashboard_controller.py, as variáveis que ele envia para a página inicial, vulgo index.html são: populares, melhores, total_favoritos, historico e modo_demo

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

A pasta dada anteriormente na pergunta é um controller, pois ele é o cérebro da página, faz as requisições e toda a coisa funcionar, não é model pois é para instanciar classes no projeto, e view para retornar as telas e os arquivos estáticos do projeto

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

H:\_python\flask\Aula12 - Alunos\views\templates\

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

O template base está dentro da pasta informada anteriormente, o nome do arquivo é layout.html, e eles fazem a "importação" deste layout com o seguinte comando:
{% extends "layout.html" %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

href="{{ url_for('dashboard.index') }}" StreamFlix
href="{{ url_for('filmes.populares') }}" Populares
href="{{ url_for('filmes.melhores') }}" Melhores
href="{{ url_for('filmes.buscar') }}" Buscar
href="{{ url_for('favoritos.listar') }}" Favoritos

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

O arquivo HTML que apresenta a seguinte sessão dada na questão é o detalhe.html. A variável streaming vem de algum lugar deste projeto.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

É um componente vulgo pedaço reutilizável, os arquivos que incluem este pedaço são: buscar.html, lista.html e index.html com o comando {% include "filmes/_card.html" %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

Ele sabe a partir de uma verificação condicional -> if e a variável que faz a verificação é favorito

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

O CSS do site está no seguinte diretório H:\_python\flask\Aula12 - Alunos\views\static\css\style.css, ele realiza a importação a partir de um url_for com a inclusão do caminho static + a pasta de CSS com o arquivo style.css em anexo

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

O loop que percorre os registros é o for -> para fav em favoritos, os campos são título, ano e data de criação

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

O modo demo acredito eu que seja para caso quando não houver uma chave API disponível para o projeto, ou caso tenha alguma limitação que faça com que o site deixe de responder corretamente, o que disponibiliza é o layout.html

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.


---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
