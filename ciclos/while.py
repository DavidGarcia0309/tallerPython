limite_repeticiones = 5
contador_actual = 0

while contador_actual < limite_repeticiones:
    if contador_actual == 3:
        print("¡Llegamos al número 3!")
    else:
        print(f"Hola Mundo {contador_actual}")
    contador_actual += 1
