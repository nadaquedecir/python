
# pass
# simula que algo pasa 
# pasa a la siguiente linea

for item in [1,2,3,4]:
    pass

# break 
# rompe el programa, cortando el ejecucion
print("break")
for item in [1,2,3,4]:
    if item == 4:
        break 
    print(item)

print("continue")
# continue, ignora lo que sigue
number = 0
while number < len([1,2,3,4]):
    number += 1
    continue
    print(number)