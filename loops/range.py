
print(range(1,10))
print(iter(range(1,10)))

for number in range(0,100,10):
    print(number)

# en este caso no se esta usando item por lo que se puede reemplazar por _ que se entiende que no se utilizara una variable
#for item in range(0,10,2):
for _ in range(0,10,2):
    print("Enviar notificación")