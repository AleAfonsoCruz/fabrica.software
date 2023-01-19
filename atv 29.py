h = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

peso_idealM = (72.7*h) - 58
peso_idealF = (62.1*h) - 44.7

if sexo == "F":
    print(f"O peso ideal é: {peso_idealF:.1f}")
elif sexo == "M":
    print(f"O peso ideal é:{peso_idealM:.1f}")
else:
    print("Sexo inválido.")