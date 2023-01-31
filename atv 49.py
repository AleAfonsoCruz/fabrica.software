cotacao = float(input("Digite a cotação do dólar atualmente: "))
real = float(input("Valor em real (R$) a ser convertido: "))
print(f"Cotação do dólar: U${cotacao:.2f}; \nValor em real: R${real:.2f}; \nReal(R$) em dólar(U$): R${real*cotacao:.2f}")