semaforo = str(input("Digite uma cor do sinal de trânsito: "))

match semaforo:
    case "vermelho":
        print("PARE")
    case "amarelo":
        print("ATENÇÃO")
    case "verde":
        print("SIGA")
    case _:
        print("Inválido")