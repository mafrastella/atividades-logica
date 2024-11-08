idade = int(input("Digite sua idade: "))
preferencia = input("Digite sua preferência de gênero (ação, comédia, drama): ").strip().lower()

if idade >= 18:
    if preferencia == "ação" or preferencia == "comédia":
        recomendacao = "Recomendamos um filme de ação ou comédia para adultos."
    elif preferencia == "drama":
        recomendacao = "Recomendamos um filme de drama para adultos."
    else:
        recomendacao = "Gênero não reconhecido. Tente 'ação', 'comédia' ou 'drama'."
else:
    if preferencia == "ação" or preferencia == "comédia":
        recomendacao = "Recomendamos um filme de ação ou comédia para adolescentes."
    elif preferencia == "drama":
        recomendacao = "Recomendamos um filme de drama para adolescentes."
    else:
        recomendacao = "Gênero não reconhecido. Tente 'ação', 'comédia' ou 'drama'."

print(recomendacao)
