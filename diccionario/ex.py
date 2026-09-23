
students = {
    "Ana" : [8,7,9],
    "Luis" : [6,5,7],
    "Sofia" : [10,9,10]
}

#Agregar nuevo estudiante
#Sacar promedio de estudiante existente
#Sacar promedio de nuevo estudiante

students["Patricio"] = [7,9,7]

average_exist = students["Ana"]
print(f"El promedio del estudiante Ana es de: {sum(average_exist)/3}")


average_new = students["Patricio"]
print(f"El promedio del estudiante nuevo Patricio es de: {sum(average_new)/3}") 