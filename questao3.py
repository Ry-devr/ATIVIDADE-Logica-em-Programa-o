listaProdutos = []

for n in range(10):
    produtos = input("\nDigite o nome do produto\n=> ")
    preçoProduto = float(input("Digite o preço\n=> "))

    listaProdutos.append([produtos, preçoProduto])

print(listaProdutos[::-1])
