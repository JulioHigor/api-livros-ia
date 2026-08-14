from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


@app.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    
    resultado = []
    
    for livro in livros:
        resultado.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor
        })

    return jsonify(resultado)

@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = db.get_or_404(Livro, id)
    
    return jsonify({
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor
    })

@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.get_json()
    
    novo_livro = Livro(
        titulo=dados["titulo"],
        autor=dados["autor"]
    )
    
    db.session.add(novo_livro)
    db.session.commit()
    
    return jsonify({
        "id": novo_livro.id,
        "titulo": novo_livro.titulo,
        "autor": novo_livro.autor
    }), 201

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = db.get_or_404(Livro, id)
    dados = request.get_json()

    livro.titulo = dados["titulo"]
    livro.autor = dados["autor"]

    db.session.commit()

    return jsonify({
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor
    })
      

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    livro = db.get_or_404(Livro, id)
    
    db.session.delete(livro)
    db.session.commit()
    
    return jsonify({
        "mensagem": "Livro deletado com sucesso"
    })
    
    
@app.route("/ia/recomendar", methods=["POST"])
def recomendar_livro():
    dados = request.get_json()

    preferencia = dados["preferencia"]

    livros = Livro.query.all()

    catalogo = []

    for livro in livros:
        catalogo.append(
            f"ID: {livro.id} | Título: {livro.titulo} | Autor: {livro.autor}"
        )

    prompt = f"""
Você é um assistente especializado em recomendação de livros.

Não responda nada que não seja específico sobre livros.

O usuário informou a seguinte preferência:
"{preferencia}"

Estes são os livros disponíveis no catálogo:

{chr(10).join(catalogo)}

Escolha o livro do catálogo que melhor combina com a preferência do usuário.

Retorne SOMENTE um JSON válido, sem markdown e sem texto adicional, seguindo exatamente este formato:

{{
    "livro_id": número do ID do livro escolhido,
    "titulo": "título do livro",
    "autor": "autor do livro",
    "motivo": "explicação curta de por que o livro combina com a preferência"
}}

Não recomende livros que não estejam no catálogo.
"""

    resposta = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )

    recomendacao = json.loads(resposta.output_text)

    return jsonify(recomendacao)
    
    
if __name__ == "__main__":
    app.run(debug=True)