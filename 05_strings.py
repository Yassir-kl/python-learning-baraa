# Types
name = "Yassir"
print(type(name))

age = 24
print(type(age))
print("Your age is: " + str(age))  # Solo junta str con str, por eso convierto age (int) a str
age = age + 5  # Acá si funcionará ya que los dos son int
print(age)
age = str(age)
print(type(age))
# age = age + 5  # Acá obtendré un error ya que arriba convertí en str age


# Math
password = "  12345678a" 
print(len(password))  # Cuenta los espacios también en el len
if len(password) < 8:
    print("Your password is too short!")
   
text = """
Python is easy to learn.
Python is powerful.
Many people love python
"""
# Count sirve para contar la palabra que quiero, en este caso Python
print(text.count("python"))  # Contó solo 1 ya que count distingue Mayús y Minús.
print(text.count("Python"))  # Contó solo 2 ya que count distingue Mayús y Minús.


# Transformations
price = "1234,56"
# Lo que hace este método es reemplazar, en este caso cambia la coma por el punto.
print(price.replace(",", "."))
phone = "176-1234-56"
print(phone.replace("-", "/"))  # Reemplaza por diagonal
print(phone.replace("-", ""))  # Reemplaza por nada
print(phone.replace("-", " "))  # Reemplaza por espacio
price = "$1,299.99"
# Puedo meter varios métodos, en este caso solo estoy metiendo 2
print(price.replace("$", "").replace(",", ""))

print("===== PYTHON CHALLENGE =====\n")
print("QUIERO QUITAR LOS +, ESPACIOS, PARÉNTESIS Y GUIONES\n")

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00")
      .replace(" ", "")
      .replace("(", "")
      .replace(")", "")
      .replace("-", ""))


# Transformations

first_name = "Ricardo"
last_name = "Olortegui"

# last_name = first_name + last_name
last_name = first_name + " " + last_name
print(last_name)

# Otro uso del +: armar rutas de archivos con variables
folder = "C:/Users/Ricardo/"
file = "report.csv"

# full_file_path = folder + "/" + file
full_file_path = folder + file
print(full_file_path)

# f-strings, una forma más cómoda de juntar textos

name = "Yassir"
age = 31
is_student = False

# Forma larga y común
"""print("My name is " + name 
      + ", I am " + str(age) 
      + " years old, and student status is " + str(is_student) 
      + ".")
"""
# Nueva forma y más moderna
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

print(f"2 + 3 =  {2 + 3}")

# Doble llave {{ }} para mostrar las llaves como texto en un f-string
print(f"{{This is me}}")


# Transformations
stamp = "2026-09-20 14:30"
print(stamp.split(" "))  # separa la fecha de la hora
stamp = "2026-09-20"
print(stamp.split("-"))  # separa año, mes y día por el guión

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # Separa los datos de un CSV por la coma