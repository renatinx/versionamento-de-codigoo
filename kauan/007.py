LIMITI = 10000

lista_cidades = []

print("Lista inicial:", lista_cidades)

while True:
    nome_cidade = input(f"Digite o nome da cidade (ou 'parar' para sair): ")
    lista_cidades.append(nome_cidade)
    print("Lista atualizada:", lista_cidades)

    if nome_cidade.lower() == 'sair':
        break






