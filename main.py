from modelo.Camion import Camion
from modelo.Carro import Carro
from modelo.Moto import Moto
import time
import random

if __name__ == '__main__':

    print('=====================================================================================')
    print('|                                                                                   |')
    print('|  ¡Bienvenido a la simulación de carreras de diferentes vehículos!    |')
    print('|    Esta simulación se desarrolla en un circuito de 5 kilómetros   |')
    print('|                                                                                   |')
    print('======================================Iniciando======================================')

    kilometrosPista = 5

    print("Competidores: ")
    carro = Carro("Ferrari", 2023, 1600, 380, 30, 1)
    moto = Moto("Honda", 2023, 1000, 366, 6, 2)
    camion = Camion("Suzuki", 2023, 9400, 350, 10, 3)

    print(carro.descripcion(), moto.descripcion(), camion.descripcion())

    competidores = [carro, moto, camion]

    puntajeCarro = 0
    puntajeMoto = 0
    puntajeCamion = 0

    tiempoInicio = time.time()

    while True:
        for competidor in competidores:

            ##Cada competidor acelerará una cantidad random de km/h
            cantidad = random.randint(10, 20)
            competidor.acelerar(cantidad)

        tiempoActual = time.time()
        distanciaCamion = (camion.getVelocidadActual() / 3600) * (tiempoActual - tiempoInicio)
        distanciaCarro = (carro.getVelocidadActual() / 3600) * (tiempoActual - tiempoInicio)
        distanciaMoto = (moto.getVelocidadActual() / 3600) * (tiempoActual - tiempoInicio)


        #print(distanciaCarro, distanciaMoto, distanciaCamion)

        ##El primer carro en cruzar la meta sera el ganador
        if distanciaCarro >= kilometrosPista:
            print('          ^^^^^ ¡El carro ha cruzado la línea de meta! ^^^^^')
            print('\n                 ==========================')
            print(f"Tiempo transcurrido: {time.time() - tiempoInicio} segundos")
            break

        if distanciaMoto >= kilometrosPista:
            print('          ^^^^^ ¡La moto ha cruzado la línea de meta! ^^^^^')
            print('\n                 ==========================')
            print(f"Tiempo transcurrido: {time.time() - tiempoInicio} segundos")
            break

        if distanciaCamion >= kilometrosPista:
            print('          ^^^^^ ¡El camion ha cruzado la línea de meta! ^^^^^')
            print('\n                 ==========================')
            print(f"Tiempo transcurrido: {time.time() - tiempoInicio} segundos")
            break

        ##Si el carro va de ultimo activa el turbo durante 5 segundos y suma 100 puntos
        if distanciaCarro <= distanciaMoto and distanciaCarro <= distanciaCamion:
            #print('          ^^^^^ ¡El carro activa el turbo! ^^^^^')
            #print('\n                 ==========================')
            carro.activarTurbo()
            cantidad = random.randint(10, 20)
            carro.acelerar(cantidad)

            puntajeCarro += 5

            tiempoActual = time.time()
            if tiempoActual - tiempoInicio <= 5:
                carro.desactivarTurbo()

        ##Si el camion va de ultimo, activa el choque para perjudicar a sus oponentes durante 10 segundos y suma 150 puntos
        elif distanciaCamion <= distanciaCarro and distanciaCamion <= distanciaMoto:
            #print('          ^^^^^ ¡El camion activa el choque! ^^^^^')
            #print('\n                 ==========================')
            camion.chocar()
            cantidad = random.randint(15, 20)
            camion.acelerar(cantidad)

            puntajeCamion += 5

            ##Si el camion los choca, el carro y la moto van a frenar una cantidad random de km/h
            cantidad = random.randint(15, 20)
            carro.frenar(cantidad)
            moto.frenar(cantidad)

            tiempoActual = time.time()
            if tiempoActual - tiempoInicio <= 5:
                camion.desactivarChoque()

        ##Si la moto va de ultima debe estabilizar su velocidad con un derrape y sumara 100 puntos
        elif distanciaMoto <= distanciaCarro and distanciaMoto <= distanciaCamion:
            #print('          ^^^^^ ¡La moto activa el derrape! ^^^^^')
            #print('\n                 ==========================')
            moto.derrapar()
            cantidad = random.randint(10, 20)
            moto.acelerar(cantidad)
            puntajeMoto += 5

            tiempoActual = time.time()
            if tiempoActual - tiempoInicio <= 5:
                moto.desactivarDerrape()

    print('\n          ^^^^^ Puntajes finales ^^^^^')
    print('\n                 ==========================')
    print(f"Carro: {puntajeCarro}\n"
          f"Moto: {puntajeMoto}\n"
          f"Camion: {puntajeCamion}")











