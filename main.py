from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ✅ Teste de conexão
@app.route('/')
def home():
    return jsonify({"mensagem": "API do CoDE está online!"})

# ✅ Rota para gerar junções com base na última planilha
@app.route('/api/juncoes', methods=['GET'])
def gerar_juncoes():
    try:
        # Caminho da pasta onde você sobe as planilhas no WordPress
        PASTA_PLANILHAS = '/mnt/data/planilhas-codecalc'

        # Lista todas as planilhas disponíveis
        arquivos = [f for f in os.listdir(PASTA_PLANILHAS) if f.endswith('.xlsx')]

        if not arquivos:
            return jsonify({"erro": "Nenhuma planilha encontrada na pasta."}), 404

        # Pega a planilha mais recente
        caminho_arquivo = os.path.join(PASTA_PLANILHAS, sorted(arquivos)[-1])

        # Lê a planilha
        df = pd.read_excel(caminho_arquivo)

        # Apenas um exemplo simples: calcular total de crédito e média de entrada
        total_credito = df['Crédito'].sum()
        entrada_media = df['Entrada Fornecedor'].mean()

        resultado = {
            "total_cartas": len(df),
            "credito_total": f"R$ {total_credito:,.2f}",
            "entrada_media": f"R$ {entrada_media:,.2f}"
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
