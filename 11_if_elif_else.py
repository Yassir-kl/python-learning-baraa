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