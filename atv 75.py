lista = []
print ("Digite 10 números reais: ")
for n in range(10):
  lista.append(input("Número" + str(n+1) + ': '))
lista.reverse()
print (lista)