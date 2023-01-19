alunos = 0
mulheres = 0
homens = 0
bons = 0
porc = 0

while alunos <3:
    sexo = input("Digite o sexo:")
    altura = float(input("Digite a altura:"))
    status = int(input("Digite o status:\n1 - BOM\n2 - REGULAR\n3 - RUIM\n"))

    if(sexo == "F" and altura >1.7):
        mulheres = mulheres + 1
    else:
        homens = homens + 1

    if(sexo == "M" and status == 1):
        bons = bons + 1
        porc = bons * 100 / homens

    alunos = alunos + 1

print(f"Total de mulheres altas: {mulheres}")
print(f"Total de homens bons: {porc}")