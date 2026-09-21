
text1= "hola"
text2= 'holas'
text3= ''' holas, mi nombre es pedro y tengo 27 años''' # triple comilla para cadenas de textos mas largas, mas flexibilidad

name= "pedro"
last_name= "perez" # para espaciado saltar antes, no aceptado

full_name= name + last_name

full_name2= name + " " + last_name # no aceptado


#string_formatting
full_name3= f'{name} {last_name}'

age= 27

message = f'{full_name3}, tienes {age}'



print(full_name3)
print(message)





# string indexes
name2= "Pato" # 0-P, 1-a, 2-t, 3-o

print(name2[0])
print(name2[1])
print(name2[2])
print(name2[3])

print(name2[-1]) # ultima letra     

# [start : stop] stop no se muestra

print(name2[2:3])
print(name2[0:2])

name3="Benjamin"

#stepover- cuantos saltos da, default 1
#[start : stop : stepover]
print(name3[::2])

print(name3[-1])
print(name3[-2])
print(name3[-3])
print(name3[-4])
print(name3[-5])
print(name3[-6])
print(name3[-7])
print(name3[-8])


print(name3[::-1])

reverse = f'{name3[7]}{name3[6]}{name3[5]}{name3[4]}{name3[3]}{name3[2]}{name3[1]}{name3[0]}'
print(reverse)

