class Vehiculo:


    def __init__(self, marca, modelo, cilindraje, velocidadMaxima, capacidadTanque):
        """
        Método para la creación de un vehículo
        :param marca: la marca del vehículo en String
        :param modelo: modelo del vehículo
        :param cilindraje: cilindraje del vehículo en centímetros cúbicos
        :param velocidadMaxima: velocidad máxima del vehículo en kilómetros por hora
        :param capacidadTanque: capacidad del tanque del vehículo en galones
        """
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.velocidadMaxima = velocidadMaxima
        self.capacidadTanque = capacidadTanque
        self.velocidadActual = 0


    def acelerar(self, cantidad):
        """
            Método encargado de acelerar el vehículo
            :param cantidad: Cantidad de kilómetros por hora que se van a acelerar (km/h)
        """
        if cantidad > 0:
            self.velocidadActual += cantidad
            if self.velocidadActual > self.velocidadMaxima:
                self.velocidadActual = self.velocidadMaxima


    def frenar(self, cantidad):
        """
            Método encargado de frenar el vehículo
            :param cantidad: Cantidad de kilómetros por hora que se van a disminuir (km/h)
        """
        if cantidad > 0:
            self.velocidadActual -= cantidad
            if self.velocidadActual < 0:
                self.velocidadActual = 0

    def getVelocidadActual(self):
        return self.velocidadActual

    def descripcion(self):
        return f"Marca: {self.marca} \n" \
               f"Modelo: {self.modelo} \n" \
               f"Cilindraje: {self.cilindraje} cm^3 \n" \
               f"Velocidad máxima: {self.velocidadMaxima} km/h \n" \
               f"Capacidad del tanque: {self.capacidadTanque} galones \n"

