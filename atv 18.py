valor_hora = float(input("Digite o valor da hora:"))
qntd_hora = float(input("Digite a quantidade de horas trabahadas:"))
salarioBruto = valor_hora*qntd_hora

if salarioBruto <=900:
    ir = 0.0
elif salarioBruto <= 1500:
    ir = 0.05
elif salarioBruto <=2500:
    ir = 0.10
else:
    ir = 0.20

IR = salarioBruto * (ir/100)
INSS = salarioBruto * (10/100)
FGTS = salarioBruto * (11/100)
descontos = IR + INSS
salarioLiquido = salarioBruto - descontos

print(f"Salário Bruto R$ {salarioBruto:.2f}")
print(f"(-) IR (5%) R$ {IR:.2f}")
print(f"(-) INSS (10%) R$ {INSS:.2f}")
print(f"FGTS (11%) R$ {FGTS:.2f}")
print(f"Descontos R$ {descontos:.2f}")
print(f"Salário Líquido R$ {salarioLiquido:.2f}")