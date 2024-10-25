import random

def gerar_tabuleiro():
    # Cria uma matriz 3x3 com todos os valores inicialmente definidos como 0 (terreno vazio)
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    
    # Define uma posição aleatória para o tesouro
    linha_tesouro = random.randint(0, 2)
    coluna_tesouro = random.randint(0, 2)
    
    # Coloca o tesouro na posição aleatória
    tabuleiro[linha_tesouro][coluna_tesouro] = 1
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    # Exibe o tabuleiro sem revelar a posição do tesouro
    for linha in tabuleiro:
        print(["X" if celula == 0 else "?" for celula in linha])

def jogar():
    tabuleiro = gerar_tabuleiro()
    tentativas = 0
    encontrou = False
    
    print("Bem-vindo ao Encontre o Tesouro!")
    print("O tabuleiro é 3x3. Encontre o tesouro no menor número de tentativas possível.\n")
    
    while not encontrou:
        mostrar_tabuleiro(tabuleiro)
        
        # Solicita ao jogador para escolher uma linha e coluna
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue
        
        # Verifica se a entrada está dentro dos limites
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Escolha fora dos limites! Tente novamente.")
            continue
        
        tentativas += 1
        
        # Verifica se o tesouro foi encontrado
        if tabuleiro[linha][coluna] == 1:
            encontrou = True
            print("\nParabéns! Você encontrou o tesouro!")
            print(f"Você levou {tentativas} tentativa(s) para encontrar o tesouro.")
        else:
            print("Nada aqui... Continue procurando.\n")

if __name__ == "__main__":
    jogar()
