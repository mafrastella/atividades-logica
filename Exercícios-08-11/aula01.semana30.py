pontuacao = int(input("Digite a pontuação de desempenho do funcionário (0 a 100): "))
presenca = int(input("Digite a porcentagem de presença do funcionário (0 a 100): "))

if pontuacao >= 80:
    if presenca >= 90:
        categoria = "Excelente"
    else:
        categoria = "Bom"
elif 50 <= pontuacao <= 79:
    if presenca >= 75:
        categoria = "Bom"
    else:
        categoria = "Regular"
else:
    categoria = "Ruim"

print(f"A categoria do funcionário é: {categoria}")
