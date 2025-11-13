from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def smr():
    vlr_a=request.args.get("valor1", type=int)
    vlr_b=request.args.get("valor2", type=int)
    total=vlr_a+vlr_b
    return {"redultado" : total}

@app.route("/subtrair")
def sub():
    vlr_a=request.args.get("valor1", type=int)
    vlr_b=request.args.get("valor2", type=int)
    total=vlr_a-vlr_b
    return {"resultado":total}

@app.route("/multi")
def multi():
    vlr_a=request.args.get("valor1", type=int)
    vlr_b=request.args.get("valor2", type=int)
    total=vlr_a*vlr_b
    return {"resultado":total}

@app.route("/divisao")
def div():
    vlr_a=request.args.get("valor1", type=int)
    vlr_b=request.args.get("valor2", type=int)
    if vlr_b==0:
        return "Erro de divisão com zero"
    total=vlr_a/vlr_b
    return {"resultado":total}


if __name__=="__main__":
    app.run(debug=True)