valor = float(input("Digite o valor do produto:"))

desconto = valor *10/100
novo_valor = valor - desconto
print(f"Valor novo R$:{novo_valor:.2f}")