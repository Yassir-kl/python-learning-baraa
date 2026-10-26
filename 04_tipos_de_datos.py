# Data Types
a = 10  # int
b = 3.15  # float
c = "Hello"  # str
d = 'Hi'  # str
e = "1234"  # str
f = True  # bool
g = False  # bool
h = None  # NoneType
i = ""  # str - empty
j = " "  # str - whitespace

text = "Hi"
number = 10

print(text)
print(number)

print(type(text))
print(type(number))

print(len(text))
# print(len(number))  # TypeError: int no tiene len()

print(text.upper())
# print(number.upper())  # AttributeError: int no tiene el método upper()

# te dice cuántos bits (dígitos en binario) se necesitan para representar ese número.
print(number.bit_length())  # method int
# print(text.bit_length())  # AttributeError: str no tiene bit_length()

print("===== PYTHON CHALLENGE =====\n")
age = 31
height = 1.71
name = "Yassir"
student = True
no_valor = None

print("Tu edad es:", age)
print("Su valor es:", age, "| su tipo es:", type(age)) 
      # ,"| Su longitud es:", len(age))  # TypeError, porque es int
print("Tu altura es:", height)
print("Su valor es:", height, "| su tipo es:", type(height)) 
      # ,"| Su longitud es:", len(height))  # TypeError, porque es float
print("Tu nombre es:", name)
print("Su valor es:", name, "| su tipo es:", type(name), 
      "| Su longitud es:", len(name))
print("¿Eres estudiante?", student)
print("Su valor es:", student, "| su tipo es:", type(student))
      # ,"| Su longitud es:", len(student))  # TypeError, porque es bool   
print("Algo sin valor:", no_valor)
print("Su valor es:", no_valor, "| su tipo es:", type(no_valor))
      # , "| Su longitud es:", len(no_valor))  # TypeError, porque es NoneType      