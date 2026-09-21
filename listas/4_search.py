number_list=[1,2,3,4,5,2]
print(number_list)

#index retorna el index del elemento, posicion en la que se encuentra, devuelve la primera posicion que encuentra del elemento buscado
print(number_list.index(2))
print(number_list.index(3))
print(number_list.index(5))

# al preguntar por un valor con slicing el primer valor lo toma pero no considera el ultimo 0(considerado):2(no considerado)
print(number_list.index(2,0,2)) 

# in retorna true or false
print(3 in number_list)
print(10 in number_list)

# count retorna la cantidad de veces que se repite el valor consultado
print(number_list.count(2)) 



