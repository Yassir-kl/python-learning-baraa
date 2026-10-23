# Sin variable: hay que repetir el nombre en cada print
print("Mi nombre es Ricardo")
print("Ricardo está aprendiendo Python")
print("Ricardo quiere convertirse en un experto en Python")

# Para no estar cambiando Ricardo en cada print, es mejor agregar una variable
name = "Ricardo"
print("Mi nombre es", name)
print(name, "está aprendiendo Python")
print(name, "quiere convertirse en un experto en Python")

name = "Yassir"
# Para poder actualizar la variable es recomendable que los prints vayan después
# si no no irán las actualizaciones   
# print("Mi nombre es", name)
# print(name, "está aprendiendo Python")
# print(name, "quiere convertirse en un experto en Python")

name = "Yassir"
language = "JavaScript"
print("Mi nombre es", name)
print(name, "está aprendiendo", language)
print(name, "quiere convertirse en un experto en", language, "y conseguir trabajo")

print("===== PYTHON CHALLENGE =====\n")
# En este challenge usaremos "+" ya que queremos imprimir algo sin espacios y la "," da espacios
dominio = "datawithbaraa.com"
# print("info@", dominio)
# print("support", dominio)
# print("www.", dominio)
print("info@" + dominio)
print("support@" + dominio)
print("www." + dominio)