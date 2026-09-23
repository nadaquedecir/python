# iterables
# lists, tuples, sets, dictionaries
# iterador, objeto que recuerda su posición

numbers = [1,2,3,4,5,6]   # esto es un interable

for number in numbers:
    print(number)

iterator = iter(numbers)
print(iterator) # es de tipo list_iterator
# iterator es mas controlable

print(next(iterator))
print(next(iterator))
print(next(iterator))

# in dictionaries

user = {
    "name": "Benjazmin",
    "age": 26,
    "Country": "Chile",
    "can_swim": False
}
# remember dictonaries
# aqui solo trae keys
for item in user:
    print(item)
# aqui solo trae valor
for item in user.values():
    print(item)
# aqui trae todo en formato tupla
for item in user.items():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)