alunosNotasBaixa = []

for n in range(10):
    nome = input("\nnome do aluno=> ")

    nota = -1
    while nota > 10 or nota < 0:
        nota = float(input("Nota=> "))

    if nota < 7:
        alunosNotasBaixa.append(nome)

print("\nALUNOS COM NOTA BAIXA:")
for n in alunosNotasBaixa:
    print(n)
