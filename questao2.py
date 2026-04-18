numero = int(input("Digita um numero: "))

# FOR
numeroFatorial = 1
for n in range(1, numero+1):
    numeroFatorial *= n

print(numeroFatorial)

# WHILE
n = 1
numeroFatorialWhile = 1 
while n <= numero:
    numeroFatorialWhile *= n
    n += 1

print(numeroFatorialWhile)

# FUNÇAO RECURSIVA
def fatoria(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatoria(num-1)

print(fatoria(numero))

