# if: ejecuta el código de adentro solo si la condición es True
score = 100
if score >= 90:   # ¿el puntaje es 90 o más? → True
    print("A")    # se ejecuta porque la condición se cumple

score = 50
if score >= 90:   # ¿el puntaje es 90 o más? → False
    print("A")    # no se ejecuta, porque la condición no se cumple
    
# else: se ejecuta cuando la condición del if es False
# else no puede ir solo: necesita un if antes
score = 50
if score >= 90:  # ¿el puntaje es 90 o más? → False
    print("A")   # no se ejecuta
else:            # como el if fue False, entra aquí
    print("F")   # se ejecuta → muestra F

score = 95
if score >= 90:  # ¿el puntaje es 90 o más? → True
    print("A")   # se ejecuta → muestra A
else:            # no entra, porque el if fue True
    print("F")   # no se ejecuta

# elif: revisa otra condición si la anterior fue False
# Orden: if → elif (uno o varios) → else (opcional)
# elif no puede ir solo: necesita un if antes
score = 95
if score >= 90:  # True → entra aquí
    print("A")  # A
elif score >= 80:  # no se revisa
    print("B")
else:
    print("F")

score = 85
if score >= 90:  # False → pasa al siguiente
    print("A")
elif score >= 80:  # True → entra aquí
    print("B")  # B
else:
    print("F")

score = 50
if score >= 90:  # False
    print("A")
elif score >= 80:  # False
    print("B")
else:  # ninguna se cumplió → entra aquí
    print("F")  # F

# Varios elif: se revisan de arriba hacia abajo hasta encontrar una True
score = 75
if score >= 90:  # False
    print("A")
elif score >= 80:  # False
    print("B")
elif score >= 70:  # True → entra aquí
    print("C")  # C
else:
    print("F")
    
# Nested if: un if dentro de otro, la segunda condición solo se revisa si la primera es True
score = 95
submitted_project = True
# submitted_project = False
if score >= 90:              # True → revisa el proyecto
    if submitted_project:    # True → A+
        print("A+")
    else:                    # 90 o más, pero sin proyecto
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


# Sin if anidado: and para A+, y un elif aparte para A
score = 100
submitted_project = True
# submitted_project = False

if score >= 90 and submitted_project:  # ≥ 90 y con proyecto → A+
    print("A+")  # True A+
elif score >= 90:                      # ≥ 90 sin proyecto → A
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    
# or en elif: con 60 o más, o con proyecto entregado → D (el proyecto te salva de la F)
# or basta un solo True para que todo dé True. Solo da False si las dos son False
score = 50
submitted_project = True
# submitted_project = False

if score >= 90 and submitted_project:  # ≥ 90 y con proyecto → A+
    print("A+")
elif score >= 90:  # ≥ 90 sin proyecto → A
    print("A")
elif score >= 80:  # ≥ 80 → B
    print("B")
elif score >= 70:  # ≥ 70 → C
    print("C")
elif score >= 60 or submitted_project:  # ≥ 60, o entregó el proyecto → D
    print("D")
else:  # menos de 60 y sin proyecto → F
    print("F")

# If independientes: cada if se revisa por separado, se pueden ejecutar varios
score = 50
submitted_project = False

# Primer if: revisa el puntaje
if score >= 90:
    print("High Score")
else:
    print("Low Score")  # se ejecuta → 50 es menor a 90

# Segundo if: revisa el proyecto (no depende del anterior)
if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")  # se ejecuta → no entregó el proyecto
    

# Se usan if independientes para revisar cada regla por separado
# y avisar de todos los errores, no solo del primero
print("===== PYTHON CHALLENGE =====\n")

# Challenge #1: validar la calidad y el formato de un correo
# email = "  "  # → El correo no puede estar vacío
# email = "ryov@gmail.com"  # → El correo debe tener . y @
# email = "ryov@@gmail.com"  # → El correo debe tener exactamente una @
# email = "ryov@gmail.io"  # → El correo debe terminar en .com, .org o .net 
# email = "ryov@gmail.com" # → El correo no puede tener más de 254 caracteres
email = ".ryov@gmail.com#"  # → El correo debe empezar y terminar con una letra o un número
# Limpiar el texto: quita los espacios de los extremos antes de validar
email = email.strip()

