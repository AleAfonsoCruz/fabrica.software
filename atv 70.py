atletas = []
while True:
    nome = input("Digite o nome do atleta (0 para finalizar): ")
    if nome == "0":
        break
    atleta = {
        "nome": nome,
        "saltos":[],
        "media dos saltos": 0,
        "melhor_salto": 0,
        "pior_salto": 0,
    }
    for s in range(5):
        atleta.get("saltos").append(float(input(f"Distância do {s+1}º salto: ")))
    atleta.get("saltos").sort()
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    atleta["melhor_salto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3
    
    print(f"Melhor salto: {atleta.get('melhor_salto'):.1f} m")
    print(f"Pior salto: {atleta.get('pior_salto'):.1f} m")
    print(f"Media dos saltos: {atleta.get('media'):.1f} m")

print("\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")