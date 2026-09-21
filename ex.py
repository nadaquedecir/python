#evaluacion de candidatos potenciales
# nombre, año experiencia, habilidades
'''
si sabe python/django, +3 años experiencia, candidato optimo
si sabe python/django, +1 años experiencia, buen candidato
si sabe python/django, posible candidato 
no sabe python, no optimo  
'''
'''
name = input("Ingrese su nombre: ")
experience_years = (input("Ingrese sus año de experiencia:"))
abilities = input("Ingrese sus habilidades tecnicas:")

candidate_abilities = abilities.split(" ")

print(candidate_abilities)

if experience_years == "":
    experience_years = None
else:
    int(experience_years)



if ("python" in candidate_abilities) and (experience_years is not None) and (experience_years >= 3):
    print(name.upper(), "\nCandidato Optimo")
elif ("django" in candidate_abilities) and (experience_years is not None) and (experience_years >= 3):
    print(name.upper(), "\nCandidato Optimo")
elif ("python" in candidate_abilities) and (experience_years is not None) and (experience_years >= 1):
    print(name.upper(), "\nBuen Candidato")
elif ("django" in candidate_abilities) and (experience_years is not None) and (experience_years >= 1):
    print(name.upper(), "\nBuen Candidato")
elif ("python" in candidate_abilities) and (experience_years == 0) or (experience_years == None):
    print(name.upper(), "\nPosible Candidato")
elif ("django" in candidate_abilities) and (experience_years == 0) or (experience_years == None):
    print(name.upper(), "\nPosible Candidato")
else:
    print(name.upper(), "\nCandidato No Optimo")
'''


name = input("Ingrese su nombre: ")
experience_years = int(input("Ingrese sus año de experiencia:"))
abilities = input("Ingrese sus habilidades tecnicas:").split(" ")

skills = "django" in abilities or "python" in abilities

result = ""
if skills:
    if experience_years >= 3:
        result = "Candidato Optimo"
    if experience_years >= 1:
        result = "Buen Candidato"
    else:
        result = "Posible Candidato"
else:
    result = "Candidato NO Optimo"
    
print(f"El candidato {name} es un {result}")