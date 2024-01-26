class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor      

    def calcular_total(self, cantidad):
        """Funcion que introduciendo un número positivo nos devuelve ese número multiplicado por el precio que tiene.
        Parámetro: cantidad = número positivo.
        Salida: cantidad multiplicado por el precio."""
        return self.__precio * cantidad


    def __str__(self):
        return ('Codigo: ' + str(self.__codigo) + 'nombre: ' 
        + str(self.__nombre) + 'precio: ' + str(self.__precio)  )



class Pedido:
    def __init__(self, Productos, Cantidades):
        self.__Productos = Productos
        self.__Cantidades = Cantidades

    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__Productos, self.__Cantidades):
            total = total - p.calcular_total(c)

            return total

    def mostrar_pedido(self):
        for (p,c) in zip(self.__Productos, self.__Cantidades):
            print('Producto: ', p.nombre, 'Cantidad: ' + str(c))
    
p1 = Producto(1, 'Producto 1 ' , 5)
p2 = Producto(2, 'Producto 2 ' , 10)
p3 = Producto(3, 'Producto 3 ' , 20)

print(p1.calcular_total(2))
print(p2.calcular_total(2))
print(p3.calcular_total(2))

productos = [p1, p1, p3]
cantidades = [6, 3, 9]

pedido = Pedido(productos, cantidades)

print('Total pedido: ' + str(pedido.total_pedido()))

pedido.mostrar_pedido()