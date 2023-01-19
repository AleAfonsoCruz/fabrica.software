peso = float(input("Peso dos peixes:"))
excesso = 0
multa = 0

if peso <=50:
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)

else:
    excesso = peso - 50
    multa = excesso * 4
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)

