# 📚 API de Livros com Inteligência Artificial

API REST desenvolvida em Python com Flask para gerenciamento de livros, utilizando SQLite como banco de dados e integração com a API do Google Gemini para recomendações personalizadas.

> **Projeto exclusivamente para estudo**, desenvolvido para praticar desenvolvimento backend, APIs REST, bancos de dados, operações CRUD e integração com Inteligência Artificial.

## 🚀 Funcionalidades

### 📖 Gerenciamento de livros

A API possui operações completas de CRUD:

- Listar livros
- Buscar um livro pelo ID
- Cadastrar livros
- Atualizar livros
- Excluir livros

### 🤖 Recomendação com Inteligência Artificial

O usuário informa uma preferência de leitura e a API consulta os livros disponíveis no banco de dados.

A preferência e o catálogo são enviados para o Google Gemini, que seleciona o livro mais adequado.

Exemplo de preferência:

> "Quero um livro de ficção científica com uma atmosfera política e sombria."

Exemplo de resposta:

```json
{
    "livro_id": 4,
    "titulo": "1984",
    "autor": "George Orwell",
    "motivo": "Combina com a preferência por ficção científica, política e uma atmosfera sombria."
}