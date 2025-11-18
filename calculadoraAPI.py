from flask import Flask, request, jsonify, render_template

#Criando o nosso aplicativo Flask
app = Flask(__name__)

#crianção da rota /soma com método GET
@app.route("/somar", methods=["GET"])
def somar():
    valor1 = request.args.get("a", type=int)
    valor2 = request.args.get("b", type=int)
    total = valor1 + valor2
    #Devolveremos ao usuário uma resposta com json no corpo
    return {"Tota":total}
#:f"{numero1} + {numero2} = {total}"



@app.route("/menos", methods=["GET"])
def menos():
    valor1 = request.args.get("c", type=int, default=0)
    valor2 = request.args.get("d", type=int, default=0)
    total = valor1 - valor2
    return {"Total":total}


@app.route("/multiplicador", methods=["GET"])
def multiplicador():
    valor1 = request.args.get("e", type=int, default=0)
    valor2 = request.args.get("f", type=int, default=0)
    total = valor1 * valor2
    return {"Total":total}



@app.route("/dividir", methods=["GET"])
def dividir():
    valor1 = request.args.get("g", type=int, default=0)
    valor2 = request.args.get("h", type=int, default=0)
    if valor2 == 0:
        return {"mensagem":"Erro Da Conta"}
    else:
        total = valor1 / valor2
        {"Total":total}


@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)
