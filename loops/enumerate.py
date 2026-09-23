
for char in "hola":
    print(char)

# si se quiere in index se ocupa enumerate ya que "hola" solo es un string
for index, char in enumerate("Hola"):
    print(index, char)

for index, number in enumerate([1,2,3,4,5]):
    print(index, number)

for index, number in enumerate(list(range(20))):
    print(index, number)