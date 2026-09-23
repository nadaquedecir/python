# *args == arguments ocupado cuando no se sabe cuantos argumentos resivira la funcion *args -> n arguments -> retorna una tupla
# **kwargs == argumentos que vienen con nombres, es necesario asignar nombre -> n arguments con name -> retorna un diccionario

def big_funtion(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return(sum(args) + total)


print(big_funtion(1,2,3,4,5, num1=2, num2=100, num3=50))