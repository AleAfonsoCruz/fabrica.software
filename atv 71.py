while True:
    num = int(input("Digite um número inteiro positivo: "))
    if num <0:
        print("Número está negativo, digite novamente.")
    else:
        num = str(num)
        reverso = num[::-1]
        print(f"Número ao contrário: {reverso}")
        break