quantidade = int(input("Digite a quantidade de peças compradas: "))
preco_unitario = float(input("Digite o preço unitário da peça: "))

preco_total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = 0
elif 6 <= quantidade <= 10:
    desconto = 0.10  
else:
    desconto = 0.20  

valor_desconto = preco_total * desconto
preco_final = preco_total - valor_desconto

print(f"Preço total: R$ {preco_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
