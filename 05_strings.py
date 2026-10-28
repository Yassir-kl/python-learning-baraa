"""# Types
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
"""

# Math
"""password = "  12345678a" 
print(len(password))  # Cuenta los espacios también en el len
if len(password) < 8:
    print("Your password is too short!")
"""   
text = """
Python is easy to learn.
Python is powerful.
Many people love python
"""
# Count sirve para contar la palabra que quiero, en este caso Python
print(text.count("python"))  # Contó solo 1 ya que count distingue Mayús y Minús.
print(text.count("Python"))  # Contó solo 2 ya que count distingue Mayús y Minús.
