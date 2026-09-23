
# letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numeros = "0123456789"
# simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres = letras + numeros + simbolos
# Formula simple = (item * 7 + 3) %len(caracteres)

import string
import random


def password_generator(length):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    char = letras + numeros + simbolos
    password = ""
    for item in range(length):
        index = (item * 7 + 3)% len(char)
        password += char[index]    
    return password

def password_generator2(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    for item in range(length):
        index = random.choice(char)
        password.append(index)
    return "".join(password)


caracteres = int(input("Cantidad de caracteres para la contraseña: "))
print(password_generator2(caracteres))