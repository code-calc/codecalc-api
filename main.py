
from flask import Flask, jsonify
from processor import gerar_juncoes

app = Flask(__name__)

@app.route('/api/juncoes', methods=['GET'])
def listar_juncoes():
    resultado = gerar_juncoes()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
