import random

def criar_tabuleiro():
    # Cria uma matriz 3x3 com todos os elementos sendo 1
    tabuleiro = [[1 for _ in range(3)] for _ in range(3)]
    
    # Define uma posição aleatória para o zero
    linha_zero = random.randint(0, 2)
    coluna_zero = random.randint(0, 2)
    tabuleiro[linha_zero][coluna_zero] = 0
    
    return tabuleiro, (linha_zero, coluna_zero)

def imprimir_tabuleiro(tabuleiro):
    # Exibe o tabuleiro para o jogador, ocultando o zero
    for linha in tabuleiro:
        for elemento in linha:
            # Exibe 1 no lugar do zero para ocultá-lo
            print(1, end=" ")
        print()  # Quebra de linha para cada nova linha da matriz

def jogar():
    # Cria o tabuleiro e recebe a posição do zero
    tabuleiro, posicao_zero = criar_tabuleiro()
    
    # Inicializa o número de tentativas
    tentativas = 0
    
    print("Bem-vindo ao Caça ao Zero! Encontre o zero na matriz 3x3.")
    imprimir_tabuleiro(tabuleiro)

    while True:
        # Recebe as coordenadas do jogador
        try:
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros.")
            continue
        
        # Verifica se a entrada está dentro do intervalo válido
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Coordenadas fora do limite! Tente novamente.")
            continue

        tentativas += 1
        
        # Verifica se o jogador encontrou o zero
        if (linha, coluna) == posicao_zero:
            print(f"Parabéns! Você encontrou o zero em {tentativas} tentativas.")
            break
        else:
            print("Não encontrou o zero! Tente novamente.")
            imprimir_tabuleiro(tabuleiro)

# Executa o jogo
jogar()
