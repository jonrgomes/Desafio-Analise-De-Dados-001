# Nivel Fácil

# Desafio 1
# nomes = ["joAo SIILVA", "mARIA souza", "carlos Eduardo"]

# nomes_corrigidos = []
# for lista in nomes: 
#     nomes_corrigidos = lista.title()
#     nomes_corrigidos = nomes_corrigidos.replace("Joao Siilva", "João Silva")
#     print(nomes_corrigidos)

# # Desafio 2
# gastos_mes = [45.50, 120.00, 15.00, 800.00, 50.00, 250.00]
# despesa_baixa = []
# despesa_alta = []
# for valor in gastos_mes:
#     if valor <= 100.00:
#         despesa_baixa.append(valor)
#     else: 
#         despesa_alta.append(valor)
# print(f"Despesa alta: {despesa_alta}")
# print(f"Despesa baixa: {despesa_baixa}")

# Nível Médio

# Desafio 3
lista_telefonica = []
celulares = ["11987654321", "987654321", "1198765432100", "21912345678"]
for digitos in celulares:
    if len(digitos) == 11:
        lista_telefonica.append(digitos)
print(lista_telefonica)
   
