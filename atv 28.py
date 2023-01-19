n1 = int(input("Número inteiro:"))
n2 = int(input("Segundo número inteiro:"))
n3 = float(input("Número real:"))

#dobro do primeiro com metade do segundo
dobro1_2 = n1*2 + n2/2
soma1_3 = n1*3 + n3
ele_mesmo3 = n3*n3

print(f"O dobro do n1 com metade do n2:{dobro1_2}")
print(f"O triplo do n1 com a soma do n3:{soma1_3}")
print(f"N3 elevado ao cubo:{ele_mesmo3:.2f}")