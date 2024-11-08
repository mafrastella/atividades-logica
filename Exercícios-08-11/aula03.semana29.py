lista_compras = []


print("Bem-vindo ao aplicativo de lista de compras!")
print("Escolha uma das opções a seguir:")
print("1 - Adicionar item")
print("2 - Remover item")
print("3 - Exibir lista de compras")
print("4 - Sair")

while True:
    
    acao = input("\nDigite o número da ação desejada: ")

   
    if acao == "1":
        
        item = input("Digite o nome do item a ser adicionado: ")
        lista_compras.append(item)
        print(f"'{item}' foi adicionado à lista.")

    elif acao == "2":
        
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print(f"'{item}' não está na lista de compras.")

    elif acao == "3":
       
        if lista_compras:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        else:
            print("A lista de compras está vazia.")

    elif acao == "4":
        
        print("Saindo do aplicativo. Até mais!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
