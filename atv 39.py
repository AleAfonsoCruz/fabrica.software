dia = int(input("Dia: "))
mes = int(input("Mês: "))
if mes >=1 and mes <=12 and dia >= 1 and dia <=30 :
    print(f"Se passaram {dia+30*(mes-1)} dia(s)")
else:
    print("Mês ou dia inválido.")