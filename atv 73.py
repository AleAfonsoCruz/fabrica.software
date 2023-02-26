joao = 0 
pedro = 0 
tiago = 0
lucas = 0
voto_em_branco = 0
voto_nulo = 0 
votos = [0,0,0,0,0,0]
print("Candidato 1: João (14) \nCandidato 2: Pedro (18) \nCandidato 3: Tiago (20) \nCandidato 4: Lucas (15)")
print(" "*60)
while True:
    voto = input("Digite o número do candidato: \nou 0:Nulo \n1:Branco ")
    
    if voto == " ":
        break

    match voto:
        case 14:
            joao = joao + 1
        case 18:
            pedro = pedro + 1
        case 20:
            tiago = tiago + 1
        case 15:
            lucas = lucas + 1
        case 0:
            voto_nulo = voto_nulo + 1
        case 1:
            voto_em_branco = voto_em_branco + 1

print(f"O Candidato João teve {joao} votos")  
print(f"O Candidato Pedro teve {pedro} votos")
print(f"O Candidato Tiago teve {tiago} votos")
print(f"O Candidato Lucas teve {lucas} votos")
print(f"{voto_em_branco} votos em branco")
print(f"{voto_nulo} votos nulos")