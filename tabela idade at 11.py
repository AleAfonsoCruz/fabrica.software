nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if idade <= 2:
    print("De acordo com sua idade você é bebê.")
if idade >=3 and idade <=11:
    print("De acordo com sua idade você é criança.")
if idade >=12 and idade <=21:
    print("De acordo com sua idade você é jovem.")
if idade >=22 and idade <=64:
    print("De acordo com sua idade você é adulto.")
if idade >=65 and idade <=100:
    print("De acordo com sua idade você é idoso.")
if idade >101:
    print("De acordo com sua idade você é muito velhinho.")