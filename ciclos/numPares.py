numero_ingresado = int(input("Ingrese un número: "))
limite_superior = numero_ingresado

for contador_actual in range(limite_superior):
    if contador_actual % 5 == 0 and contador_actual != 0:
        print(f"El número {contador_actual} es múltiplo de 5")
    elif contador_actual % 2 == 0:
        print(f"El número {contador_actual} es par")
    else:
        print(f"El número {contador_actual} es impar")
