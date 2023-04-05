from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route('/filme')
def hello_world():
    name = request.args.get('name')
    print(database.buscar_nome_filme(name))
    return jsonify(database.buscar_nome_filme(name))

@app.route('/criar')
def criar_banco_url():
    database.criar_banco()
    return "criado"

@app.route('/apagar')
def apagar_banco_url():
    database.apagar_table()
    return "apagado"

if __name__ == '__main__':
    app.run(debug=True)
