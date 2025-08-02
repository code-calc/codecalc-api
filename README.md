
# CoDE Calc API

API simples em Flask para processar planilhas de cartas contempladas e gerar junções inteligentes com base em regras de entrada.

## Como funciona
- Lê todos os arquivos .xlsx da pasta /planilhas
- Aplica filtros (ex: entrada <= 47%)
- Gera um JSON com os resultados filtrados
- Disponibiliza via endpoint: /api/juncoes

## Como rodar localmente
```bash
pip install -r requirements.txt
python main.py
```

Depois acesse:
http://localhost:5000/api/juncoes
