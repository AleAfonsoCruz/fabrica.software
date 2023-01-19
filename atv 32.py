saque = int(input("Digite o valor do saque [10 - 600]:"))

cem = int(saque/100)
saque_cem = saque - (cem*100)

cinquenta = int(saque/50)
saque_cinquenta = saque - (cinquenta*50)

dez = int(saque/10)
saque_dez = saque - (dez*10)

cinco = int(saque/5)
saque_cinco = saque - (cinco*5)

um = saque

print(f"Notas R$100: {cem}")
print(f"Notas R$50: {cinquenta}")
print(f"Notas R$10: {dez}")
print(f"Notas R$5: {cinco}")
print(f"Notas R$1: {um}")