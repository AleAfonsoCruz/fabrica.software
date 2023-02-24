atletas = []
while True:
    nome = str(input("Digite o nome do atleta (ou Enter para finalizar): "))
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "notas": [],
        "melhorNota": 0,
        "piorNota": 0,
        "media": 0,
    }
    for n in range(7):
        atleta.get("notas").append(float(input(f"{n+1}º nota: ")))
    atleta.get("notas").sort()
    atleta["piorNota"] = atleta.get("notas").pop(0)
    atleta["melhorNota"] = atleta.get("notas").pop()
    atleta["media"] = sum(atleta.get("notas"))/5

    print(f"Melhor nota: {atleta.get('melhorNota'): } ")
    print(f"Pior nota: {atleta.get('piorNota'): } ")
    print(f"Media das notas: {atleta.get('media'): } ")

print("\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.f}")