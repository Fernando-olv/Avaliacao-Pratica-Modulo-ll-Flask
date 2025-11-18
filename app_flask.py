from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/plus')
def plus():
    valor1 = (request.args.get("a", type=int))
    valor2 = (request.args.get("b", type=int))
    total = valor1 + valor2
    return {"message":total}

@app.route('/subtract')
def subtract():
    valor1 = (request.args.get("a", type=int))
    valor2 = (request.args.get("b", type=int))
    total = valor1 - valor2
    return {"message":total}

@app.route('/multiply')
def multiply():
    valor1 = (request.args.get("a", type=int))
    valor2 = (request.args.get("b", type=int))
    total = valor1 * valor2
    return {"message":total}

@app.route('/divide')
def divide ():
    try:
        valor1 = (request.args.get("a", type=int, default=0))
        valor2 = (request.args.get("b", type=int, default=1))
        total = valor1 / valor2
        return {"message":total}
    except:
        return {"message": "erro de divisao por zero"}

if __name__ == "__main__":
    app.run(debug=True)
