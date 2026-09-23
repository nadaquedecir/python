
global_variable = "Soy global"

def outer_fuction():
    enclosing_variable = "Soy enclosing"
    def inner_function():
        local_variable = "Soy local"
        
        print(local_variable)
        print(enclosing_variable)
        print(global_variable)
    inner_function()


outer_fuction()