while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    if numero < 0:
        print("Programa encerrado.")
        break
    if numero < 2:
        print(f"{numero} não é considerado primo.")
        continue
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
