from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route ("/soma")
def somar ():
    valor_a = request.args.get ("valor1" , type=int)
    valor_b = request.args.get ("valor2" , type=int)
    total= valor_a + valor_b
    return {"resultado": total}

@app.route ("/menos")
def menos ():
    valor_a = request.args.get ("valor1" ,type=int )
    valor_b = request.args.get ("valor" , type=int)
    total= valor_a - valor_b
    return {"resultado" : total}

@app.route ("/divisao")
def dividir ():
    valor_a = request.args.get ("valor1" ,type=int )
    valor_b = request.args.get ("valor2" , type=int)
    total= valor_a / valor_b
    return {"resultado" : total}

@app.route ("/multiplicacao")
def multiplicacao():
    valor_a = request.args.get ("valor1", type=int)
    valor_b = request.args.get ("valor2" , type=int)
    total= valor_a * valor_b
    return {"resultado": total}

@app.route ("/dividir")
def dividir ():
    valor_a = request.args.get ("valor1" , type=int)
    valor_b = request.args.get ("valor2" , type=int)
    if= valor_b == 0:
        return "erro de divisao por zero."
    total = valor_a/valor_b
    return {"resultado" : total}



## Continue o código aqui.

if __name__ == "__main__":
    app.run(debug=True, port=1500)
