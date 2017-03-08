'''
Created on Mar 7, 2017

@author: francisco
'''
from configuracion.configuracion import Configuracion
from juego.juego import Juego


def simulacion():
    configuracion = Configuracion()
    juego = Juego(configuracion=configuracion)
    juego.configurar()
    juego.ejecutar()
    print("Costo: %0.6f" % juego.costo)
