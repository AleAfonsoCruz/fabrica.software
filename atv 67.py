while True:
    nome = str(input("Digite o nome de usuário: "))
    senha = input("Digite sua senha de acesso: ")
    if nome != senha:
        print("Acesso concedido!")
        break
    print("Senha não pode ser igual ao nome. Altere sua senha.")
