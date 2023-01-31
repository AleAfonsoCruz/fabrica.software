#Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente.
#Assuma as entradas corretas:

x= ''
pedido = 0
total = 0

while True:
      print("\n100- Cachorro quente  R$11,20"
            "\n101- Ovo simples      R$8,30"
            "\n102- Bauru com ovo    R$11,50"
            "\n103- Hambúrguer       R$16,20")
      print("-"*40)

      cod = int(input("Digite o código do lanche: "))
      match (cod):
            case 100:
                  pedido = pedido + 11.20
            case 101:
                  pedido = pedido + 8.30
            case 102:
                  pedido = pedido + 11.50
            case 103:
                  pedido = pedido + 16.20

      print("\n201- Refrigerante   R$6,00"
            "\n202- Suco           R$7,50"
            "\n203- Água mineral   R$4,70")
      print("-"*40)

      cod = int(input("Digite o código da bebida: "))
      match (cod):
            case 201:
                  pedido = pedido + 6
            case 202:
                  pedido = pedido + 7.50
            case 203:
                  pedido = pedido + 4.70
      print(f"Valor total do pedido: R${pedido:.2f} ")

      x = input("Fazer novo pedido?")

      if x == 'N':
            break