# 1. No debe estar vacío
if email == "":
    print("El correo no puede estar vacío")  # se ejecuta → solo tenía espacios, strip lo dejó vacío
    
# 2. El correo debe tener "." y "@"
elif not('.' in email and '@' in email):  # ¿le falta . o le falta @?
    print("El correo debe tener . y @")

# 3. Debe tener exactamente una "@"
elif email.count('@') != 1:  # ¿tiene 0 o más de una @?
    print("El correo debe tener exactamente una @")
# 4. Debe terminar en .com, .org o .net
# not: queremos el error cuando NO termina en ninguna de las tres
elif not email.endswith(('.com', '.org', '.net')):
    print("El correo debe terminar en .com, .org o .net")
# 5. No debe tener más de 254 caracteres
elif len(email) > 254:  # ¿es demasiado largo?
    print("El correo no puede tener más de 254 caracteres")
# 6. Debe empezar y terminar con una letra o un número
elif not (email[0].isalnum() and email[-1].isalnum()):  # ¿el primero o el último no es letra/número?
    print("El correo debe empezar y terminar con una letra o un número")
else:
    print("El correo es válido")

# Versión 2: if independientes + bandera (muestra TODOS los errores)
# valid empieza en True; cada regla que falla la cambia a False
email = "ryovgg@gmail.com"
valid = True

# Limpiar el texto
email = email.strip()

# 1. No debe estar vacío
if email == "":
    print("El correo no puede estar vacío")
    valid = False
# 2. Debe tener "." y "@"
if not ('.' in email and '@' in email):
    print("El correo debe tener . y @")
    valid = False
# 3. Debe tener exactamente una "@"
if email.count('@') != 1:
    print("El correo debe tener exactamente una @")
    valid = False
# 4. Debe terminar en .com, .org o .net
if not email.endswith(('.com', '.org', '.net')):
    print("El correo debe terminar en .com, .org o .net")
    valid = False
# 5. No debe tener más de 254 caracteres
if len(email) > 254:
    print("El correo no puede tener más de 254 caracteres")
    valid = False
# 6. Debe empezar y terminar con una letra o un número
if not (email[0].isalnum() and email[-1].isalnum()):
    print("El correo debe empezar y terminar con una letra o un número")
    valid = False

# Si ninguna regla cambió la bandera, el correo es válido
if valid:
    print("El correo es válido")
    
print("===== PYTHON CHALLENGE 2 =====\n")

# password = "  "  # → solo espacios: strip la deja vacía → falla 1, 2, 3 y 4
# password = "python123"  # → falta mayúscula
# password = "PYTHON123"  # → falta minúscula
# password = "123"  # → falla 2, 3 y 4 (corta, sin mayúscula ni minúscula)
# email = "usuario@ejemplo.com"  # correo del usuario (para comparar en la regla 5)
# password = "usuario@ejemplo.com"  # → falla la regla 5 (igual al correo) y la 3 (sin mayúscula)
# password = "Python 123"  # → falla la regla 6 (tiene un espacio en el medio)
# password = "Python123#"  # → no termina con letra o número
password = "Python123"  # → válida: pasa las 7 reglas
valid = True
# Limpiar el texto: quita los espacios de los extremos antes de validar
password = password.strip()

# 1. No debe estar vacía
if password == "":
    print("La contraseña no puede estar vacía")
    valid = False

# 2. Debe tener al menos 8 caracteres
if len(password) < 8:
    print("La contraseña debe tener al menos 8 caracteres") 
    valid = False
    
# 3. Debe tener al menos 1 mayúscula
if password.lower() == password:
    print("La contraseña debe tener al menos una mayúscula")
    valid = False

# 4. Debe tener al menos 1 minúscula
if password.upper() == password:
    print("La contraseña debe tener al menos una minúscula")
    valid = False
# 5. No debe ser igual al correo
if password == email:
    print("La contraseña no debe ser igual al correo")
    valid = False
# 6. No debe tener espacios
if " " in password:  # ¿hay un espacio dentro de la contraseña?
    print("La contraseña no debe tener espacios")
    valid = False

# 7. Debe empezar y terminar con una letra o un número
if not (password[0].isalnum() and password[-1].isalnum()):
    print("La contraseña debe empezar y terminar con una letra o un número")
    valid = False
if valid:
    print("La contraseña es válida")