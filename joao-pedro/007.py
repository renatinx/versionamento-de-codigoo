cidades = []
for i in cidades:
    nome = input(f"Digite o nome da cidade {i + 1}: ")
    CLOSE = 'SAIR'
    if nome == CLOSE:
        break
    else:
        cidades.append(nome)
    print("Lista atualizada de cidades:", cidades)

