print("Promoção de carne mercados Trabajara: "
      "\nAté 5 kg                                    Acima de 5 Kg"
      "\nFilé duplo R$34,90 por kg                   R$ 35,80 por Kg"
      "\nAlcatra R$44,90 por kg                      R$ 46,80 por Kg"
      "\nPicanha R$ 66,90 por kg                     R$ 67,80 por Kg")
print("="*60)
tipo = (input("Qual tipo de carne irá levar?\nF- Filé Duplo \nA- Alcatra \nP- Picanha"))
print("="*60)
quantidade = (float(input("Qual a quantidade desejada? (kg) ")))
print("="*60)
pagamento = input("Qual a forma de pagamento? \n1- Cartão Trabajara \n2- Outras formas")
print("="*60)
preco = desconto = 0

if tipo == "F":
      if quantidade <=5:
            preco = quantidade*34.90
      else:
            preco = quantidade*35.80
      tipo = "Filé duplo"
if tipo == "A":
      if quantidade <=5:
            preco = quantidade*44.90
      else:
            preco = quantidade*46.80
      tipo = "Alcatra"
if tipo == "P":
      if quantidade <=5:
            preco = quantidade*66.90
      else:
            preco = quantidade*67.80
      tipo = "Picanha"

if pagamento == "1":
      desconto = preco*5/100
      pagamento = "Cartões Trabajara"

elif pagamento == 2:
    desconto = 0
    pagamento = "Outras formas"
else:
    print("Valor inválido")

print(f"SUPERMERCADOS TRABAJARA")
print(f"\nCarne:--------------------------------{tipo}"
      f"\nForma de pagamento:-------------------{pagamento}"
      f"\nDesconto:---------------------------R${desconto:.1f}"
      f"\nValor total:------------------------R${preco-desconto:.1f}")
