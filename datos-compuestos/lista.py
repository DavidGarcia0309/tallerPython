lista_elementos = ["Hola", 15, True, "Adios"]
print(lista_elementos[0])
print(type(lista_elementos[0]))
print(type(lista_elementos[1]))
print(type(lista_elementos[2]))
print(type(lista_elementos[3]))

lista_elementos[1] = "Marco"
print(type(lista_elementos[1]))

if type(lista_elementos[1]) == str:
    print("El elemento en el índice 1 ahora es una cadena de texto")
else:
    print("El elemento en el índice 1 no es una cadena de texto")
