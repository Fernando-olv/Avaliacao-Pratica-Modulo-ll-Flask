from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/soma', methods=['GET'])
def soma():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    resultado = a + b
    return {'resultado': resultado}

@app.route('/subtrai', methods=['GET'])
def subtrai():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    resultado = a - b
    return {'resultado': resultado}

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))
    if b == 0:
        return {'erro': 'Divisão por zero não permitida!'}
    resultado = a / b
    return {'resultado': resultado}

@app.route('/multiplica', methods=['GET'])
def multiplica():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    resultado = a * b
    return{'resultado': resultado}

if __name__ == "___main__":
    app.run(debug=True)