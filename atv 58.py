print("Cardápio"
            "\n1- Bife à parmegiana      R$18,50"
            "\n2- Batata recheada        R$14,00"
            "\n3- Lasanha                R$25,00"
            "\n4- Risoto                 R$23,50"
            "\n5- Guisado                R$35,00")
print("-"*40)

cardapio = int(input("Selecione o prato desejado: "))
match (cardapio):
      case 1:
            cardapio = 18.50
      case 2:
            cardapio = 14
      case 3:
            cardapio = 25
      case 4:
            cardapio = 23.50
      case 5:
            cardapio = 35
print(f"Valor do pedido R${cardapio:.1f}")

gorjeta = input("Aceita pagar a gorjeta de 10% para o garçom sobre o valor do prato? [S/N]")
if gorjeta == "S":
      print(f"Valor passa a ser R${cardapio+cardapio*10/100}")

