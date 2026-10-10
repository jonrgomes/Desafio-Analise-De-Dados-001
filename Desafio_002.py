# desafio 1
nomes = ["joAo SIILVA", "mARIA souza", "carlos Eduardo"]

nomes_corrigidos = []
for lista in nomes: 
    nomes_corrigidos = lista.title()
    nomes_corrigidos = nomes_corrigidos.replace("Joao Siilva", "João Silva")
    print(nomes_corrigidos)

