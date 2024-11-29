numero_ingresado = int(input("Ingrese un número: "))
limite_superior = numero_ingresado

for contador_actual in range(limite_superior):
    if (contador_actual + 1) % 2 == 0:
        print(f"{contador_actual + 1} es un número par")
    else:
        print(contador_actual + 1)
