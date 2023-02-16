livros = int(input("Quantidade de livros desejados: "))
print("-"*40)
pontos = 0
while livros >0:
    match (livros):
        case 0:
            pontos += 0
            print(f"Quantidade de pontos obtidos {pontos}")
        case 1:
            pontos += 5
            print(f"Quantidade de pontos obtidos {pontos}")
        case 2:
            pontos += 15
            print(f"Quantidade de pontos obtidos {pontos}")
        case 3:
            pontos += 30
            print(f"Quantidade de pontos obtidos {pontos}")
        case _:
            pontos += 60
            print(f"Quantidade de pontos obtidos {pontos}")

    livros = input("Gostaria de comprar mais livros? [S/N]")
    livros = livros.upper()
    print("-" * 40)
    if livros == "S":
        livros = int(input("Quantos livros a mais? "))
        print("-" * 40)
    else:
        break

brindes = input(f"Você possui {pontos} pontos, gostaria de trocar por brinde? [S/N]")
brindes = brindes.upper()
print("-"*40)
if brindes == "S":
    print("       LISTA DE BRINDES"
          "\n1- 20-30 pontos: EcoBag ou Caneta personalizada "
          "\n2- 35-60 pontos: Livro até R$30,00 ou Luminária de cabeceira"
          "\n3- 65 ou mais pontos: 2 livros com máximo R$100,00 ou POWERBANK")
    print("-" * 40)
    escolha = pontos - pontos
    brindes = int(input("Escolha a opção do brinde: "))
    if brindes == 1 and pontos >=20 and pontos <=30:
        print("Dirija-se ao caixa para retirar seu brinde!")
    if brindes == 2 and pontos >= 35 and pontos <= 60:
        print("Dirija-se ao caixa para retirar seu brinde!")
    if brindes == 3 and pontos >=65:
        print("Dirija-se ao caixa para retirar seu brinde!")
        print("-" * 40)
    print(f"Quantidade de pontos disponíveis: {escolha}")
else:
    print(f"Você não possui pontos suficientes.")
