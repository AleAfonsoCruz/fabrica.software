moeda1 = 0.01
moeda2 = 0.10
moeda3 = 0.25
moeda4 = 0.50
real1 = 1
cent1 = int(input("Quantia de moedas de R$0,01 cent: "))
cent2 = int(input("Quantia de moedas de R$0,10 cent: "))
cent3 = int(input("Quantia de moedas de R$0,25 cent: "))
cent4 = int(input("Quantia de moedas de R$0,50 cent: "))
real = int(input("Quantia de moedas de R$1,00: "))

total = moeda1*cent1 + moeda2*cent2 + moeda3*cent3 + moeda4*cent4 + real1*real

print(f"O total de moedas em real é de: R${total:.1f}")