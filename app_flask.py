from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    n1 = request.args.get("valor1", type=float)
    n2 = request.args.get("valor2", type=float)
    total = n1 + n2
    return{"operação": "soma", "resultado":f"{n1} + {n2} = {total}"}

@app.route("/subtrair")
def subtrair():
    n1 = request.args.get("valor1", type=float)
    n2 = request.args.get("valor2", type=float)
    total = n1 - n2
    return{"operação": "subtração", "resultado":f"{n1} - {n2} = {total}"}

@app.route("/multiplicar")
def multiplicar():
    n1 = request.args.get("valor1", type=float)
    n2 = request.args.get("valor2", type=float)
    produto = n1 * n2
    return{"operação": "multiplicação", "resultado":f"{n1} x {n2} = {produto}"}

@app.route("/dividir")
def dividir():
    n1 = request.args.get("valor1", type=float)
    n2 = request.args.get("valor2", type=float)
    if n2 == 0:
        return{"Erro": "Divisão por zero não é permitida."}
    else:
        quociente = n1 / n2
        return{"operação": "divisão", "resultado":f"{n1} / {n2} = {quociente:.3f}"}

             
if __name__ == "__main__":
    app.run(debug=True)