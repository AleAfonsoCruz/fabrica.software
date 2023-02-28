nome = input("Nome do aluno:\n")
disciplina = input("Disciplina:\n")
nota1 = float(input("Nota prova 1:\n"))
nota2 = float(input("Nota prova 2:\n"))
nota3 = float(input("Nota prova 3:\n"))

media = (nota1+nota2+nota3)/3

if(media >=6):
    print(f"As notas foram: {nota1}, {nota2} e {nota3} média do" f" aluno {nome} foi {media:.1f}, aluno APROVADO.")
else:
    print(f"As notas foram: {nota1}, {nota2} e {nota3} média do" f" aluno {nome} foi {media:.1f}, aluno NÃo foi aprovado.")
