

from flask import Flask, request, jsonify, render_template
app = Flask(__name__ )

@app.route("/")
def index():
    return render_template("index.html")



#Criação da rota / soma com metodo GET
@app.route("/dividir", methods = ["GET"])

def dividir():
    valor1 = request.args.get("a", type=int, default=0)
    valor2 = request.args.get('b', type=int, default=1)
    total = valor1 / valor2
    #Devolveremos ao usuario uma respota com json no corpo
    return {"total":total}



@app.route("/soma", methods = ["GET"])

def somar():
    valor1 = request.args.get("a", type=int, default=0)
    valor2 = request.args.get('b', type=int, default=0)
    total = valor1 + valor2
    #Devolveremos ao usuario uma respota com json no corpo
    return {"total":total}




@app.route("/multiplicação", methods = ["GET"])

def multiplicar():
    valor1 = request.args.get("a", type=int, default=0)
    valor2 = request.args.get('b', type=int, default=0)
    total = valor1 * valor2
    #Devolveremos ao usuario uma respota com json no corpo
    return {"total":total}



@app.route("/subtrair", methods = ["GET"])

def subitrair():
    valor1 = request.args.get("a", type=int, default=0)
    valor2 = request.args.get('b', type=int, default=0)
    total = valor1 - valor2
    #Devolveremos ao usuario uma respota com json no corpo
    return {"total":total}

app.run(debug=True) 

