# Añadir una clase Pedido que tiene como atributos:
#     - lista de productos
#     - lista de cantidades
# Añade las siguiente funcionalidad:
#     - total_pedido: muestra el precio final del pedido
#     - mostrar_productos: muestra los productos del pedido

class Pedido:
    def __init__(self, listaDeProductos, listaDeCantidades):
        self.__listaDeProductos = listaDeProductos
        self.__lsitaDeCantidades = listaDeCantidades

    @property
    def listaDeProductos(self):
        return self.__listaDeProductos
    
    @listaDeProductos.setter
    def listaDeProductos(self, valor):
        self.__listaDeProductos = valor

        @property
    def listaDeCantidades(self):
        return self.__listaDeProductos
    
    @listaDeCantidades.setter
    def listaDeCantidades(self, valor):
        self.__listaDeProductos = valor

    