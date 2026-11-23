# in: revisa si algo está dentro de otra cosa
print("o" in "python")  # True → "o" aparece en python
print("f" not in "python")  # True → "f" no aparece en python
print("o" not in "python")  # False → "o" sí aparece, y not in lo invierte
print(3 not in [1, 2, 3])  # False → el 3 sí está en la lista, y not in lo invierte

# Seguridad: revisar que el dominio no esté en la lista de prohibidos
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)  # True → gmail.com no está bloqueado

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)  # False → spam.com está bloqueado


# Listas iguales: == compara el contenido, is compara si son el mismo objeto
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)  # True → mismo contenido
print(x is y)  # False → son dos listas distintas en memoria

# Números pequeños: Python reutiliza el mismo objeto
x = 10
y = 10
print(x == y)  # True → mismo valor
print(x is y)  # True → apuntan al mismo objeto (mismo Id)

# y = x no crea otra lista: las dos variables apuntan al mismo objeto
x = ['a', 'b', 'c']
y = x
print(x == y)  # True → mismo contenido
print(x is y)  # True → son el mismo objeto (mismo Id)

# Revisa que el correo exista (no sea None) y no esté vacío
email = ""
print(email != "")  # False → el correo está vacío

email = "usuario@ejemplo.com"
print(email != "")  # True → el correo tiene contenido

# Revisar que el correo exista (no sea None) y no esté vacío
email = None
# Regla: para None se usa is / is not, nunca == / !=
print(email != None and email != "")  # False → funciona, pero no es lo recomendado
print(email is not None and email != "")  # False, forma correcta, para una buena práctica