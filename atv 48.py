produto = float(input("Valor do produto (etiqueta): R$"))
pagamento = int(input("Forma de pagamento: "
                      "\n1- À vista, dinheiro ou pix "
                      "\n2- Crédito à vista "
                      "\n3- Crédito em 2x "
                      "\n4- Crédito em 3x\n"))
match (pagamento):
    case 1:
        total = produto - (produto*10/100)
    case 2:
        total = produto - (produto*5/100)
    case 3:
        total = produto
    case 4:
        total = produto + (produto+10/100)

print(f"Valor final do produto R${total}")