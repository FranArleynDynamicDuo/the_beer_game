'''
Created on Mar 7, 2017

@author: francisco
'''


class Juego(object):
    '''
    classdocs
    '''

    def __init__(self, semana_actual, estaciones, jugadores, configuracion):
        '''
        Constructor
        '''
        self.estaciones = estaciones
        self.jugadores = jugadores
        self.semana_actual = semana_actual
        self.demandas = []
        self.costo = 0
        self.configuracion = configuracion
