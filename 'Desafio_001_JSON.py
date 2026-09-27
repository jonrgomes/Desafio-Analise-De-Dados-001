import json

dados_json = '''
[
    {"produto": "Notebook", "valor": 3500, "vendedor": {"nome": "Ana", "regiao": "Nordeste"}},
    {"produto": "Mouse", "valor": 80, "vendedor": {"nome": "Carlos", "regiao": "Sul"}},
    {"produto": "Teclado", "valor": 250, "vendedor": {"nome": "Bia", "regiao": "Sudeste"}},
    {"produto": "Monitor", "valor": 1200, "vendedor": {"nome": "Ana", "regiao": "Nordeste"}},
    {"produto": "Cadeira", "valor": 900, "vendedor": {"nome": "Carlos", "regiao": "Sul"}}
]
'''

# 1) Use json.loads(dados_json) para transformar o texto em lista de dicionários
# 2) Percorra a lista e calcule: soma total, maior venda, menor venda e média
# 3) Bônus: imprima o nome do vendedor que fez a maior venda


lista_vendas = json.loads(dados_json)

soma = 0
maior_venda = lista_vendas[0]["valor"]
menor_venda = lista_vendas[0]["valor"]

for vendas in lista_vendas:
    valor_total = vendas["valor"]
    soma += valor_total
    print(soma)