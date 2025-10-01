from datetime import datetime

# Pega o ano atual automaticamente
ano_atual = datetime.now().year

# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Calcula a idade
idade = ano_atual - ano_nascimento

# Verifica se fará ou já fez 18 anos
if idade == 18:
    print("Você faz 18 anos neste ano!")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não tem 18 anos.")