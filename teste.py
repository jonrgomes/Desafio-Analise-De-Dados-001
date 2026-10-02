import json 
with open("base_de_dados.json", "r",encoding="utf-8") as file: # encoding="utf-8 utilizado para o terminal aceitar os acentos e ç;
    vendas = list(json.load(file)) # converte a base de dados JSON em lista;
    
# Nivel 1
# categorias_unicas = []
# for venda in vendas: # percorre lista vendas com a variavel venda, venda recebe a lista JSON, base de dados;
#     for produtos in venda["itens"]: # percorre vendas com a variavel produto acessando o objeto itens;
#         if produtos["categoria"] not in categorias_unicas: # condiciona a leitura dos dados para não se repetir, sendo unica a impressáo da categoria no terminal. 
            
#             categorias_unicas.append(produtos["categoria"]) # adiciona a variavel produtos que recebeu a lista venda e os itens a categorias_unicas
            
# print(categorias_unicas) # imprime a lista criada e atribuida a variavel categorias_unicas
 
# cidades_unicas = []
# for venda in vendas:
#     if venda["endereco_entrega"]["cidade"] not in cidades_unicas:
#             cidades_unicas.append(venda["endereco_entrega"]["cidade"])
# print(cidades_unicas)

# status_venda = []
# for venda in vendas: 
#     if venda["status"] not in status_venda:
#         status_venda.append(venda["status"])
# print(status_venda)

# contagem_vendas = {}
# for venda in vendas: 
#    pagamento = venda["pagamento"]["metodo"]
#    if pagamento in contagem_vendas:
#         contagem_vendas[pagamento] +=1
#    else:
#         contagem_vendas[pagamento] = 1
# print(contagem_vendas)
       
            
 # Nível 2

valor_total = {}
qtd_de_itens = {}
qtd_de_pedidos = {}
for venda in vendas:
    if venda["status"] == "CANCELADO";
        continue
    valor_total += venda["preco_unitario"]
    itens_totais += venda["quantidade"]        
    pedidos_validos += 1
    print()