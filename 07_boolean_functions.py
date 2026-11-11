print(True)
print(False)
print(type(True))
print(bool(123))   # True → número distinto de 0
print(bool("Hi"))  # True → texto con contenido
print(bool())  # False → sin argumento
# El 0 es un valor, pero bool() lo toma como False (cero = "nada")
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False
print(bool(" "))  # True → tiene un espacio, no está vacío

# any 

email = ""
phone = "94074-0745"
username = "yassir123"

# Permite el registro si al menos un campo está lleno
print(any([email, phone, username]))  # phone, username → True

# all

email = ""
phone = ""
username = ""

# Permite el registro solo si todos los campos están llenos
print(all([email, phone, username]))  # False → hay campos vacíos

# Ejemplo (Así llenes un campo, dará False)
email = ""
phone = ""
username = "yassir123"
print(all([email, phone, username]))  # False → porque solo un campo está lleno

# Ejemplo (Llenando los 3 campos, solo así dará True)
email = "ryov.kernel@gmail.com"
phone = "940749-744"
username = "yassir123"
print(all([email, phone, username]))  # True

# isinstance
# True si el valor es de ese tipo
print(isinstance(123, int))  # True
print(isinstance(True, str))  # False

# Métodos que devuelven True o False
print("Hello".endswith("o"))  # True → termina en "o"
print("Hello".startswith("o"))  # False → empieza con "H"
