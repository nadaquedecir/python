
class Person:
    def __init__(self, name, age): # constructor, obligatorio, hace referecia a la propia clase, se puede pasar los argumentos que se quiera, obligatorio es self
        if (age > 18):
            self.name = name # -> atributos asigandos a la clase
            self.age = age # -> atributos


#object 
person_1 = Person("Benjamin", 29) # argumentos son parametros que tenemos en el constructor

print(person_1)
print(person_1.name)
print(person_1.age)

person_2 = Person("Pato", 26) # argumentos son parametros que tenemos en el constructor


class MyObject:
    # atriburtos de instacia y de clase son publicos
    specie = "Humano" # atriburtos de clase
    def __init__(self, name, age):
        self.name = name # atriburtos de instacia
        self.age = age # atriburtos de instacia
    
    #metodo publico
    def work(self):
        return f"{self.name} esta trabajando"
    
    def eats(self, food):
        if food.lower() == "porotos":
            return "Buenisima"
        else:
            return "Buena"

#atributos, caracteristicas del objeto creado

cliente_1 = MyObject("Benja", 26) # MyObject("Benja", 26) -> instancia

print(cliente_1.name)
print(cliente_1.age)
print(cliente_1.specie)
print(cliente_1.work())
print(cliente_1.eats("Porotos"))
print(cliente_1.eats("tacos"))