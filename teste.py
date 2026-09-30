import json 
with open("base_de_dados.json", "r",encoding="utf-8") as file: # encoding="utf-8 utilizado para o terminal aceitar os acentos e ç;
    vendas = list(json.load(file)) # converte a base de dados JSON em lista;
    
# Nivel 1
categorias_unicas = []
for venda in vendas: # percorre lista vendas com a variavel venda, venda recebe a lista JSON, base de dados;
    for produtos in venda["itens"]: # percorre vendas com a variavel produto acessando o objeto itens;
        if produtos["categoria"] not in categorias_unicas: # condiciona a leitura dos dados para não se repetir, sendo unica a impressáo da categoria no terminal. 
            
            categorias_unicas.append(produtos["categoria"]) # adiciona a variavel produtos que recebeu a lista venda e os itens a categorias_unicas
            
print(categorias_unicas) # imprime a lista criada e atribuida a variavel categorias_unicas
 
