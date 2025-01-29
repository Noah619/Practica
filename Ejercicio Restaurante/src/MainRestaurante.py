from clases import Restaurante
from clases import Plato
from clases import Cliente
from clases import Pedido

if __name__ == "__main__":
    
    restaurante = Restaurante()

    # Crear menú
    restaurante.agregar_plato(Plato("Hamburguesa", 8.50, "Comida"))
    restaurante.agregar_plato(Plato("Refresco", 2.00, "Bebida"))
    restaurante.agregar_plato(Plato("Pizza", 12.00, "Comida"))
    
    print("¡Bienvenido al sistema del restaurante!")
    while True:
        print("\nOpciones:")
        print("1. Ver menú")
        print("2. Registrar un pedido")
        print("3. Ver pedidos")
        print("4. Cambiar estado de un pedido")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            restaurante.ver_menu()
        
        elif opcion == "2":
            cliente_nombre = input("Nombre del cliente: ")
            cliente = Cliente(cliente_nombre)
            pedido = Pedido(cliente)
            
            print("Selecciona los platos por número (escribe 'hecho' para finalizar):")
            for i, plato in enumerate(restaurante.menu):
                print(f"{i + 1}. {plato}")
            
            while True:
                seleccion = input("Número del plato: ")
                if seleccion.lower() == "hecho":
                    break
                try:
                    indice = int(seleccion) - 1
                    if 0 <= indice < len(restaurante.menu):
                        pedido.agregar_plato(restaurante.menu[indice])
                        print(f"Plato '{restaurante.menu[indice].nombre}' agregado al pedido.")
                    else:
                        print("Número inválido, intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida, intenta de nuevo.")
            
            restaurante.registrar_pedido(pedido)
            print("Pedido registrado con éxito.")
        
        elif opcion == "3":
            print("Pedidos registrados:")
            if not restaurante.pedidos:
                print("  No hay pedidos registrados.")
            for pedido in restaurante.pedidos:
                print(pedido)
        
        elif opcion == "4":
            print("Pedidos registrados:")
            for i, pedido in enumerate(restaurante.pedidos):
                print(f"{i + 1}. {pedido}")
            
            try:
                seleccion = int(input("Selecciona el número del pedido a actualizar: ")) - 1
                if 0 <= seleccion < len(restaurante.pedidos):
                    nuevo_estado = input("Nuevo estado del pedido: ")
                    restaurante.actualizar_estado_pedido(restaurante.pedidos[seleccion], nuevo_estado)
                else:
                    print("Número inválido, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")
        
        elif opcion == "5":
            print("¡Gracias por usar el sistema del restaurante!")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")
    
