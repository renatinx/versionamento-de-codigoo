from datetime import datetime


ano_atual = datetime.now().year


ano_nascimento = int(input("Digite o ano em que você nasceu: "))


idade = ano_atual - ano_nascimento


if idade == 18:
    print("Você faz 18 anos neste ano!")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não tem 18 anos.")