numero = int(input("Digite um número: "))
nummaior = numero
nummenor = numero

for n in range (1,20):
    numero = int(input("Digite um número: "))
    if numero < nummenor:
        nummenor = numero
    if numero > nummaior:
        nummaior = numero
print(f"Número maior: {nummaior} \nNúmero menor: {nummenor}")