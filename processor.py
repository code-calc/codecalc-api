
import pandas as pd
import os
import json

def gerar_juncoes():
    pasta_planilhas = 'planilhas'
    arquivos = [arq for arq in os.listdir(pasta_planilhas) if arq.endswith('.xlsx')]
    juncoes = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta_planilhas, arquivo)
        try:
            df = pd.read_excel(caminho)

            # Aqui começa a lógica fictícia (você vai adaptar depois)
            for _, row in df.iterrows():
                if 'Crédito' in row and 'Entrada Fornecedor' in row:
                    entrada = row['Entrada Fornecedor']
                    credito = row['Crédito']
                    if credito > 0:
                        porcentagem = round((entrada / credito) * 100, 2)
                        if porcentagem <= 47:
                            juncoes.append({
                                'Arquivo': arquivo,
                                'Crédito': credito,
                                'Entrada': entrada,
                                'Parcelas': row.get('Parcelas', '---'),
                                'Administradora': row.get('Administradora', '---'),
                                'Tipo': row.get('Destino/Tipo', '---'),
                                'Vencimento': str(row.get('Vencimento', '---')),
                                'Fornecedor': row.get('Fornecedor', '---'),
                                'Entrada %': porcentagem
                            })
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    # Salvar em JSON (modo local/teste)
    with open('juncoes.json', 'w', encoding='utf-8') as f:
        json.dump(juncoes, f, ensure_ascii=False, indent=2)

    return juncoes
