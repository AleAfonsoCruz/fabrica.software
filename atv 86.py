salario = float(input("Digite o salário:  "))
financiamento = float(input("Valor do financiamento desejado: "))

salarioMin = salario * 5

if financiamento <= salarioMin:
    print("Seu financiamento foi aprovado!")
else:
    print("Seu financiamento foi recusado.")
