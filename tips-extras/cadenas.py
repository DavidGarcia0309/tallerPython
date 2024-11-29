cadena = "Hola"
cadena2 = cadena.lower()
print(dir(cadena))
print(cadena)
print(cadena2.capitalize())

cadena_larga = "Hola mi nombre es david estamos en un curso de python Bienvenido"

print(cadena_larga.find("david"))
print(cadena_larga.find("z"))
print(cadena_larga.index("z"))

print(cadena.isalpha())
print(cadena.isnumeric())
print(cadena_larga.count("a"))
print(len(cadena_larga))
print(cadena_larga.split(" "))