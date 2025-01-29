from clases import Restaurante
from clases import Plato
from clases import Cliente
from clases import Pedido

# Ejemplo de uso del sistema
if __name__ == "__main__":
    restaurante = Restaurante()

    # Crear y agregar platos al menú
    restaurante.agregar_plato(Plato("Hamburguesa", 8.50, "Comida"))
    restaurante.agregar_plato(Plato("Refresco", 2.00, "Bebida"))
    restaurante.agregar_plato(Plato("Pizza", 12.00, "Comida"))

    print("Bienvenido al Restaurante")

    cliente_nombre = input("Ingrese su nombre: ")
    cliente = Cliente(cliente_nombre)

    while True:
        print("\n--- Menú ---")
        restaurante.ver_menu()

        print("\n¿Qué desea hacer?")
        print("1. Hacer un pedido")
        print("2. Ver mis pedidos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedido = Pedido(cliente)
            while True:
                plato_nombre = input("Ingresar el nombre del plato o 'fin' para terminar: ")
                if plato_nombre.lower() == "fin":
                    break

                plato_encontrado = next((plato for plato in restaurante.menu if plato.nombre.lower() == plato_nombre.lower()), None)
                if plato_encontrado:
                    pedido.agregar_plato(plato_encontrado)
                    print(f"{plato_encontrado.nombre} agregado al pedido.")
                else:
                    print("Plato no encontrado, intente de nuevo.")

            restaurante.registrar_pedido(pedido)
            print("Pedido registrado exitosamente.")

        elif opcion == "2":
            cliente.ver_pedidos()

        elif opcion == "3":
            print("Gracias por pedir. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, intentar de nuevo.")
