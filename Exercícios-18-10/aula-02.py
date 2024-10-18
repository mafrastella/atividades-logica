import numpy as np

# Matriz de disponibilidade dos funcionários (1 disponível, 0 indisponível)
# Linhas: Funcionários, Colunas: Projetos
A = np.array([
    [1, 0],  # Funcionário 1 disponível para Projetos 1
    [1, 1],  # Funcionário 2 disponível para Projetos 1 e 2
    [0, 1]   # Funcionário 3 disponível apenas para o Projeto 2
])

# Matriz de habilidades dos funcionários (nível de habilidade de 0 a 10)
# Linhas: Funcionários, Colunas: Habilidades
H = np.array([
    [8, 6, 7],  # Funcionário 1 (Habilidade 1, 2 e 3)
    [5, 9, 3],  # Funcionário 2 (Habilidade 1, 2 e 3)
    [7, 5, 8]   # Funcionário 3 (Habilidade 1, 2 e 3)
])

# Matriz de requisitos dos projetos (quantidade de habilidade necessária)
# Linhas: Projetos, Colunas: Habilidades
P = np.array([
    [6, 5, 7],  # Projeto 1 (Requisitos Habilidade 1, 2 e 3)
    [5, 7, 9]   # Projeto 2 (Requisitos Habilidade 1, 2 e 3)
])

# Função para alocar recursos
def alocar_recursos(A, H, P):
    # Matriz para armazenar a alocação final
    alocacao = np.zeros((A.shape[0], P.shape[0]))  # Funcionários x Projetos
    
    # Itera sobre cada projeto
    for j in range(P.shape[0]):
        print(f"\nVerificando Projeto {j+1} com requisitos {P[j]}")
        for i in range(A.shape[0]):
            # Verifica se o funcionário está disponível para o projeto e se suas habilidades atendem aos requisitos
            if A[i, j] == 1 and np.all(H[i] >= P[j]):
                print(f"Alocando Funcionário {i+1} ao Projeto {j+1}")
                alocacao[i, j] = 1  # Aloca funcionário ao projeto
                A[i, j] = 0  # Marca o funcionário como não disponível para esse projeto
                break  # Passa para o próximo projeto
            else:
                print(f"Funcionário {i+1} não pode ser alocado ao Projeto {j+1}")

    return alocacao

# Executa a alocação
resultado_alocacao = alocar_recursos(A.copy(), H, P)

# Exibir os resultados
print("\nAlocação de funcionários aos projetos:")
print(resultado_alocacao)








