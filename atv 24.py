sanduiche = int(input("Digite a quantidade de sanduiche desejada:"))
queijo = 0.05
presunto = 0.05
hamburguer = 0.1

queijo_kg = (2*queijo)*sanduiche
presunto_kg = presunto*sanduiche
hamburguer_kg = hamburguer*sanduiche
print(f"A quantidade necessária é de: {queijo_kg} kg de queijo.")
print(f"A quantidade necessária é de: {presunto_kg} kg de presunto.")
print(f"A quantidade necessária é de: {hamburguer_kg} kg de hamburguer.")