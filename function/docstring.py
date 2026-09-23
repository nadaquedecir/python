
def hello(greet = "Hola", name = "Invitado"):
    '''
    Info: Esta es una funcion para saludo personalizado.
    Devuelve un print.
    '''
    print(f"{greet}, {name}")


def multiply(a: int, b: float) -> int:
    '''
    Info: Esto multiplica dos numeros y devuelve su multiplicación
    '''
    return a*b

greet = input("Greet: ")
name = input("Name: ")


hello()
hello(name,greet)
hello(name = name, greet = greet)

number = multiply(2.0,3)
print(f"La multiplicacion es: {number}")
print(type(2))
print(type(number))