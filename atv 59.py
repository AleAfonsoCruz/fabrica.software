num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num2<num1:
	for n in range(num2+1,num1,1):
		print(n)

else:
	for n in range(num1+1,num2,1):
		print(n)