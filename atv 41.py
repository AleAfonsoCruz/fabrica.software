conta = float(input("Digite o valor total da conta: "))
valor_ale = conta - 2*conta//3 #Duas barras não considera o resto na divisão
print(f"Uma conta de R${conta:.2f} resulta em {conta//3:.2f} para Joceyr e Thiago, R${valor_ale:.2f} para Alexandre.")
