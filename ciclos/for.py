numero_repeticiones = 5
for contador_actual in range(numero_repeticiones):
    if contador_actual == numero_repeticiones - 1:
        print(f"¡Última vez diciendo Hola Mundo! {contador_actual + 1}")
    else:
        print(f"Hola mundo {contador_actual + 1}")
