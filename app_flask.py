from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def somar():
    numero1=  request.args.get("valor1", type=int)
    numero2=  request.args.get("valor2", type=int)
    total = numero1 + numero2
    return {"operação": "soma", "resultado": total}

@app.route("/subtrair")
def subtrair():
    numero1= request.args.get("valor1", type=int)
    numero2= request.args.get("valor2", type=int)
    total = numero1 - numero2
    return {"operação": "subtrair", "resultado":f"{numero1} + {numero2} = {total}"}


@app.route("/multiplicar")   
def multiplicar():
    numero1= request.args.get("valor1", type=int)
    numero2= request.args.get("valor2", type=int)
    total = numero1 * numero2
    return {"operação": "multiplicar", "resultado":f"{numero1} * {numero2} = {total}"}


@app.route("/divisao")    
def divisao():
    numero1= request.args.get("valor1", type=int)
    numero2= request.args.get("valor2", type=int)
    if numero2 == 0:
        return {"erro": "Divisão por zero não é permitida."}, 400
    total = numero1 / numero2
    return {"operação": "divisao", "resultado":f"{numero1} / {numero2} = {total}"}
          


if __name__ == "__main__":
    app.run(debug=True, port=3000)
