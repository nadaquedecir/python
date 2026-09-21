number_list=[1,2,3,4,5,4,5]
print(number_list)

#pop le doy el index como argumento
number_list.pop()
number_list.pop(2)
print(number_list)

# remove() como argumento se da el numero o valor que se quiera remover, si esta repetido este sacara el primero que encuentre
number_list.remove(4)
print(number_list)

# clear() elimina toda la lista
number_list.clear()
print(number_list)