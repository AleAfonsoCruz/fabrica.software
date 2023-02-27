caracter = []
print("Digite 10 caracteres")
for c in range (10):
    caracteres = str(input(f"Caracter {c+1}: "))
    caracter.append(caracteres)
print(f"Caracteres: {caracter}")

def consoante(caracteres):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    consoantes = set(consoantes)
    soma = 0
    for c in caracteres:
        if c in consoantes:
            soma += 1
    return soma