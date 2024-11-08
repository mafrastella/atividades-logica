quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

soma_notas = 0

for i in range(1, quantidade_alunos + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma_notas += nota

media = soma_notas / quantidade_alunos

print(f"A média das notas da turma é: {media:.2f}")

