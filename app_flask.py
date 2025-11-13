from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def somar():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type=int)
    total = valor1 + valor2
    return {"resultado":total}

@app.route("/subtracao")
def subtrair():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type=int)
    total = valor1 - valor2
    return {"resultado":total }

@app.route("/multiplicaçao")
def multiplicar():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type=int)
    total = valor1 * valor2
    return {"resultado":total }

@app.route("/divisao")
def dividir():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type=int)
    if valor2 == 0:
        return "Erro de divasao por 0"
    total = valor1 / valor2
    return {"resultado":total }


if __name__ == "__main__":
    app.run(debug=True)
