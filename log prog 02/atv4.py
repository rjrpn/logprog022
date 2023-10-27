# letra_digitada = str(input("Digite uma letra: ")).upper().strip()

# match letra_digitada:
#     case "A":
#         print(f"A letra {letra_digitada} é uma VOGAL.")
#     case "E":
#         print(f"A letra {letra_digitada} é uma VOGAL.")
#     case "I":
#         print(f"A letra {letra_digitada} é uma VOGAL.")
#     case "O":
#         print(f"A letra {letra_digitada} é uma VOGAL.")
#     case "U":
#         print(f"A letra {letra_digitada} é uma VOGAL.")
#     case _:
#         print(f"A letra {letra_digitada} é uma CONSOANTE.")


# CORREÇÃO IMVERTEXTO ABAIXO:
# QUESTÃO 4 BÁSICA:

# letra = str(input("Digite uma letra: "))

# if letra in "aeiou":
#     print("vogal")
# elif letra in "bcdfghjklmnpqrstvxywz":
#     print("consoante")
# else:
#     print("inválido")


# QUESTÃO 4 COMPLEXA:
letra = str(input("Digite uma letra: ")).lower().strip()

if len(letra) == 1:
    if letra in 'aeiou':
        print("é uma vogal")
    elif letra in 'bcdfghjklmnpqrstvxywz':
        print("é uma consoante")
    else:
        print("Caracter inválido, digite uma LETRA meu fi, alfabeto ta ligado?")
else:
    print("Digite apenas UMA letra")