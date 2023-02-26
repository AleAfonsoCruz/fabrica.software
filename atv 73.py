x = " "
votos = [0,0,0,0,0,0]
print("Candidato 1: João (14) \nCandidato 2: Pedro (18) \nCandidato 3: Tiago (20) \nCandidato 4: Lucas (15)")
print(" "*60)
while True:
    voto = input("Digite o número do candidato: \nou 0:Nulo \n1:Branco \n ")
    print(" "*60)
    match (voto):
        case 14:
            votos = votos[1]+ 1
        case 18:
            votos = votos[2]+ 1
        case 20:
            votos = votos[3]+ 1
        case 15:
            votos = votos[4]+ 1
        case 0:
            votos = votos[5]+ 1
        case 1:
            votos = votos[6]+ 1
    
    x = input("Deseja votar novamente? ")
    if x == "N":
        break

print(f"O Candidato João teve {votos[0]} votos")  
print(f"O Candidato Pedro teve {votos[1]} votos")
print(f"O Candidato Tiago teve {votos[2]} votos")
print(f"O Candidato Lucas teve {votos[3]} votos")
print(f"{votos[5]} votos em branco")
print(f"{votos[4]} votos nulos")
