

#adicion  append
numbers = [1,2,3,4,5]
print(numbers)
numbers.append(100) # metodo que no retorna nada, solo para agregar
print(numbers)

#insert  insertar    [index, lo que se quiere insertar]
numbers.insert(1,200)
numbers.insert(3,300)
print(numbers)


#extension extend
numbers.extend([1,2,3,4,550])
print(numbers)
