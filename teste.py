import json
with open("base_de_dados.json", "r",encoding="utf-8") as file:
    vendas = list(json.load(file))
    
# Nivel 1
categorias_unicas = []
for venda in vendas:
    for produtos in venda["itens"]:
        if produtos["categoria"] not in categorias_unicas:
            
            categorias_unicas.append(produtos["categoria"])
            
print(categorias_unicas)

