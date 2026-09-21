print("if conditional")
is_old = False

if is_old:
    print("puedes manejar")
else:
    print("debes ser mayor de edad")


print("\nelif")
is_old= True
is_licenced = True

if is_old:
    print("Puedes manejar")
elif is_licenced:
    print("Puedes manejar con tu licencia")
else:
    print("Debes ser mayor o tramitar tu licencia")


print("\noperadores ternarios")
is_student = False
#operadores ternarios
# True if condicion else False  ---> en python
#otros lenguajes son  ----> condicion ? True : False

get_licenced = "Licencia estudiante" if is_student else "Licencia normal"
print(get_licenced) 



print("\nThuthy vs Falsey")
#Truthy vs Falsey

# Truthy -> Verdaderos
# todo numero diferente a cero sera un valor True
print(bool(True))

print(bool(100))
print(bool(1.1))
print(bool(-1))
print(bool("Hola"))
print(bool({1,2,3}))
print(bool([1,2,3]))
print(bool((1,2,3)))
#Falsey -> Falsos
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(None))


print("\nNone")
# None
# en python no exite el null
# Null == None
# None -> vacio, ausencia

print(bool(None))

user1 = "Benjamin"
user2 = None

if user1:
    print("Este usuario esta registrado")
else:
    print("Usuario disponible")

if user2:
    print("Este usuario esta registrado")
else:
    print("Usuario disponible")