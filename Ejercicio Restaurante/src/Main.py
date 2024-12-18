if __name__ == '__main__':
    
        while True:
        print("================================================================")
        print("\n")
        print("1. Menu")
        print("2. Buscar una ubicación")
        print("3. Buscar ubicaciones por provincia")
        print("4. Mostrar provincias y CP almacenados")
        print("Escribe 'exit' para salir.")
        
        opcion = input("Selecciona una opción: ").strip().lower()

        if opcion == '1':
            insertar_ubicacion(gestor)
        elif opcion == '2':
            buscar_ubicacion(gestor)
        elif opcion == '3':
            buscar_ubicaciones_por_provincia(gestor)
        elif opcion == '4':
            mostrar_codigos_postales_y_provincias_almacenadas(gestor)
        elif opcion == 'exit':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
    # Ejemplo de uso del sistema
    # Crear el restaurante
    restaurante = Restaurante()
    
    # Crear platos
    plato1 = Plato("Hamburguesa", 8.50, "Comida")
    plato2 = Plato("Refresco", 2.00, "Bebida")
    plato3 = Plato("Pizza", 12.00, "Comida")
    
    # Agregar platos al menú
    restaurante.agregar_plato_al_menu(plato1)
    restaurante.agregar_plato_al_menu(plato2)
    restaurante.agregar_plato_al_menu(plato3)
    
    # Crear clientes
    cliente1 = Cliente("Carlos")
    cliente2 = Cliente("Lucía")
    
    # Crear pedidos
    pedido1 = Pedido(cliente1)
    pedido1.agregar_plato(plato1)
    pedido1.agregar_plato(plato2)
    
    pedido2 = Pedido(cliente2)
    pedido2.agregar_plato(plato3)
    
    # Registrar pedidos en el restaurante
    restaurante.registrar_pedido(pedido1)
    restaurante.registrar_pedido(pedido2)
    
    # Cambiar el estado del pedido de un cliente
    restaurante.actualizar_estado_pedido(cliente1, "Preparando")
    
    # Ver menú
    restaurante.ver_menu()
    
    # Cliente ve sus pedidos
    cliente1.ver_pedidos()
    cliente2.ver_pedidos()
