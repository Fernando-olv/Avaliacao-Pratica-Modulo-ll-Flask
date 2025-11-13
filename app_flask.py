from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route ("/soma")
def somar():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type= int)
    total = valor1 +  valor2
    return {"resultado": total}
## Continue o código aqui.

@app.route ("/subtrair")
def subtracao():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type= int)
    total = valor1 - valor2
    return {"resultado": total}

@app.route ("/dividir")
def divisão():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type= int)
    if valor2 == 0:
        return "Erro de divisão por zero."
    total = valor1/valor2
    return {"resultado": total}

@app.route ("/multiplicacao")
def multiplicar():
    valor1 = request.args.get ("valor1", type=int)
    valor2 = request.args.get ("valor2", type= int)
    total = valor1 * valor2
    return {"resultado": total}





if __name__ == "__main__":
    app.run(debug=True)
