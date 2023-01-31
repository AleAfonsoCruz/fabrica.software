qnt_pao = int(input("Quantidade de pãozinhos vendidos: "))
qnt_broa = int(input("Quantidade de broas vendidas: "))

qnt_total = 1*qnt_pao + 3.50*qnt_broa
print(f"Valor total vendido: {qnt_total:.1f}")
print(f"Valor a ser guardado (10%): {qnt_total*10/100:.1f}")