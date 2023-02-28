num = 1 
par = 0
impar = 0

for n in range (10): 
    numeros = int(input(f"Digite o {n+1}º número inteiro: ")) 
    n = num + 1 
    if numeros % 2 == 0: 
        par = par + 1
    else: 
        impar = impar + 1
    
print(f"Quantidade de números pares: {par} \nQuantidade de números ímpares: {impar}") 