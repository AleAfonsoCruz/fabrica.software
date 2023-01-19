l1 = int(input("Tamanho do lado 1:"))
l2 = int(input("Tamanho do lado 2:"))
l3 = int(input("Tamanho do lado 3:"))

if ((l1==l2)and(l1==l3)):
    print("Se um triângulo, é equilátero.")
elif ((l1==l2 and l1!=l3)|(l2==l1 and l2!=l3)|(l3==l1 and l3!=l2)):
    print("Se um triângulo, é isósceles.")
else:
    print("Se um triângulo, é escaleno.")