# Desafios de Fixação de Listas e Objetos.

## 🟢 Nível 1: Fáceis

*Desafio 1: Padronização de Base de Clientes (Listas, Loops e Strings)*

* *Contexto:* Você extraiu uma lista de nomes do banco de dados, mas os usuários digitaram os nomes sem padrão (letras maiúsculas e minúsculas misturadas).
* Exemplo de entrada: ["joAo SIILVA", "mARIA souza", "carlos Eduardo"]


* *Objetivo:* Percorra a lista usando um laço de repetição. Transforme cada nome para o formato "Título" (apenas a primeira letra de cada palavra maiúscula, ex: "Joao Silva") e adicione o nome corrigido em uma nova lista chamada nomes_corrigidos. Imprima a lista final.

*Desafio 2: Triagem de Despesas Mensais (Listas, Loops, Condicionais e Matemática)*

* *Contexto:* O setor financeiro te enviou uma lista com todos os valores gastos no mês: [45.50, 120.00, 15.00, 800.00, 50.00, 250.00].
* *Objetivo:* Percorra essa lista e separe os valores em duas novas listas: gastos_pequenos (valores abaixo de R$ 100) e gastos_altos (valores de R$ 100 ou mais). No final, use a lógica para somar e exibir qual foi o valor total apenas da lista de gastos_altos.

---

## 🟡 Nível 2: Médios

*Desafio 3: O Formatador Automático de Celulares (Listas, Loops, Condicionais e Fatiamento/Máscara)*

* *Contexto:* Uma lista contém números de telefone digitados como texto puro. Alguns estão corretos (11 dígitos, com DDD e o 9 extra), outros estão incompletos ou grandes demais.
* Exemplo: celulares = ["11987654321", "987654321", "1198765432100", "21912345678"]


* *Objetivo:* Percorra a lista.
1. Se a string tiver exatamente 11 caracteres, aplique a máscara e salve na nova lista no formato (XX) XXXXX-XXXX.
2. Se não tiver 11 caracteres, insira a string "Número Inválido" na nova lista.
3. Imprima a lista resultante.



*Desafio 4: Fechamento de Carrinho de E-commerce (Listas de Dicionários, Loops e Matemática)*

* *Contexto:* O carrinho de compras de um cliente é representado por uma lista de dicionários, onde cada item tem nome, quantidade e preço unitário.
* Exemplo: carrinho = [{"item": "Camisa", "qtd": 2, "preco": 80.0}, {"item": "Calça", "qtd": 1, "preco": 150.0}, {"item": "Meia", "qtd": 3, "preco": 15.0}]


* *Objetivo:* Percorra a lista do carrinho. Calcule o subtotal de cada produto (qtd * preco) e vá somando para encontrar o *valor total da compra*.
* Regra extra: Se o valor total da compra passar de R$ 300,00, aplique um desconto de 10% no total e exiba o valor final.



---

## 🔴 Nível 3: Difícil

*Desafio 5: ETL Básico - Extração e Agrupamento de Vendas (Listas, Loops, Strings e Modificação de Dicionários)*

* *Contexto:* Você recebeu um log do sistema de caixa, mas os dados vieram em um formato de texto bruto, separados por dois pontos (:), dentro de uma lista.
* Log bruto: vendas_log = ["Teclado:2:150.00", "Mouse:5:80.00", "Teclado:1:150.00", "Monitor:1:1200.00", "Mouse:2:80.00"]


* *Objetivo:* Você precisa converter essa lista de textos em um relatório financeiro agrupado usando um Dicionário.
1. Percorra a lista de logs.
2. Para cada texto, use o método .split(":") para separar o Nome do Produto, a Quantidade e o Valor Unitário. Lembre-se de converter os números para int e float.
3. Crie um dicionário vazio chamado relatorio_agrupado.
4. Adicione os produtos ao dicionário. Se o produto já existir lá, some a nova quantidade e adicione o novo faturamento ao existente.
5. Saída Esperada (Exemplo): {"Teclado": {"quantidade_total": 3, "faturamento_total": 450.0}, "Mouse": ...}