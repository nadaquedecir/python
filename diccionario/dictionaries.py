
#Diccionario = Obejct(JSON)
#Estan desordenados

dictionary = {
    "key" : "value",
    "a" : 1,
    "b" : 2,
    "c" : [1,2,3,4,4],
    "verdad" : True
}

print(dictionary["key"])
print(dictionary["c"])
print(dictionary["verdad"])

user_1 = {
    "name" : "Benjamin",
    "country" : "Chile",
    "age" : 26
}

print(user_1["country"])

#key

user_2 = {
    "name" : "Benjamin",
    "country" : "Chile",
    "age" : 26,
    "email" : "rubiobenja42@gmail.com",
    (1,2,3) : "Ciudad de Mexico"  # no puede ser lista porque es mutable, pero si pouede ser tupla ya que son inmutables
}

user_2["name"] = "Patricio"

user_2["lastname"] = "Rubio"

print(user_2)

#metodos

# get()
print(user_2["name"])
print(user_2.get("name"))

# in por defecto busca el valor de llaves
print("name" in user_2)
print("Patricio" in user_2) # por defecto seria == print("Patricio" in user_2.keys())
print("Patricio" in user_2.keys())
print("Patricio" in user_2.values())

# items()

print(user_2.items())

# .copy()

user_copy = user_2.copy()

print(user_2)
print(user_copy)

#.pop()
user_copy.pop("age")
print(user_copy)

#.popitem()

user_copy.popitem()
print(user_copy)

#.update()
user_copy.update({"name" : "BENJA"})
user_copy.update({"cats" : 2}) # si no existe lo agrega

print(user_copy)

#.append()

user_copy["skills"] = user_copy.get("skills", []) # se creo otra key y se le asigno el valor de skills si es que existia la key previamente, si no se le asigna lista vacia [] o el valor que se quiera agregar
user_copy["skills"].append("Python")
user_copy["skills"].append("Django")

print(user_copy)