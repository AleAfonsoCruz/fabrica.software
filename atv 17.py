salario = float(input("Digite seu salário:"))
print ("Valor antes do reajuste:", salario)

salario_baixo = salario*0.20
baixo = salario*1.20
salario_medio = salario*0.15
medio = salario*1.15
salario_minimo = salario*0.10
minimo = salario*1.10
salario_comercial = salario*0.05
comercial = salario*1.05

if salario <=280:
    print(f"Aumento de: 20% Valor: {salario_baixo} Final: {baixo:.1f}")
elif salario >280 and salario <=700:
    print(f"Aumento de: 15% Valor: {salario_medio} Final: {medio:.1f}")
elif salario >= 700 and salario <=1000:
    print (f"Aumento de: 10% Valor: {salario_minimo} Final: {minimo:.1f}")
elif salario >1500:
    print (f"Aumento de: 5% Valor: {salario_comercial} Final: {comercial:.1f}")


