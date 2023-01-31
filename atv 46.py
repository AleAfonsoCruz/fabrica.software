nome = input("Seu nome: ")
print("-"*15)
sexo = input("Sexo [F/M]: ")
print("-"*15)
estado = int(input("Estado civil \n1- Solteiro(a) \n2- Casado(a) \n3- Viúvo(a)\n"))
if sexo == "F" and estado == 2:
    tempo = int(input("Quanto tempo de casada? "))
    print(f"Seu nome é {nome}, estado civil {estado} e está casada há {tempo} anos.")
else:
    print("Bom saber!")