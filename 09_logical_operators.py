# logical operations

# and: las dos condiciones deben ser True
print(3 > 1 and 5 < 1)  # False → 5 < 1 no se cumple
print(3 > 1 and 5 > 1)  # True → se cumplen las dos

# or: basta con que una condición sea True
print(3 > 1 or 5 < 1)  # True → 3 > 1 se cumple
print(3 < 1 or 5 < 1)  # False → ninguna se cumple

# Ejemplo real para entender cuando usamos esas cosas

# revisa si el sistema está sobrecargado (basta con que uno pase de 90)
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)  # True → la memoria pasa de 90

cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)  # False → no pasan de 90

# revisar si están correctas las credenciales

email = True
password = False

print(email and password)  # False → la contraseña está mal

email = True
password = True

print(email and password)  # True → los dos están bien

email = False
password = False

print(email and password)  # False → los dos están mal

# Datos guardados (en una página real vendrían de una base de datos)
email_guardado = "ryov@gmail.com"
password_guardado = "123456789"

# Caso 1: el usuario escribe los datos correctos
email = "ryov@gmail.com"
password = "123456789"
print(email == email_guardado and password == password_guardado)  # True → coinciden los dos

# Caso 2: el usuario se equivoca en la contraseña
password = "123456"
print(email == email_guardado and password == password_guardado)  # False → la contraseña no coincide

# not: invierte el resultado (True → False, False → True)

print(not 3 > 2)  # False
print(not True)  # False
print(not False)  # True
print(not not False)  # False → un not cancela al otro (no tiene sentido usarlo)

name = ""
print(not name)  # True → el nombre está vacío
print(not 0)  # True → 0 cuenta como False

# allow access only if the user is logged in
# or they are a guest
# but they must not be banned

# Tarea: permitir el acceso si el usuario inició sesión o es invitado,
# pero no debe estar baneado

# Caso 1: inició sesión y no está baneado
is_logged_in = True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned)  # True → puede entrar

# Caso 2: inició sesión, pero está baneado 
is_logged_in = True
is_guest = False
is_banned = True

# ERROR: and va antes que or, así que "not baneado" solo se revisa para invitados
print(is_logged_in or is_guest and not is_banned)  # True → ¡lo deja entrar estando baneado!

# Solución: paréntesis para que el or se resuelva primero
print((is_logged_in or is_guest) and not is_banned)  # False → ahora sí lo bloquea

print("===== PYTHON CHALLENGE =====\n")

# 1. Verificar si el nombre de usuario no está vacío y edad es mayor o igual a 18
# and: deben cumplirse las dos condiciones
name_user = "Yassir"
age = 20
print(not name_user == "" and age >= 18)  # True → tiene nombre y es mayor de edad

# 2. Verifica si la contraseña tiene al menos 8 caracteres y sin espacios
password = "python123"
print(len(password) >= 8 and " " not in password)  # True → 9 caracteres y sin espacios

# 3. Verifica si el correo no está vacío, contiene "@" y que termine en ".com"
email = "usuario@ejemplo.com"
print(not email == "" and "@" in email and email.endswith(".com"))  # True

# 4. Comprueba si username es una cadena (string), no es None y tiene más de 5 caracteres
username = "yassir123"
print(isinstance(username, str) and username is not None and len(username) > 5)  # True

# 5. Comprueba si el usuario es admin o moderador, y además (no baneado o con correo verificado)
is_admin = False
is_moderator = True
is_banned = True
is_verified = True
# Paréntesis en los dos or, para que no pase el bug del baneado
print((is_admin or is_moderator) and (not is_banned or is_verified))  # True → es moderador y verificó su correo