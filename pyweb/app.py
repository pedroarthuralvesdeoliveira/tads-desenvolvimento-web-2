from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
