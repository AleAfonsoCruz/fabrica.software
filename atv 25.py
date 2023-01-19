P = 10
camisa_p = int(input("Quantidade de camisa pequena:"))
M = 12
camisa_m = int(input("Quantidade de camisa média:"))
G = 15
camisa_g = int(input("Quantidade de camisa grande:"))

qnt_valor = (P*camisa_p) + (M*camisa_m) + (G*camisa_g)
print(f"O valor total de camisas é de R$: {qnt_valor},00")
