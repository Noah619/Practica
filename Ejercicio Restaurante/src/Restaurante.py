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



