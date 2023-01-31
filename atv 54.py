quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    elif n == 50:
        n = quantidade
        quantidade = quantidade + 1
print(f"Quantidade de número 50 digitados: {quantidade}")