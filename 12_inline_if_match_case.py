# Forma normal: if/else en varias líneas
score = 100
if score >= 90:
    print("A")
else:
    print("F")

# Inline if: lo mismo en una sola línea
# valor_si_True if condición else valor_si_False
print("A" if score >= 90 else "F")  # A

# También se puede guardar el resultado en una variable
grade = "A" if score >= 90 else "F"
print(grade)  # A

# Forma normal: if/elif/else en varias líneas
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")  # B
else:
    print("F")

# Inline if encadenado: lo mismo en una línea, poniendo otro inline if dentro del else
# Funciona, pero con 3 o más opciones es más claro el if/elif/else normal
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)  # B

# Match
# Forma con if/elif: hay que repetir country == en cada condición
country = "India"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")  # IN
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown Country")
    
# Forma con match-case: la variable se escribe una sola vez
# Regla de match: solo compara valores exactos (como ==)
# No se puede usar >, <, >=, <=, and, or ni not en los case
# Excepción: | sirve para poner varias opciones ("sábado" | "domingo")
# Para rangos o condiciones, usa if/elif
country = "USA"
match country:
    case "United States" | "USA":  # podemos verificar varios valores en un unico case
        print("US")  # US
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:  # _ es como el else: cualquier otro valor
        print("Unknown Country")