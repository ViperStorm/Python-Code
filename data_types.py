import math

# String Data Type

# Literal  assignment
from audioop import mul
from operator import irshift, le
from turtle import right


first = "Yohan"
last = "Shyam Sundar"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Conctatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a String
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple Lines
multiline = """
Hey, how are you?                                         

I was just checking in      

                            All good?


"""
print(multiline)

# Escaping special characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                 "
multiline = "                              " + multiline
print(len(multiline))

print(len(multiline.strip()))  # Removes white space
print(len(multiline.lstrip()))  # Removes white space from left side
print(len(multiline.rstrip()))  # Removes white space from the right side

print("")

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "£1".rjust(4))
print("Muffin".ljust(16, ".") + "£2".rjust(4))
print("Cheescake".ljust(16, ".") + "£3.50".rjust(4))

print("")

# String Index Values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some Methods return Boolean Data
print(first.startswith("Y"))
print(first.endswith("f"))

# Boolean data type


myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Nummeric data Types

# Integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in funtions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
