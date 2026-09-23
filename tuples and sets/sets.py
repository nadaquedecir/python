
my_set= {1,2,3,4}
# sets
# coleccion desordenada
# no tiene indeces
# no permite duplicados
# óptimo para operaciones matemáticas

print(my_set) # los imprime ordenado y sn los repetidos

# Métodos 
# Conjuntos
# .add() agrega elemento a el set
my_set.add(5)
my_set.add(3) # si existe en el set lo ignora
print(my_set)

# .remove() elimina un elemento solo si existe, error si no existe
my_set.remove(2)
print(my_set)

# .discard() igual que remove(), pero no marca error si no existe
my_set.discard(7)
print(my_set)

# .pop() elimina un elemento de manera aleatoria y lo devuelve

print(my_set.pop())
print(my_set)

# union
# set1.union(set2)
# crea un nuevo set con los elementos de ambos conjuntos
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}

union_set = set_1.union(set_2)
print(union_set)

# intersección
# set1.intersection(set2)
intersection_set = set_1.intersection(set_2)
print(intersection_set)

# difference elementos que se encuentran en un set y que no estan en otro
# set1.difference(set2)
difference = set_1.difference(set_2)
print(difference)

# symmetric difference
# elementos que se encuentran en 1 y 2 pero no en su interseccion
# set1.symmetric_difference(set2)
symmetric_difference = set_1.symmetric_difference(set_2)
print(symmetric_difference)

# issubset() evalua si un set es subconjunto de otro
# set1.issubset(set2) retorna True or False
set_sub1 = {1,2}
set_sub2 = {1,2,3,4}
print(set_sub1.issubset(set_sub2))
print(set_sub2.issubset(set_sub1))

# issuperset() evalua si un set contiene todos los elementos del otro set
# set1.issuperset(set2) retorna True or False
set_sub1 = {1,2}
set_sub2 = {1,2,3,4}
print(set_sub1.issuperset(set_sub2))
print(set_sub2.issuperset(set_sub1))