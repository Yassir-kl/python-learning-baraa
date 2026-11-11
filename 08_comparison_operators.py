# comparison operators

print(10 == 10)  # True
print(10 != 10)  # False
print(7 > 3)  # True
print(7 >= 3)  # True
print(3 < 7)  # True
print(3 <= 7)  # True
print(7 <= 7)  # True → es igual, y <= incluye el igual

# Python compara letras por su código: mayúsculas valen menos que minúsculas
print("a" < "b")  # True → "a" va antes que "b" (97 < 98 → True)
print("a" == "b")  # False
print("a" == "A")  # False → distingue mayúsculas de minúsculas
print("a" < "A")  # False → "A" vale menos que "a"
print("A" < "a")  # True → "A" vale más que "a"

# comparación encadenada
# Es lo mismo que: 1 < 4 and 4 < 6 → True and True → True
# es como el operador Between
print(1 < 4 < 6)  # True

# basta con que una parte sea False para que todo sea False
print(5 < 4 < 6)  # False → 5 < 4 no se cumple

# Is age between 18 and 30?

age = 20
print(18 <= age <= 30)  # True

age = 35
print(18 <= age <= 30)  # False
