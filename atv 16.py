n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

if n1>n2 and n1>n3:
    print("O primeiro número digitado é maior")
if n2>n1 and n2>n3:
    print("O segundo número digitado é maior")
if n3>n1 and n3>n2:
    print("O terceiro número digitado é maior")

if n1<n2 and n1<n3:
    print("O primeiro número digitado é menor")
if n2<n1 and n2<n3:
    print("O segundo número digitado é menor")
if n3<n1 and n3<n2:
    print("O terceiro número digitado é menor")