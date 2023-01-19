salario = float(input("Digite seu salário:"))
vendas = float(input("Digite o valor de vendas total:"))

comissao = vendas *4/100
print(f"O valor da comissão é de R$: {comissao:.2f}")
valor_final = salario + comissao
print(f"O valo final é de R$:{valor_final:.2f}")