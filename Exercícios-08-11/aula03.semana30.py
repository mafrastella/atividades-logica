precos = {
    "entrada": 20,
    "prato principal": 50,
    "sobremesa": 15
}

total_pedido = 0

while True:
    tipo_prato = input("Digite o tipo de prato (entrada, prato principal, sobremesa) ou 'sair' para finalizar: ").strip().lower()
    
    if tipo_prato == "sair":
        break

    if tipo_prato in precos:
        quantidade = int(input(f"Digite a quantidade de {tipo_prato}s: "))
        total_pedido += precos[tipo_prato] * quantidade
    else:
        print("Tipo de prato inválido! Tente 'entrada', 'prato principal' ou 'sobremesa'.")

if total_pedido > 100:
    total_com_desconto = total_pedido * 0.9
    print(f"O total do pedido com desconto é: R$ {total_com_desconto:.2f}")
else:
    print(f"O total do pedido é: R$ {total_pedido:.2f}")
