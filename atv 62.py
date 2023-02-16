inteiro = int(input("Digite um número inteiro para descobrir seu fatorial: "))
rstd = 1
contador = 1
while contador <=inteiro:
    rstd *= contador
    contador += 1
print(f"Fatorial do número {inteiro} é: {rstd}")