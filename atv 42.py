lata1 = 0.35
garrafa1 = 0.6
garrafa2 = 2

print("Gui-Cola Refrigerantes"
      "\n1- Lata 350ml"
      "\n2- Garrafa 600ml"
      "\n3- Garrafa 2L")
print("-"*25)
lat = int(input("Quantidade de latas 350 ml: "))
gar600 = int(input("Quantidade de garrafa 600ml: "))
gar2 = int(input("Quantidade de garrafa 2L: "))

total = lata1*lat + garrafa1*gar600 + garrafa2*gar2

print(f"Quantidade total de refrigerante é de: {total:.1f} L")