numero_ingresado = int(input("Ingrese un número: "))

if numero_ingresado > 0:
    print("El número es positivo")
elif numero_ingresado < 0:
    print("El número es negativo")
else:
    print("El número es cero")

if numero_ingresado % 5 == 0:
    print("El número es divisible por 5")
