divida = int(input(("Digite o valor da sua conta: ")))
print(" "*60)
print("Quantidade de parcelas        % de juros no valor inicial"
      "\n1- 1x parcela-----------------------0%"
      "\n2- 3x parcelas----------------------10%"
      "\n3- 6x parcelas----------------------15%"
      "\n4- 9x parcelas----------------------20%"
      "\n5- 12x parcelas---------------------25%")
print(" "*60)
parcelas = int(input("Escolha a opção de parcelas: "))
match (parcelas):
    case 1:
        juros = 0
        quantia = divida+juros/1
    case 2:
        juros = divida*10/100
        quantia = (divida+juros)/3
        parcelas = 3
    case 3:
        juros = divida*15/100
        quantia = (divida+juros)/6
        parcelas = 6
    case 4:
        juros = divida*20/100
        quantia = (divida+juros)/9
        parcelas = 9
    case 5:
        juros = divida*25/100
        quantia = (divida+juros)/12
        parcelas = 12
print(" "*60)
print("Valor da dívida      Valor do Juros      Quantidade de parcelas      Valor da parcela"
      f"\nR${divida}                    R${juros}                       {parcelas}           R${quantia}")