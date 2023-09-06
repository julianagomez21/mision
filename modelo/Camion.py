from modelo.Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, cilindraje, velocidadMaxima, capacidadTanque, numeroCambios):
        super().__init__(marca, modelo, cilindraje, velocidadMaxima, capacidadTanque)
        self.numeroCambios = numeroCambios
        self.choque = False

    def choque(func):
        def wrapper(self, cantidad):
            """
            Decorador para la función acelerar de la clase Camion, se encarga de aumentar
            la aceleración si el choque está activado, con el objetivo de tener la fuerza
            para derribar a los demás vehículos
            :param cantidad: kilómetros por hora a acelerar
            :return: la función acelerar decorada con la cantidad cuadruplicada
            """
            if self.choque:
                cantidad *= 3
            return func(self, cantidad)
        return wrapper

    @choque
    def acelerar(self, cantidad):
        super().acelerar(cantidad)

    def chocar(self):
        """
        Acción de la clase camión que, en cierto momento, choca a los demás vehículos
        para avanzar en la carrera
        """
        self.choque = True

    def desactivarChoque(self):
        self.choque = False

    def descripcion(self):
        return f"Camión: \n" \
               f"{super().descripcion()}" \
               f"Número de cambios: {self.numeroCambios}\n"
