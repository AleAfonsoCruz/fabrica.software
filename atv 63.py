soma = 0
numero = []

for n in range(1,6):
    num = int(input("Digite um número: "))

    if num != 0:
        soma += num
        numero.append(num)
    else:
        break

print(f"Menor valor:", min(numero))
print(f"Maior valor:", max(numero))
print(f"Soma dos valores:", soma)