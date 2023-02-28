inteiros = []
par = []
impar = []
num = 0

print("Digite 20 Números Inteiros")
for i in range(20):
  inteiros.append(int(input('Número ' + str(i+1) + ': ')))
  num = inteiros[i]
  
  if num %2 == 0:
    par.append(num)
  else:
    impar.append(num)

print(f"Números: {inteiros} \nPares: {par} \nÍmpares: {impar}")
