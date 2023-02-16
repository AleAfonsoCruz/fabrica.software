a = 80000
b = 200000
ano = 0
print("Quantidade atual de habitantes no país A: 80.000"
	  "\nTaxa de crescimento anual: 3%"
	  "\nQuantidade atual de habitantes no país B: 200.000"
	  "\nTaxa de crescimento anual: 1.5%")
while a <= b:
	a += a * 3/100
	b += b * 0.15/100
	ano +=1
print(" "*60)
print(f"Para que o país A alcance a quantidade de habitantes do país B será necessário {ano} ano(s).")