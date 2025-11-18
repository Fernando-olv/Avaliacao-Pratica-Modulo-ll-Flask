from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/somar")
def somar():
    numero1 = request.args.get("valor1", type=int)
    numero2 = request.args.get("valor2", type=int)
    total = numero1 + numero2
    return {"resultado":total}

@app.route ("/subtrair")
def subtrair():
     numero1 = request . args.get ("valor1" , type=int)
     numero2 = request . args.get ("valor2", type =int)
     total= numero1 - numero2
     return {"resultado": total}

@app.route ("/divisao")
def dividir():
    numero1 = request . args.get ("valor1" , type=int)
    numero2 = request . args.get ("valor2", type =int)
    total= numero1 / numero2
    return {"resultado": total}

@app.route ("/multiplicacao")
def multiplicar():
    numero1 = request . args.get ("valor1" , type=int)
    numero2 = request . args.get ("valor2", type =int)
    total= numero1 * numero2
    return {"resultado": total}

## Continue o código aqui.

if __name__ == "__main__":
    app.run(debug=True)
