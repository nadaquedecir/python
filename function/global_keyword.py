
tax = 19

# solo accede al tax no lo puede modificar, para modificar se utiliza global
def change_global():
    global tax
    tax = 20
    return tax

print(change_global())
print(tax)