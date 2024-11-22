soma = 0
contagem = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero
    contagem += 1
if contagem > 0:
    media = soma / contagem
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
