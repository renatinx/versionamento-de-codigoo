lista_cidades = []
print("lista de cidades")


while True:
  cidade =  input("Digite o nome da cidade para adiciona-la ou 'sair' para finalizar: ")
  lista_cidades.append(cidade)  
  print(f"Lista atualizada: {lista_cidades}")
  print(f"Você digitou: {cidade}")
  if cidade.lower () == "sair" :
    print("o codigo foi encerrado")
    break
  

