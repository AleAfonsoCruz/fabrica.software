cliente = input("Digite seu nome:")
conta = int(input("Digite o número da sua conta:"))
debito = float(input("Digite seu valor de débito:"))
credito = float(input("Digite seu valor de crédito:"))
saldo = (debito+credito)
print("Seu saldo total é de: {}".format(saldo))

if (saldo>=1):
    print (f"Cliente {cliente} seu saldo atual de {saldo:.1f} é positivo.")

if (saldo<=0):
    print (f"Cliente {cliente} seu saldo atual de {saldo:.1f} é negativo.")
