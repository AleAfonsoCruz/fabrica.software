lista = []
soma = 0

print("Digite 5 números")
for n in range(5):
  lista.append(float(input(f"{n+1}º número: ")))
  num = lista[n]
  soma = soma + num
print(f"A soma dos números digitados é: {soma:.1f}")
print(f"Os números digitados foram: {lista}")