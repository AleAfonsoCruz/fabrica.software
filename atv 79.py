medias = []
medias_sete = 0
notas = 4
for a in range(10):
    media = 0
    for n in range (notas):
        media += float(input(f"Digite a {n+1}º nota do aluno {a+1}: "))
    media /= notas
    medias.append(media)
    if media >=7:
        medias_sete +=1

for a in range(10):
    print(f"Média dos aluno \nAluno {a+1}: {medias[a]}")
print(" "*60)
print(f"{medias_sete} alunos tiveram média maior ou igual a 7.")