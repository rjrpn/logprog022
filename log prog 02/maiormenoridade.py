import datetime

ano = int(input("Digite o ano que você nasceu."))

ano_atual = datetime.datetime.now().year
idade = ano_atual - ano

if ano >= 18:
    print(f"Você tem {idade} anos, então é maior de idade")
else:
    print(f"Você tem {idade} anos, então é menor de idade")