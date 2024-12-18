# Clase Plato
class Plato:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # 'Comida' o 'Bebida'

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"


# Clase Pedido
class Pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_de_platos = []
        self.estado = "Pendiente"  # Estados: Pendiente, Preparando, Entregado

    def agregar_plato(self, plato):
        # TODO: Implementar la lógica para agregar un plato al pedido
        print("agregar_plato")

    def cambiar_estado(self, nuevo_estado):
        # TODO: Implementar la lógica para cambiar el estado del pedido
        print("cambiar_estado")

    def calcular_total(self):
        # TODO: Implementar la lógica para calcular el total del pedido
        print("calcular_total")

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - Estado: {self.estado}"

# Clase Restaurante
class Restaurante:

    def __init__(self):
        self.menu = []
        self.pedidos = []

    def agregar_plato_al_menu(self, plato):
        # TODO: Implementar la lógica para agregar un plato al menú
        print("agregar_plato_al_menu")

    def registrar_pedido(self, pedido):
        # TODO: Implementar la lógica para registrar un pedido en el restaurante
        print("registrar_pedido")

    def actualizar_estado_pedido(self, cliente, nuevo_estado):
        # TODO: Implementar la lógica para actualizar el estado del pedido de un cliente
        print("actualizar_estado_pedido")

    def ver_menu(self):
        # TODO: Implementar la lógica para ver el menú del restaurante
        print("ver_menu")

