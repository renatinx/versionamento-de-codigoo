lista_cidades = []

print("Lista inicial:", lista_cidades)
for i in range(3):
    nome_cidade = input(f"Digite o nome da cidade #{i + 1}: ")
    lista_cidades.append(nome_cidade)
    print("Lista atualizada:", lista_cidades)
