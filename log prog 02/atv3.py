# letra = str("Digite o sexo do usuário: ")

# if letra == "F" or letra == "Feminino" or letra == "FEMININO" or "feminino":
#     print("O Sexo informado é FEMININO")
# elif letra == "M" or letra == "Masculino" or "MASCULINO" or "masculino":
#     print("O Sexo informado é MASCULINO")

# QUESTÃO 3:

sexo = str(input("""
Digite o seu sexo: 
F - Feminino
M - Masculino
""")).upper().strip()
# upper transforma tudo em uppercase(maiusculo) e strip tira o espaçamento a esquerda e direita da string

if sexo == 'F' or sexo == 'FEMININO':
    print("F - Feminino")
elif sexo == "M" or sexo == 'MASCULINO':
    print("M - Masculino")
else:
    print("Alternativa inválida")