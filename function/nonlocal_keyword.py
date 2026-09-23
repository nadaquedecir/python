
def outer():
    enclosing_variable = "Enclosing variable"
    
    def inner():
        nonlocal enclosing_variable
        enclosing_variable = "Enclosing Modificado" # variable local pertenece a inner() para modificar tiene que salir
    
    inner()
    print(enclosing_variable)

outer()