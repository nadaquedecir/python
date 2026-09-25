
class Person:
    specie = "Humano" 
    def __init__(self, name, age):# el self es de instancia
        self.name = name 
        self.age = age 
    
    #statics methods - class methods para definir, cambiar atributos de la clase no de instancia
    @classmethod # define a class method
    def change_specie(cls, new_specie):
        cls.specie = new_specie
    
    #static method competlamente independiente, funciona por su cuenta, lo puede ocupar cualquiera tanto la clase como las instancias. se puede llamar dentro de la clase como por fuera
    @staticmethod 
    def is_old(age): # este parametro age es diferente al parametro del contructor
        return age >= 18



person_1 = Person("Benjamin", 26) # esto es una instancia
print(person_1.specie)
Person.change_specie("Humanoide") # classmethod cambia para todas las instancias
print(person_1.specie)

person_2 = Person("Pato", 26)
print(person_2.specie)
print()
#aqui usado como clase
print(Person.is_old(19))
print(Person.is_old(16))

#aqui como instancia
print(person_1.is_old(person_1.age))