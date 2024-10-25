import random

def criar_tabuleiro():
    """Cria um tabuleiro 3x3 com um tesouro escondido em uma célula aleatória."""
    grid = [[0, 0, 0] for _ in range(3)]
    tesouro_x, tesouro_y = random.randint(0, 2), random.randint(0, 2)
    grid[tesouro_x][tesouro_y] = 1  # Coloca o tesouro
    return grid

def imprimir_tabuleiro(grid):
    """Imprime o tabuleiro, escondendo o tesouro e mostrando tentativas anteriores."""
    for linha in grid:
        print(' '.join('T' if celula == -1 else '0' for celula in linha))

def jogar():
    grid = criar_tabuleiro()
    tentativas = 0
    encontrou_tesouro = False

    while not encontrou_tesouro:
        imprimir_tabuleiro(grid)
        try:
            x = int(input("Escolha uma linha (0-2): "))
            y = int(input("Escolha uma coluna (0-2): "))
            
            # Verifica se a entrada está dentro dos limites
            if x not in [0, 1, 2] or y not in [0, 1, 2]:
                print("Coordenadas fora dos limites! Tente novamente.")
                continue

            # Verifica se o jogador encontrou o tesouro
            if grid[x][y] == 1:
                print("Parabéns! Você encontrou o 0!")
                encontrou_tesouro = True
            elif grid[x][y] == -1:
                print("Você já tentou aqui. Tente outra posição.")
            else:
                print("Não há tesouro aqui. Tente novamente.")
                grid[x][y] = -1  # Marca a tentativa do jogador
                tentativas += 1

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    print(f"Você encontrou o 0 em {tentativas} tentativas!")

# Para rodar o jogo:

if __name__ == "__main__":
    jogar()
