idades = []
alturas = []
for p in range (5):
    idade = int(input(f"Idade da {p+1}º pessoa: "))
    altura = float(input(f"Altura da {p+1}º pessoa: "))
    idades.append(idade)
    alturas.append(altura)
print(" "*60)
print(f"Idades e alturas \nIdades ordem lida: {idades} \nAlturas ordem lida: {alturas}")
print(" "*60)
print(f"Idades ordem inversa: {idades[::-1]} \nAlturas ordem inversa: {alturas[::-1]}")
