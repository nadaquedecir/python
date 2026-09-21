name= input('Escribe tu nombre: ')
email= input('Escribe tu correo electronico: ')
year_of_birth= int(input('Escribe tu año de nacimiento: '))
password= input('Escribe tu constraseña: ')
long = len(password)
age = 2050-year_of_birth



print('Nombre: ', name)
print('Email: ', email)
print('Tendras ', age, 'en el año 2050')
print('Tu contraseña es: ','*' * long)





card = f'''
    nombre: {name}
    email: {email}
    tendras {age} año en el 2050
    tu constraseña es: {'*' * long}
'''

