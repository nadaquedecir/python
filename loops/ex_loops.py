
option = 0
shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]

while option != 7:
    print("Carrito de compras")
    print("Opciones:")
    print("1 - Agregar producto")
    print("2 - Eliminar producto")
    print("3 - Mostrar lista ordenada")
    print("4 - Buscar producto")
    print("5 - Contar productos del carrito")
    print("6 - Vaciar el carrito")
    print("7 - Salir")
    
    option = int(input("Ingrese su opción: "))
    
    if option == 1:
        new_product = input("Que producto desea agregar (si son varios separe con ,): ").split(",")
        if len(new_product) == 1 and new_product[0] not in shopping_cart:
            shopping_cart.append(new_product[0])
            print("Producto agregado")
        elif len(new_product) > 1 and new_product not in shopping_cart:
            shopping_cart.extend(new_product)
            print("Producto agregado")
        else:
            print("Producto ya se encuentra en el carro")   
        print(shopping_cart)
        
    elif option == 2:
        delete_product = input("Que producto desea eliminar: ")
        if delete_product in shopping_cart:
            shopping_cart.remove(delete_product)
            print("Producto eliminado")
        else:
            print("El producto no esta en el carro")
        
        print(shopping_cart)
        
    elif option == 3:
        if len(shopping_cart) > 0:    
            shopping_cart.sort()
            print("Producto ordenados")
            print(shopping_cart)
        else:
            print("Carrito vacio")
    
    elif option == 4:
        search_product = input("Que producto desea buscar: ")
        if search_product in shopping_cart:
            print("El producto esta en el carro")
        else:
            print("El prodcuto no esta en el carro")
        
        print(shopping_cart)
    
    elif option == 5:
        amount_prodcuts = len(shopping_cart)
        if amount_prodcuts >= 1:
            print(f"En el carro hay {amount_prodcuts} productos")
        else:
            print("El carro esta vacio")
        print(shopping_cart)
    
    elif option == 6:
        shopping_cart.clear()
        print("El carro se vacio")
        print(shopping_cart)
    
else:
    print("Operación terminada")