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
print()
print()


# metodos y atributos protegidos, por convencion inician con un _

class BigPerson:
    def __init__(self, name):
        self.name = name
        self._energy = 100 # atributo protegido

    #método protegido, pensado para que no sea accesible fuera de la clase
    def _waste_energy(self, energy):
        self._energy -= energy

big_person_1 = BigPerson("Benjamin")
print(big_person_1.name)
print(big_person_1._energy)
big_person_1._waste_energy(20)
print(big_person_1._energy)
print()
print()


# Métodos y atributos privados todos aquellos que inicien con __ (doble guion bajo)
# cuando se quiere ocultar valores dentro de la clase
class SmallPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = "1234" # python internamente renombra el atributo, metodo aplicando name mangling quedando _NOMBRECLASE__NOMBREATRIBUTOPRIVADO
        # SmallPerson__password
    
    def __generated_password(self):
        return f"$${self.name}%%{self.age}"

small_person_1 = SmallPerson("Benjamin",26)
print(small_person_1.name)
# print(small_person_1.__password) # error, nombre correcto seria small_person_1._SmallPerson__password
# se accede de esta manera si es muy necesario, brechas 
print(small_person_1._SmallPerson__password)
print(small_person_1._SmallPerson__generated_password())
