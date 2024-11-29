valor_ingresado = int(input("Ingresa un valor: "))
if valor_ingresado > 10:
    print("Es mayor que 10")
    if valor_ingresado > 20:
        print("También es mayor que 20")
elif valor_ingresado > 5:
    print("Es menor que 10")
    
if valor_ingresado % 3 == 0:
    print("El número es divisible por 3")
