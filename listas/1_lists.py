list_number = [1,2,3,4,5,6]
list_letters = ['a','b','c','d']
list_mix = [1,'z',5,10.5,True,[1,2,3],'g']


#list slicing 
shopping_list=['cafe','azucar','leche','te']

print(shopping_list)

#slicing
print(shopping_list[0])
print(shopping_list[3])

# inicio:fin
print(shopping_list[1:3]) # crea una nueva lista
print(shopping_list)

new_list = shopping_list[1:3]

print(new_list)

#new_shopping_list = shopping_list # aqui no se copia la lista como tal si no se copia la direccion de memoria

#para copiar una lista y poder modificar sin cambiar la original se utiliza el slicing

new_shopping_list = shopping_list[:]

new_shopping_list[0] = 'Poleras'

print(new_shopping_list)

print(shopping_list)