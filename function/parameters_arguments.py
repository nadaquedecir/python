
#Parámetrosd-> dentro de parentensis de función 
def hello(greet, name):
    print(f"{greet}, {name}")

greet = input("Greet: ")
name = input("Name: ")

#Argumentos van dentro de cuando se llama a la función
hello(greet, name)