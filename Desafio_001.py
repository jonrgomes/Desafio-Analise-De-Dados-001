# Nível_1
categorias = ("Cama_mesa_e_banho", "Eletrodomésticos", "Vestuário", "Papelaria", "Calçados")
cidades = ("Itabuna", "Camacãn", "Porto Seguro", "Teuxeira de Freitas", "Bom Jesus da Lapa", "Salvador", "Feira de Santana")
status_venda = ("Em processamento", "Aguardando pagamento", "Pagamento recebido", "Em separacão", "Faturado", "Entregue", "Cancelada", "Devolvida")

pagamento = {
    "PIX": 200,
    "CARTÃO_CRÉDITO": 300,
    "DINHEIRO": 68,
    "DÉBITO": 232
}

# Nível_2
produtos_catalogo = [
    {"Produto":1, "qtd_vendida": 1500, "valor": 389.90, "Status da venda": "Cacelada"},
    {"Produto":2, "qtd_vendida": 288, "valor": 389.90, "Status da venda": "Faturado"},
    {"Produto":3, "qtd_vendida": 6, "valor": 389.90, "Status da venda": "Cacelada"},
    {"Produto":4, "qtd_vendida": 3788, "valor": 389.90, "Status da venda": "Entregue"},
    {"Produto":5, "qtd_vendida": 98, "valor": 389.90, "Status da venda": "Em processamento"},
    {"Produto":6, "qtd_vendida": 4, "valor": 389.90, "Status da venda": "Aguardando pagamento"},
    {"Produto":7, "qtd_vendida": 978, "valor": 389.90, "Status da venda": "Pagamento recebido"},
    {"Produto":8, "qtd_vendida": 2, "valor": 389.90, "Status da venda": "Cacelada"}                               
]

vlr_total_vendas = 0
qtd_produtos_vendidos = 0
qtd_pedidos_validos = 0

for vendas in produtos_catalogo:
    if vendas["Status da venda"] != "Cancelada":
        vlr_total_vendas += vendas["valor"]
        qtd_produtos_vendidos += vendas["qtd_vendida"]
        qtd_pedidos_validos += 1


if qtd_pedidos_validos > 0:
    ticket_medio = vlr_total_vendas / qtd_pedidos_validos
else:
    ticket_medio = 0
        
print(f"Valor em vendas: R${vlr_total_vendas:.2f}")
print(f"Qtd. de vendas: {qtd_produtos_vendidos}")
print(f"Pedidos validados: {qtd_pedidos_validos}")
print(f"Ticket médio: R${ticket_medio:.2f}")