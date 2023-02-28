profesor1 = 0
professor2 = 0

horas1 = int(input("Quantidade de horas trabalhadas pelo prof 1: "))
horas2 = int(input("Quantidade de horas trabalhadas pelo prof 2: "))
print(" "*60)
porhr1 = float(input("Valor recebido por horas do prof 1:"))
porhr2 = float(input("Valor recebido por horas do prof 2: "))

salario1 = horas1 * porhr1
salario2 = horas2 * porhr2

if salario1 > salario2:
    print(f"O salário do prof 1 é de R${salario1} maior que o salário do prof 2.")
elif salario2 > salario1:
    print(f"O salário do prof 2 é de R${salario2} maior que o salário do prof 1.")
else:
    print(f"Os salários \nProf 1 R${salario1} \nProf 2 R${salario2} SÃO IGUAIS!")