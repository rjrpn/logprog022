semaforo = str(input("Digite uma cor do sinal de trânsito: "))

if semaforo == "vermelho" or semaforo == "VERMELHO" or semaforo == "red":
    print("PARE")
elif semaforo == "amarelo":
    print("ATENÇÃO")
elif semaforo == "verde":
    print("Siga")
else:
    print("Inválido")