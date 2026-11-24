# if: ejecuta el código de adentro solo si la condición es True
score = 100
if score >= 90:   # ¿el puntaje es 90 o más? → True
    print("A")    # se ejecuta porque la condición se cumple

score = 50
if score >= 90:   # ¿el puntaje es 90 o más? → False
    print("A")    # no se ejecuta, porque la condición no se cumple
    
# else: se ejecuta cuando la condición del if es False
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