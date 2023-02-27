notas = []
media = 0
print("Informe 4 notas")
for n in range(4):
  notas.append(float(input(str(n+1) + "nota" + ': ')))
  media += notas[n]
media = media/4
print(" "*60)
print (f"Notas: {notas}")
print(f"Média: {media:.1f}")