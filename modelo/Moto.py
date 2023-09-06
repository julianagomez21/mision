from modelo.Vehiculo import Vehiculo

class Moto(Vehiculo):

    def __init__(self, marca, modelo, cilindraje, velocidadMaxima, capacidadTanque, numeroLlantas):
        super().__init__(marca, modelo, cilindraje, velocidadMaxima, capacidadTanque)
        self.numeroLlantas = numeroLlantas
        self.derrape = False

    def derrape(func):
        def wrapper(self, cantidad):
            """
            Decorador para la función acelerar y frenar de la clase Moto, se encarga de disminuir a la mitad
            la aceleración o el frenado si el derrape está activado, ya que ambas acciones se
            vuelven menos efectivas durante el derrape
            :param cantidad: kilómetros por hora a acelerar o frenar
            :return: la función acelerar o frenar decorada con la cantidad duplicada
            """
            if self.derrape:
                cantidad *= 0.5
            return func(self, cantidad)
        return wrapper

    @derrape
    def acelerar(self, cantidad):
        super().acelerar(cantidad)

    @derrape
    def frenar(self, cantidad):
        super(Moto, self).frenar(cantidad)

    def derrapar(self):
        """
        Acción de la clase Moto para derrapar, con el objetivo de no
        perder el control en una curva, por ejemplo
        """
        self.derrape = True

    def desactivarDerrape(self):
        self.derrape = False

    def descripcion(self):
        return f"Moto: \n" \
               f"{super().descripcion()}" \
               f"Número de llantas: {self.numeroLlantas}\n"