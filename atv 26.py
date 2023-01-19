p1 = float(input("Valor do produto 1:"))
p2 = float(input("Valor do produto 2:"))

p1_mais = p1 + p1*45/100
p2_mais = p2 + p2*45/100

# valor adicionado caso aquisição menor que 50
if p1 <= 50:
    print(f"O valor do produto 1 é de R$: {p1_mais}")
if p2 <= 50:
    print(f"O valor do produto 2 é de R$: {p2_mais}")

p1_menos = p1 + p1*30/10
p2_menos = p2 + p2*30/100

# valor adicionado caso aquisição maior que 50
if p1 > 50:
    print(f"O valor do produto 1 é de R$: {p1_menos}")
if p2 > 50:
    print(f"O valor do produto 2 é de R$: {p2_menos}")