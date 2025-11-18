from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def soma():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    resultado = a + b
    return {'resultado': resultado}

@app.route('/subtrai', methods=['GET'])
def subtrai():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    resultado = a - b
    return {'resultado': resultado}

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    if b == 0:
        return {'erro': 'Divisão por zero não permitida!'}
    resultado = a / b
    return {'resultado': resultado}

@app.route('/multiplica', methods=['GET'])
def multiplica():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    resultado = a * b
    return{'resultado': resultado}

@app.route ('/')
def index ():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


