inventory = {
    "chocolate" : 10,
    "gomitas" : 5,
    "paleta" : 8,
    "chicle" : 2,
    "mexicano" : 8,
    "galleta" : 12
}

cart = []
option = 0
sum = 0

while option != 7:
    print("*******************************************")
    print("¡Bienvenido a la tienda de dulces!")
    print("1 - Mostrar inventario ")
    print("2 - Mostrar carrito de compra ")
    print("3 - Agregar item al carrito de compra ")
    print("4 - Eliminar item del carrito de compra ")
    print("5 - Vaciar carrito de compra ")
    print("6 - Total de compra ")
    print("7 - Salir ")
    print()
    print("*******************************************")
    print()
    option = int(input(" Ingrese la opcion: "))
    
    if option == 1:
        print("Productos")
        for key, value in inventory.items():
            print(f"{key}:{value}")
    elif option == 2:
        if len(cart) != 0:
            print("Carrito de compra")
            for item in cart:
                print(item[0])
        else:
            print(" Carrito vacio")
    elif option == 3:
        product = input("Ingrese el producto que desea agregar: ")
        for item in inventory.items():
            if item[0] == product.lower():
                cart.append(item)
                print("Producto agregado")
    elif option == 4:
        remove = input("Ingrese el producto que desea eliminar del carro: ")
        cart_copy = cart[:]
        for item in cart_copy:
            if item[0] == remove.lower():
                cart.remove(item)
                sum -= item[1]
                print("Producto eliminado")
    elif option == 5:
        if len(cart) != 0:
            cart.clear()
            sum = 0
            print("Se ha vaciado el carrito")
        else:
            print("El carrito esta vacio")
    elif option == 6:
        sum = 0
        if len(cart) != 0:
            for item in cart:
                sum += item[1]    
            print(f"El valor de su carro es de {sum} pesos")
        else:
            print("El carrito esta vacio")
else:
    print("Ha salido de la tienda")