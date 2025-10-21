lista_cidades = ["Belo Horizonte"]

print("Lista inicial:", lista_cidades)
for i in range(3):
    nova_cidade = input(f"Digite o nome da cidade #{i + 1}: ")
    lista_cidades.append(nova_cidade)
    print("Lista atualizada:", lista_cidades)
less
Lista inicial: ['Belo Horizonte']
Digite o nome da cidade #1: Ribeirão das Neves
Lista atualizada: ['Belo Horizonte', 'Ribeirão das Neves']
Digite o nome da cidade #2: Contagem
Lista atualizada: ['Belo Horizonte', 'Ribeirão das Neves', 'Contagem']
Digite o nome da cidade #3: Betim
Lista atualizada: ['Belo Horizonte', 'Ribeirão das Neves', 'Contagem', 'Betim']
