class Plato:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} ({self.categoria})"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []
        self.estado = "Pendiente"

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __str__(self):
        platos_str = ", ".join([plato.nombre for plato in self.platos])
        return f"Cliente: {self.cliente.nombre}, Estado: {self.estado}, Platos: [{platos_str}]"


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []

    def hacer_pedido(self, pedido):
        self.pedidos.append(pedido)

    def ver_pedidos(self):
        print(f"Pedidos de {self.nombre}:")
        if not self.pedidos:
            print("  No hay pedidos.")
        for pedido in self.pedidos:
            print(pedido)


class Restaurante:
    def __init__(self):
        self.menu = []
        self.pedidos = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def registrar_pedido(self, pedido):
        self.pedidos.append(pedido)
        pedido.cliente.hacer_pedido(pedido)

    def actualizar_estado_pedido(self, pedido, nuevo_estado):
        if pedido in self.pedidos:
            pedido.cambiar_estado(nuevo_estado)
            print(f"Estado del pedido de {pedido.cliente.nombre} actualizado a '{nuevo_estado}'.")
        else:
            print("El pedido no existe en el sistema.")

    def ver_menu(self):
        print("Menú del Restaurante:")
        if not self.menu:
            print("  El menú está vacío.")
        for plato in self.menu:
            print(plato)


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


    
