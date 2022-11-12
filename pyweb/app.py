from flask import Flask, render_template, request
from datetime import datetime

from Entities.Cliente import Cliente

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/conversao", methods=["POST", "GET"])
def conversao():
    if request.method == 'GET':
        return render_template("conversao.html")

    valor = float(request.form.get("valor"))
    valorReais = valor * 5.24
    return render_template("conversao.html", valorReais=valorReais)


@app.route("/imc", methods=["POST", "GET"])
def calculaIMC():
    if request.method == 'GET':
        return render_template("imc.html")

    peso = float(request.form.get("peso"))
    altura = float(request.form.get("altura"))

    def calcularIMC(peso, altura):
        return peso / (altura*altura)

    imc = calcularIMC(peso, altura)

    return render_template("imc.html", imc=imc)


@app.route("/cliente", methods=["POST", "GET"])
def cliente():
    if request.method == 'GET':
        return render_template("cliente.html")
    id = int(request.form.get("id"))
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    cep = request.form.get("cep")
    email = request.form.get("email")
    cpf = request.form.get("cpf")
    dataNascimento = request.form.get("dataNascimento")
    telefone = request.form.get("telefone")

    cliente = Cliente(id, nome, senha, cep, email,
                      cpf, dataNascimento, telefone)

    return render_template("cliente.html", nome=cliente.nome)


if __name__ == "__main__":
    app.run(debug=True)
