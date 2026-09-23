
nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")



cart = []
dictinoary = {
    "name": "Benjazmin",
    "age": 26,
    "city": "Pichidegua"
}
print()

item = input("Input: ")
for n in dictinoary.items():
    if n[0] == item: 
        cart.append(n)

print(cart)

cart2 = [("choco",10), ("mani",20), ("perfume",30)]
for item in cart2:
    print(item[1], end=" ")
    
numbers = [1,2,4,4,3,4,5,6,4,5,3,2,4]
item = int(input("number: "))
product = input("word: ")
words = [("chocolate",10), ("colacion",10), ("chocolate",10), ("galleta",10), ("galleta",10), ("chicle",10), ("chocolate",10)]
words_copy = words[:]
for number in numbers:
    print(number)
    if number == item:
        numbers.remove(item)
print(numbers)

print(words)
for word in words_copy:
    if word[0] == product:
        words.remove(word)
        print(words)
print(words)