
# default parameter
def hello(greet = "Hola", name = "Invitado"):
    print(f"{greet}, {name}")

greet = input("Greet: ")
name = input("Name: ")


hello()
hello(name,greet)
#keyword argument
hello(name = name, greet = greet)