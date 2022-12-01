kmporl = float(input("Qual autonomia do seu carro por km?:"))
metragem = float(input("Quantos km irá percorrer?:"))
valor = float(input("Qual o valor da gasolina por litro?:"))

gasto = (metragem/kmporl)*valor

print("Gasto:",gasto)