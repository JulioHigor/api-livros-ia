# API REST de Livros com Inteligência Artificial

API REST desenvolvida em Python com Flask e SQLite para gerenciamento de
um catálogo de livros, implementando operações CRUD e integração com
Inteligência Artificial para recomendação de livros com base nas
preferências do usuário.

> **Projeto exclusivamente para estudo**, desenvolvido para praticar
> conceitos de desenvolvimento backend, APIs REST, bancos de dados,
> integração com serviços externos e Inteligência Artificial.

------------------------------------------------------------------------

## Sobre o projeto

O projeto tem como base o desenvolvimento de uma API REST para
gerenciamento de livros utilizando Flask e SQLite.

A aplicação permite realizar operações de criação, consulta, atualização
e exclusão de livros, utilizando Flask-SQLAlchemy para fazer a
integração entre a aplicação e o banco de dados.

Como extensão da proposta original, o projeto também possui uma
funcionalidade de Inteligência Artificial integrada ao Google Gemini. O
usuário pode informar uma preferência de leitura e a aplicação consulta
o catálogo disponível no banco de dados para que a IA selecione e
recomende o livro mais adequado.

O projeto foi desenvolvido exclusivamente para fins de estudo e não
possui como objetivo utilização em ambiente de produção.

## Funcionalidades

### Gerenciamento de livros

A API implementa operações CRUD:

-   Listagem de livros
-   Busca de livro por ID
-   Cadastro de novos livros
-   Atualização de livros
-   Exclusão de livros

### Recomendação com Inteligência Artificial

A API possui uma rota específica para recomendação de livros:

1.  O usuário informa uma preferência.
2.  A aplicação consulta os livros cadastrados no SQLite.
3.  O catálogo é enviado ao Google Gemini junto com a preferência.
4.  A IA seleciona o livro que melhor corresponde à preferência.
5.  A API retorna a recomendação em formato JSON.

Exemplo de requisição:

``` json
{
  "preferencia": "Quero um livro de ficção científica com uma atmosfera política e sombria"
}
```

Exemplo de resposta:

``` json
{
  "livro_id": 4,
  "titulo": "1984",
  "autor": "George Orwell",
  "motivo": "Combina com a preferência por ficção científica, política e uma atmosfera sombria."
}
```

## Tecnologias utilizadas

  -----------------------------------------------------------------------
  Tecnologia                          Utilização
  ----------------------------------- -----------------------------------
  Python                              Linguagem de programação

  Flask                               Desenvolvimento da API REST e
                                      gerenciamento das rotas HTTP

  Flask-SQLAlchemy                    Integração com o banco de dados
                                      através de ORM

  SQLite                              Persistência dos dados dos livros

  Google Gemini API                   Recomendação de livros utilizando
                                      Inteligência Artificial

  python-dotenv                       Leitura e gerenciamento de
                                      variáveis de ambiente

  Git                                 Controle de versão
  -----------------------------------------------------------------------

## Endpoints

  Método     Rota               Descrição
  ---------- ------------------ ----------------------------------
  `GET`      `/livros`          Lista todos os livros
  `GET`      `/livros/<id>`     Busca um livro pelo ID
  `POST`     `/livros`          Cadastra um novo livro
  `PUT`      `/livros/<id>`     Atualiza um livro existente
  `DELETE`   `/livros/<id>`     Exclui um livro
  `POST`     `/ia/recomendar`   Recomenda um livro utilizando IA

## Exemplos de utilização

### Listar livros

``` bash
curl http://127.0.0.1:5000/livros
```

### Buscar um livro

``` bash
curl http://127.0.0.1:5000/livros/1
```

### Cadastrar um livro

``` bash
curl -X POST http://127.0.0.1:5000/livros \
-H "Content-Type: application/json" \
-d "{\"titulo\":\"Duna\",\"autor\":\"Frank Herbert\"}"
```

### Atualizar um livro

``` bash
curl -X PUT http://127.0.0.1:5000/livros/1 \
-H "Content-Type: application/json" \
-d "{\"titulo\":\"Duna\",\"autor\":\"Frank Herbert\"}"
```

### Excluir um livro

``` bash
curl -X DELETE http://127.0.0.1:5000/livros/1
```

### Recomendar um livro com IA

