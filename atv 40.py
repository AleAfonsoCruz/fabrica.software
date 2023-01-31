salario = 1200
print("Salário R$1200,00.")
c1 = 200*2/100+200
c2 = 120*2/100+120
print(f"Contas a ser pagas:\nConta 1 R$200,00. Com juros {c1} \nConta 2 R$120,00. Com juros {c2}.")
pagam = c1+c2
rest = salario-pagam
print(f"Valor restante do salário é de R${rest:.1f}")