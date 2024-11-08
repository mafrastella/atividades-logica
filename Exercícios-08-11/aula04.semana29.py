inventario = {}

print("Bem-vindo ao sistema de gerenciamento de inventário!")
print("Escolha uma das opções a seguir:")
print("1 - Adicionar produto")
print("2 - Remover produto")
print("3 - Exibir inventário")
print("4 - Sair")

while True:
   
    acao = input("\nDigite o número da ação desejada: ")

   
    if acao == "1":
        
        produto = input("Digite o nome do produto a ser adicionado: ")
        preco = float(input(f"Digite o preço de '{produto}': R$ "))
        inventario[produto] = preco
        print(f"'{produto}' foi adicionado ao inventário com o preço de R$ {preco:.2f}.")

    elif acao == "2":
       
        produto = input("Digite o nome do produto a ser removido: ")
        if produto in inventario:
            del inventario[produto]
            print(f"'{produto}' foi removido do inventário.")
        else:
            print(f"'{produto}' não está no inventário.")

    elif acao == "3":
        
        if inventario:
            print("Inventário de produtos:")
            for produto, preco in inventario.items():
                print(f"{produto}: R$ {preco:.2f}")
        else:
            print("O inventário está vazio.")

    elif acao == "4":
        
        print("Saindo do sistema de inventário. Até mais!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