``` bash
curl -X POST http://127.0.0.1:5000/ia/recomendar \
-H "Content-Type: application/json" \
-d "{\"preferencia\":\"Quero um livro de ficção científica com uma atmosfera política e sombria\"}"
```

Exemplo de resposta:

``` json
{
  "livro_id": 4,
  "titulo": "1984",
  "autor": "George Orwell",
  "motivo": "Combina com a preferência por ficção científica, política e uma atmosfera sombria."
}
```

## Fluxo da aplicação

``` text
                Usuário
                   │
                   ▼
              API Flask
                   │
          ┌────────┴────────┐
          ▼                 ▼
      SQLite            Gemini API
          │                 │
          │        Preferência + catálogo
          │                 │
          └────────┬────────┘
                   ▼
              Recomendação
                   │
                   ▼
                 JSON
```

Na funcionalidade de recomendação, a aplicação utiliza os livros
existentes no banco de dados como catálogo para a IA. Dessa forma, a
recomendação é limitada às obras cadastradas no sistema.

## Banco de dados

O projeto utiliza SQLite para armazenamento dos livros e
Flask-SQLAlchemy para realizar o mapeamento entre o modelo Python e a
tabela do banco.

Cada livro possui os seguintes campos:

  Campo      Tipo      Descrição
  ---------- --------- ---------------------
  `id`       Integer   Identificador único
  `titulo`   String    Título do livro
  `autor`    String    Autor do livro

## Variáveis de ambiente e segurança

A chave utilizada para acessar a API do Google Gemini não é armazenada
diretamente no código.

Ela deve ser configurada através de um arquivo `.env`:

``` text
GEMINI_API_KEY=sua_chave_aqui
```

O arquivo `.env` deve permanecer no `.gitignore` e não deve ser enviado
ao GitHub.

O repositório também não deve conter chaves de API ou outras
credenciais.

## Estrutura do projeto

A estrutura utilizada no desenvolvimento é semelhante a:

``` text
api-livros-ia/
│
├── app.py
├── teste_gemini.py
├── requirements.txt
├── .env
├── .gitignore
│
├── instance/
│   └── livros.db
│
└── venv/
```

Arquivos e diretórios como `.env`, `venv/`, `__pycache__/` e o banco de
dados local podem ser mantidos fora do controle de versão conforme a
configuração do `.gitignore`.

## Como executar

### Pré-requisitos

-   Python instalado
-   Uma chave da API do Google Gemini
-   Git, caso o projeto seja clonado de um repositório

### 1. Clonar o repositório

``` bash
git clone URL_DO_REPOSITORIO
cd api-livros-ia
```

### 2. Criar o ambiente virtual

``` bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows:

``` bash
venv\Scripts\activate
```

### 4. Instalar as dependências

``` bash
pip install -r requirements.txt
```

### 5. Configurar a chave do Gemini

Crie um arquivo `.env` na raiz do projeto:

``` text
GEMINI_API_KEY=sua_chave_aqui
```

Não compartilhe a chave e não envie o arquivo `.env` para o repositório.

### 6. Executar a aplicação

``` bash
python app.py
```

A API será executada localmente em:

``` text
http://127.0.0.1:5000
```

## Objetivos de estudo

Este projeto foi desenvolvido exclusivamente para consolidar
conhecimentos em:

-   Desenvolvimento backend com Python
-   Desenvolvimento de APIs REST
-   Rotas e métodos HTTP
-   Operações CRUD
-   Bancos de dados relacionais
-   SQLite
-   ORM com SQLAlchemy
-   Integração entre aplicação e banco de dados
-   Integração com APIs externas
-   Uso de Inteligência Artificial em aplicações
-   Variáveis de ambiente
-   Segurança básica de credenciais
-   Git e controle de versão

## Possíveis melhorias futuras

Por se tratar de um projeto de estudo, algumas funcionalidades podem ser
exploradas posteriormente:

-   Testes automatizados
-   Documentação com Swagger/OpenAPI
-   Validação mais completa dos dados recebidos
-   Tratamento mais abrangente de erros
-   Autenticação de usuários
-   Paginação dos livros
-   Interface para consumo da API
-   Sistema de avaliações e favoritos
-   Melhorias na arquitetura e organização do código

------------------------------------------------------------------------

## Autor

**Julio Higor**

Projeto desenvolvido exclusivamente para estudo e prática de
desenvolvimento de software.
