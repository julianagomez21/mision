from modelo.Vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, marca, modelo, cilindraje, velocidadMaxima, capacidadTanque, numeroPuertas):
        super().__init__(marca, modelo, cilindraje, velocidadMaxima, capacidadTanque)
        self.numeroPuertas = numeroPuertas
        self.turboActivado = False

    def turbo(func):
        def wrapper(self, cantidad):
            """
            Decorador para la función acelerar de la clase Carro, se encarga de aumentar
            la aceleración si el turbo está activado
            :param cantidad: kilómetros por hora a acelerar
            :return: la función acelerar decorada con la cantidad duplicada
            """
            if self.turboActivado:
                cantidad *= 2
            return func(self, cantidad)
        return wrapper


    @turbo
    def acelerar(self, cantidad):
        super().acelerar(cantidad)

    def activarTurbo(self):
        """
        Acción de la clase Carro para aumentar la velocidad en
        un momento determinado
        """
        self.turboActivado = True

    def desactivarTurbo(self):
        self.turboActivado = False

    def descripcion(self):
        return f"Carro: \n" \
               f"{super().descripcion()}" \
               f"Número de puertas: {self.numeroPuertas}\n"
