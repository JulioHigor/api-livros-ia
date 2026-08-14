from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

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
      
    
if __name__ == "__main__":
    app.run(debug=True)