nombre_usuario = "David"
edad_usuario = 19

print(nombre_usuario)
print(edad_usuario)

nombre_usuario = 19
edad_usuario = "David"

print(nombre_usuario)
print(edad_usuario)

if isinstance(nombre_usuario, str):
    print("El nombre es ahora una cadena de texto")
else:
    print("El nombre ya no es una cadena de texto")

if isinstance(edad_usuario, int):
    print("La edad es ahora un número entero")
else:
    print("La edad ya no es un número entero")
