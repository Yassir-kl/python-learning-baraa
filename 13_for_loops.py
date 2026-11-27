# Sin for: hay que repetir el print por cada ronda
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

# Con for: el bucle repite el print por nosotros
for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

# La variable después de for (item) la crea el for: puede tener cualquier nombre
# Después de in va la secuencia, que sí debe existir antes (items)
# Convención: items (plural) = toda la secuencia, item (singular) = un elemento por vuelta
items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")
    
# El for funciona igual con tupla () o con lista []
items = [1, 2, 3, 4, 5]  # lista
for item in items:
    print(f"Round: {item}")  # Round: 1 ... Round: 5
    
# El for acepta cualquier tipo de elemento, incluso mezclados (números y textos)
items = [1, 2, 3, 4, "Hi"]

for item in items:
    print(f"Round: {item}")  # Round: 1 ... Round: Hi


# El for también recorre textos: una letra por vuelta
items = " Python"
# incluso si le pones espacio, cuenta ese espacio
for item in items:
    print(f"Round: {item}")  # Round:  (espacio), Round: P, ... Round: n → 7 vueltas


# range(start, stop, step)
# range(stop): empieza en 0 y llega hasta stop - 1 (el stop no se incluye)
for item in range(5):  # stop = 5 → se detiene ANTES de llegar al 5
    print(f"Round: {item}")  # Round: 0, Round: 1, ... Round: 4

# start: opcional, por defecto 0, SÍ se incluye
# range(start, stop): empieza en start y llega hasta stop - 1
for item in range(1, 6):
    print(f"Round: {item}")  # Round: 1, Round: 2, ... Round: 5
    
# step: opcional, por defecto 1, de cuánto en cuánto salta
# Impares
for item in range(1, 10, 2):
    print(item)  # 1, 3, 5, 7, 9

# Pares
for item in range(2, 10, 2):
    print(item)  # 2, 4, 6, 8
    
# Acumulador: suma todos los valores de una lista
scores = [80, 50, 60, 75]
total = 0  # empieza en 0

for score in scores:
    total += score  # suma el puntaje de esta vuelta (total = total + score)
    print("Current Total:", total)  # adentro: se muestra en cada vuelta → 80, 130, 190, 265
print("Final Total:", total)  # afuera: se muestra una sola vez al final → 265


# Limpiar y transformar datos con un for (caso real)
# Primero limpiar (strip, lower), después transformar (replace)
# Ojo: después de lower(), el replace debe buscar ".txt" en minúscula
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')  # el orden es muy importante
    print(f"Processing {file}")  # report.csv, data.csv, final.csv
    
print("===== PYTHON CHALLENGE =====\n")

# Challenge: mostrar la tabla del 7, del 1 al 10, usando un for

# Mi ejercicio / Faltó que imprima 7 x 1 = 7 ... 7 x 10 = 70
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in numbers:
    print(f"Multiplicación: {7*number}")
    
# Ejercicio corregido
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in numbers:
    print(f"7 x {number} = {7 * number}")
    
# Ejercicio corregido hecho con range
for number in range(1, 11):  # del 1 al 10 (el 11 no se incluye)
    print(f"7 x {number} = {7 * number}")  # 7 x 1 = 7 ... 7 x 10 = 70