# Nivel Fácil

#Desafio 1
nomes = ["joAo SIILVA", "mARIA souza", "carlos Eduardo"]

nomes_corrigidos = []
for lista in nomes: 
    nomes_corrigidos = lista.title()
    nomes_corrigidos = nomes_corrigidos.replace("Joao Siilva", "João Silva")
    print(nomes_corrigidos)

# Desafio 2
gastos_mes = [45.50, 120.00, 15.00, 800.00, 50.00, 250.00]
despesa_baixa = []
despesa_alta = []
for valor in gastos_mes:
    if valor <= 100.00:
        despesa_baixa.append(valor)
    else: 
        despesa_alta.append(valor)
print(f"Despesa alta: {despesa_alta}")
print(f"Despesa baixa: {despesa_baixa}")

# Nível Médio

# Desafio 3
lista_telefonica = []
celulares = ["11987654321", "987654321", "1198765432100", "21912345678"]
for digitos in celulares:
    if len(digitos) == 11:
        ddd =  digitos[0:2]
        parte1 = digitos[2:7]
        parte2 = digitos[7:11]
        numero_formatado = f"({ddd}) {parte1}-{parte2}"
        lista_telefonica.append(numero_formatado)
        
print(lista_telefonica)

# Desafio 4

carrinho = [{"item": "Camisa", "qtd": 2, "preco": 80.0}, 
            {"item": "Calça", "qtd": 1, "preco": 150.0}, 
            {"item": "Meia", "qtd": 3, "preco": 15.0}
]
valor_total = 0
valor_total = sum(item["preco"] * item["qtd"] for item in carrinho)
# for valor in carrinho:
#     total = valor["qtd"] * valor["preco"]
#     valor_total = total + valor_total
print(valor_total)

if valor_total > 300:
    valor_total = valor_total - (valor_total * 0.1)
print(valor_total)
    
if valor_total > 300:
    valor_total = valor_total - (valor_total * 0.1)
print(f"Sua compra total é de R${valor_total:.2f}")
    
# Nível 3 

# Desafio 5

vendas_log = ["Teclado:2:150.00", "Mouse:5:80.00", "Teclado:1:150.00", "Monitor:1:1200.00", "Mouse:2:80.00"]

relatorio_agrupado = {}
for venda in vendas_log:
    produto, quantidade_str, valor_str = venda.split(":")
    quantidade = int(quantidade_str)
    valor_unitario = float(valor_str)
    faturamento = quantidade * valor_unitario
    if produto in relatorio_agrupado:
        relatorio_agrupado[produto]["quantidade_total"] += quantidade
        relatorio_agrupado[produto]["faturamento_total"] += faturamento
    else:
        relatorio_agrupado[produto] = {
            "quantidade_total": quantidade,
            "faturamento_total": faturamento
        }
print(relatorio_agrupado)
    
    