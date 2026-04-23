listaSorvetes = []   # ["produto", 1]

while True:
    # imprimir itens na tela
    print("Lista de itens:\n")
    if len(listaSorvetes) > 0:
        print("Indice:       Produto:       votos:")
        indice = 0
        for l in listaSorvetes:
            print(f"{indice}             {l[0]}        {l[1]}")
            indice += 1
    else:
        print("Sem Itens")

    # Opçao de escolha
    escolhaSorvete = int(input("Escolha um Produto(-1 para adicionar item)\n=> "))
    
    # Adicionar ou votar item
    if escolhaSorvete == -1:
        sorvete = input("Nome do Produto: ")
        listaSorvetes.append([sorvete, 1])

    elif escolhaSorvete >= 0:
        if len(listaSorvetes) < escolhaSorvete:
            print("Item nao encontrado, tente novamente")
        else:
            listaSorvetes[escolhaSorvete][1] += 1
    # Mais votado
    else:
        ganhador = " "
        ganhadorPontos = 0
        for n in listaSorvetes:
            pontos = n[1]
            if pontos > ganhadorPontos:
                ganhadorPontos = pontos
                ganhador = n[0]

        print("O mais votado foi >>", ganhador)
        break

