num = 1
par = 0
impar = 0

while num <=10:
    a = int(input("Digite 10 números inteiros: "))
    num = num + 1
    if num %2 == 0:
        par +=1
    else:
        impar +=1
print(f"Quantidade de números pares: {par}"
      f"\nQuantidade de números ímpares : {impar}")