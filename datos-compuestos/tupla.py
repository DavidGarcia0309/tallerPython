tupla_elementos = ('Hola', 15, True, "Adios")

print(type(tupla_elementos[0]))
print(type(tupla_elementos[1]))
print(type(tupla_elementos[2]))
print(type(tupla_elementos[3]))

print(tupla_elementos)

if type(tupla_elementos[0]) == str:
    print("El primer elemento es una cadena de texto")
else:
    print("El primer elemento no es una cadena de texto")
