achar = 0
numeros = []
print("Digite 10 números inteiros")
for l in range(10):
    numeros.append(int(input(f"Digite o {l+1}º número: ")))
num = int(input("Número que gostaria de verificar: "))
for l in range(len(numeros)):
    if num == numeros[l]:
        print(f"Localizado na posição {l+1}")
    else:
        print("Não localizado")