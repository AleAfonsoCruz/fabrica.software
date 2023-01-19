#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
#que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

A = int(input("Quantos litros de álcool?"))
G = int(input("Quantos litros de gasolina?"))

vendidos = A+G
A_alcool = 2.50*A
G_gasolina = 1.90*G
A_desconto3 = A_alcool*3/100
A_desconto5 = A_alcool*5/100
G_desconto4 = G_gasolina*4/100
G_desconto6 = G_gasolina*6/100

if A <=20:
    print(f"São {A} L de álcool, desconto de R${A_desconto3:.1f}")
if A>20:
    print(f"São {A} L de álcool, desconto de R${A_desconto5:.1f}")