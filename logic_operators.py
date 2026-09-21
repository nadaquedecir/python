#logicos
#and todos los valores true para true
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false

#or al menos un valor true para true
print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false

#not -> negar
print(not True) #false
print(not False) # true


#and
print("\nand")
age = 25
is_licenced = True

if age >= 18 and is_licenced:
    print("Puedes manejar")
else:
    print("no puedes manejar")


#or
print("\n or")
is_student = False
membership= True

if is_student or membership:
    print("tienes un descuento especial")


#not
print("\n not")
is_admin = False

if not is_admin:
    print("acceso denegado")


#compracion
print("\n comparacion")

# ==
print(5 == 5) # True
print(5 == 3)# False
print("hola" == "hola") # true

# !=
print(5 != 5) # false
print(5 != 3)# true
print("hola" != "hola") #false
print("holas" != "hola") # true

#>
print(7 > 5) #true
print(5 > 9) # false

# <
print(7 < 5) # false
print(5 < 9) # true

#>=
print(7 >= 5) #true
print(5 >= 9) # false

# <=
print(7 <= 5) # false
print(5 <= 9) # true


# operadores de pertenencia
print("\n operadores de pertenencia")
# in
# not in

print(9 in range(1,10)) # true
print(11 in range(1,10))# rango de 1 a 10 partiendo desde el 0 no cuenta el 10
print(10 in range(1,10)) # false

fruit = ["Fresa", "Manzana", "Platano"]
print("Fresa" in fruit) # true
print("Mango" in fruit) # false
print("Mango" not in fruit) # true



print("\n is vs ==")

list=[]
other_list=[]

print(10 == 10.0) # true
print(1 == []) # false

print(list == other_list) # true
print(list is other_list) # false

# operator is compara en memoria



## short circuiting
print("\n short circuiting")
#or 
True or print("hola")
# evalua de izquierda a derecha
# en or solo al menos uno debe ser true
# toma el primer dato es true por lo que el resto no lo evalua
False or print("hola")

# and

False and print("hola")
True and print("hola")

#ex

name = None
#print(name.upper())
print(name and name.upper())