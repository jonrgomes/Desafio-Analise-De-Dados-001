# Atividade 01
entradas = []
vendas = [120.50, -15.00, 45.00, 89.90, -100.00, 250.00]

for venda in vendas:
    if venda >= 0:
        venda = venda + (venda * 0.1)
        entradas.append(venda)
print(entradas)