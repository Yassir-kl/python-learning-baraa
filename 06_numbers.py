# Types

x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex

x = "24"
print(type(x))  # str
print(x * 3)  # 242424

# Si lo convertimos a int
x = int(x)
print(type(x))  # int
print(x * 3)  # 72

# Convertimos a int
x = 3.14
# 3 → no da 4, solo quita el decimal
print(int(x))  # 3 (no redondea)

# Convertimos a float
x = 3
print(float(x))  # 3.0

x = "3.14"
print(float(x))  # 3.14

x = 3  # real
y = 4  # imaginary
print(complex(x, y))  # (3+4j)


# Operators
print(2 + 3)  # 5
print(5 - 3)  # 2
print(4 * 2)  # 8
print(7 / 2)  # 3.5 (división normal, siempre da float)
# Siempre redondea hacia abajo
print(7 // 2)  # 3 (división entera, sin decimales)
print(7 % 2)  # 1 (lo que sobra)
print(2 ** 3)  # 8 (2x2x2)

x = 2
# x = x + 3
# print(x)  # 5
# Hace exactamente lo mismo
x += 3  
print(x)  # 5

# Lo mismo en otro operador
x -= 1
print(x)  # 4

x *= 2
# x = x * 2
print(x)  # 8


# Rounding
# Measure Distance
print(2 - 10)  # -8
# abs() quita el signo: sirve para medir distancias
print(abs(2 - 10))  # 8

# Rounding Numbers
# round() va al entero más cercano
# en este caso nos podríamos confundir por .5 pero tiene más valores 
# así que no aplicaría el caso especial ya que es .548, si fuera 36.548
# no sería 36 sino 37
price = 35.54879865
print(round(price))  # 36
# solo queremos 2 decimales
print(round(price, 2))  # 35.55
# solo queremos 1 decimal
print(round(price, 1))  # 35.5

# caso especial: con .5 exacto, round() va al par más cercano (round half to even)
# pensaríamos que iría hacia arriba, pero va al 34
# price = 34.5
# print(round(price))  # 34

# tenemos que importar math para usar floor(), ceil() y trunc()
import math
print(math.floor(price))  # 35 siempre hacia el piso (floor)
print(math.ceil(price))  # 36 siempre hacia el techo (ceil)

# corta el decimal
print(math.trunc(price))  # 35
print(math.trunc(0.8))  # 0 → no sube a 1, solo corta

# o la forma simple de deshacers de los decimales
print(int(price))  # 35

# diferencia entre floor() y trunc()
# trunc() siempre va hacia el cero, y floor() siempre va hacia abajo.
# Con positivos dan lo mismo.
print(math.trunc(-3.7))  # -3 → corta el decimal
print(math.floor(-3.7))  # -4 → baja al entero de abajo
print(math.trunc(3.7))  # 3 → corta el decimal
print(math.floor(3.7))  # 3 → baja al entero de abajo


# Random
import random
# obtendrás un número decimal aleatorio entre 0 y 1
print(random.random())

# número entero aleatorio en un rango (incluye ambos extremos)
print(random.randint(1, 6))  # como un dado: del 1 al 6


# Validation
# revisa si un float no tiene parte decimal, o sea, si en realidad es un número entero
x = 7.0
print(x.is_integer())  # True → 7.0 no tiene decimales reales

y = 7.1
print(y.is_integer())  # False → tiene .1

# isinstance(valor, tipo): True si el valor es de ese tipo
a = 70
print(isinstance(a, int))  # True

a = 70.4
print(isinstance(a, int))  # False
print(isinstance(a, float))  # True

print("===== PYTHON CHALLENGE =====\n")
# Generate a random integer between 1 and 100,
# and check if the result is an even number

number = random.randint(1, 100)
print(f"El número random que te tocó es: {number}")
print(f"¿Es par? {number % 2 == 0}")
