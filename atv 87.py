print("PESO DA ENCOMENDA              VALOR"
      "\n   500 g ou menos            R$1,10"
      "\n   >de 500 - 2 kg            R$2,20"
      "\n   >de 2kg - 10 kg           R$3,70"
      "\n   >de 10 kg                 R$5,00 + 3,80/kg se ultrapassar 10kg")
print(" "*60)
produto = int(input("Digite o peso em g da encomenda: "))
produto10 = 5 + ((produto-10000)/1000) *3.8
if produto <=500:
    print("O valor de envio da sua encomenda é de: R$1,10")
if produto >500 and produto <=2000:
    print("O valor de envio da sua encomenda é de: R$2,20")
if produto >2000 and produto <=10000:
    print("O valor de envio da sua encomenda é de: R$3,70")
if produto >10000:
    print(f"O valor de envio da sua encomenda é de: R${produto10}")