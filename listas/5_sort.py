
letters = ['d','a','f','r','t','q','b','a','i','h']
original = letters[:]
print(letters)
#sort ->metodo
letters.sort()
print(letters)

#sorted() ->>> funcion
new_letters = sorted(letters)
print(new_letters)

#para copiar se puede utilizar letters.copy() -> letter = letters[:] ocupa menos memoria

# reverse
original.reverse()
print(original)

#otrassssss
# rango(100) crea un objeto con numeros entre 0 y 199
numbers = list(range(100))
print(numbers)

sentence = ' '.join(['hola','mundo','como','estas','holas'])
print(sentence)

sum_total = sum(numbers)
max = max(numbers)
min = min(numbers)
length = len(numbers)
print(sum_total)
print(max)
print(min)
print(length)