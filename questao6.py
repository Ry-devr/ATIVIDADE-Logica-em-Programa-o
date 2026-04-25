# A questão pediu para ter duas lista, :(

carros = ["vectra", "peugeot", "uno", "opala", "chevete"]
consumoCarros = [11, 16, 15, 8, 11] # km/L

menorConsumo = 0
carroMConsumo = ''
for n in carros:
    indicecarro = carros.index(n)
    kmLcarro = consumoCarros[indicecarro]
    litrosUsa = 1000 / kmLcarro
    
    if menorConsumo < consumoCarros[indicecarro]:
        menorConsumo = consumoCarros[indicecarro]
        carroMConsumo = n

    print(f"O carro {n}  gasta {litrosUsa:.1f}L de gasolina em 1000km")

print(f"\nE o carro com o menor consumo foi o {carroMConsumo}")
