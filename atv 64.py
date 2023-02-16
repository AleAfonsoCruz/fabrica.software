maior = 0
menor = 0
count = 0
veiculos = 0
acidentes = 0
veiculos2k = 0
cidade_maior = cidade_menor = ""

for c in range(1, 6):
    cidade = str(input("Digite o nome da cidade: "))
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos: "))
    acidentes = int(input("Número de acidentes de trânsito: "))
    print(" "*60)

    veiculos += veiculos
    acidentes += acidentes

    if acidentes > maior:
        maior = acidentes
        cidade_maior = cidade

    if acidentes < menor or c == 1:
        menor_indice = acidentes
        cidade_menor = cidade

    if veiculos < 2000:
        veiculos2k += acidentes
        count += 1

media_cidades = acidentes / c
media_2k = veiculos2k / count

print("-"*60)
print(f"Cidade com menor índice: {cidade_menor} \nIndícide de: {menor}")
print(f"Cidade com maior índice: {cidade_maior} \nIndíce de: {maior}")
print(f"Média de veiculos nas cinco cidades: {media_cidades}")
print(f"Média de acidentes nas cidades com menos de 2000: {media_2k}")