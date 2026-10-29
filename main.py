#CALCULO DE POTENCIA DE 2
def potencia_dos():
    num_potencia_dos = int(input("A que potencia quieres elevar el 2: "))
    resultado_potencia=1

    for i in range(num_potencia_dos):
        resultado_potencia=resultado_potencia*2
    print(resultado_potencia)

#CALCULO DE LOGARITMO EN BASE 2
def logaritmo_base_dos():
    num_log_base_dos = float(input("¿A qué número tengo que elevar 2 para obtener: "))

    if num_log_base_dos <= 0:
        print("El numero tiene que ser mayor que 0")
    else:
        bajo = -100
        alto = 100

        for i in range(100):
            resultado_log = (bajo + alto) / 2
            if 2 ** resultado_log > num_log_base_dos:
                alto = resultado_log    # me he pasado
            else:
                bajo = resultado_log    # me he quedado corto

        print("El numero que tengo que elevar a 2 para obtener", num_log_base_dos, "es", resultado_log)


potencia_dos()
logaritmo_base_dos()
