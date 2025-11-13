from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

# soma

@app.route("/soma")
def somar():
    valor_a = request.args.get("valor1",type=int)
    valor_b = request.args.get("valor2",type=int)
    total = valor_a + valor_b
    return {"resultado": total}



# subtração

@app.route("/subtracao")
def subtrair():
    valor_a = request.args.get("valor1",type=int)
    valor_b = request.args.get("valor2",type=int)
    total = valor_a - valor_b
    return {"resultado": total}

# divisão

@app.route("/divisao")
def dividir():
    valor_a = request.args.get("valor1",type=int)
    valor_b = request.args.get("valor2",type=int)
    if valor_b == 0:
        return "erro de divisao por zero"
    total = valor_a / valor_b
    return {"resultado" : total}


# multiplicação

@app.route("/multiplicacao")
def multiplicar():
    valor_a = request.args.get("valor1",type=int)
    valor_b = request.args.get("valor2",type=int)
    total = valor_a * valor_b
    return {"resultado": total}


if __name__ == "__main__":
    app.run(debug=True)
