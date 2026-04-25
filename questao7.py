mesPorexteco = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

dia = int(input("Dia:  "))
while dia > 31 or dia <= 0:
    dia = int(input("Dia:  "))

mes = int(input("Mes:  "))
while mes > 12 or mes <= 0:
    mes = int(input("Mes:  "))

ano = int(input("ano:  "))

print(f"{dia} de {mesPorexteco[mes - 1]} de {ano}")
