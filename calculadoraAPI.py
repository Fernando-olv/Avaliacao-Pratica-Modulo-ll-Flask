from flask import Flask, request, render_template


#criando o nosso aplicativo Flask ⬇
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#Criação da rota /soma com metodo GET
@app.route("/somar", methods=["GET"])
def somar () :
    valor1 = request.args.get("a" , type=int, default= 0)
    valor2 = request.args.get("b" , type=int, default= 0)
    total = valor1 + valor2

    #DEVOLVEMOS AO USUARIO UMA RESPOSTA COM JSON NO CORPO
    return {"Total" :total}

#Criação da rota / subtrair com metodo GET
@app.route("/subtrair", methods=["GET"])
def subtrair () :
    valor1 = request.args.get("a" , type=int, default= 0)
    valor2 = request.args.get("b" , type=int, default= 0)
    total = valor1 - valor2

    #DEVOLVEMOS AO USUARIO UMA RESPOSTA COM JSON NO CORPO
    return {"Total" :total}

#Criação da rota /multiplicar com metodo GET
@app.route("/multiplicar", methods=["GET"])
def multiplicar () :
    valor1 = request.args.get("a" , type=int, default= 0)
    valor2 = request.args.get("b" , type=int, default= 0)
    total = valor1 * valor2

    #DEVOLVEMOS AO USUARIO UMA RESPOSTA COM JSON NO CORPO
    return {"Total" :total}

#Criação da rota /soma com metodo GET
@app.route("/dividir", methods=["GET"])
def dividir () :
    valor1 = request.args.get("a" , type=int, default= 0)
    valor2 = request.args.get("b" , type=int, default= 0)
    if valor2 == 0:
        return {"erro": "Divisão por zero não é permitida!"}, 400

    total = valor1 / valor2

    #DEVOLVEMOS AO USUARIO UMA RESPOSTA COM JSON NO CORPO
    return {"Total" :total}



app.run(debug=True)

