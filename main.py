import json
with open("base_de_dados.json", "r",encoding="utf-8") as file:
    vendas = list(json.load(file))
# Criar uma tupla com os nomes de todas as categorias únicas vendidas:
""" 
0 - Declarar uma variável categorias com um []: 
1 - Percorrer as vendas:
2 - Para cada venda percorrer a lista de itens:
3 - Para cada item acessar a categoria do item e inserir dentro da tupla de categorias:
obs: injetar um objeto completo de categorias ao invés de só o próprio nome categoria. 
4 - Remover duplicatas
"""
categorias = []
for venda in vendas:
    for produto in venda["itens"]:
        if produto["categoria"] not in categorias:
                        
            categorias.append(produto["categoria"])
print(categorias)

"""
1 - Criar um variavel cidade que recebe uma lista com as cidades unicas:
2 - Percorrer vendas:
3 - para cada venda percorrer a o atributo endereço de entrega:
4 - para endereço de entrega acessar a cidade.
"""
cidades = []
for venda in vendas:
    if venda["endereco_entrega"]["cidade"] not in cidades:
        cidades.append(venda["endereco_entrega"]["cidade"])
print(cidades)

status_venda = []
for venda in vendas:
    if venda["status"] not in status_venda:
        status_venda.append(venda["status"])
print(status_venda)




# ENCOTRAR UMA VENDA COM O ID [1001, 1002, 1007, 1009, 1015]
# lista_filtrada = [venda for venda in vendas if venda["id_venda"] >= 1001 and venda["id_venda"] <= 1009]

# print(lista_filtrada)
# for x in lista_filtrada:
#     print(x["cliente"]["nome"])



# print(venda_encontrada["valor_total"])
# print(venda_encontrada["cliente"]["nome"])



# matches = [x for x in lst if fulfills_some_condition(x)]
# matches = (x for x in lst if x > 6)
