ano_nascimento = int(input("Digite o ano em que joao nasceu: "))


ano_atual = 2025


idade = ano_atual - ano_nascimento

if idade == 18:
    print("joao faz 18 anos este ano.")
elif idade > 18:
    print("joao já fez 18 anos .")
else:
    print("joao ainda não fez 18 anos.")