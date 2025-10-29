nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.strip().split()
if len(partes) >= 2:
    
    print(partes[1])
else:
    print(" digite pelo menos nome e sobrenome.")