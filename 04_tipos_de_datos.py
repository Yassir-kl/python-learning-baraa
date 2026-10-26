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

