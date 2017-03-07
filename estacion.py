'''
Created on Mar 7, 2017

@author: francisco
'''


class EstacionBase(object):
    '''
    classdocs
    '''

    NOMBRE = 'Generica'
    NRO_CASILLAS = 2
    NRO_CASILLAS_ORDENES = 2

    def __init__(self,
                 juego,
                 nombre=NOMBRE,
                 inventario_actual,
                 jugador=None,
                 nro_casillas=NRO_CASILLAS,
                 nro_casillas_ordenes=NRO_CASILLAS_ORDENES,
                 estacion_anterior=None,
                 estacion_siguiente=None):
        '''
        Constructor
        '''
        self.juego = juego
        self.nombre = nombre
        self.inventario_actual = inventario_actual
        self.pendiente_actual = 0
        self.inventario_historico = []
        self.pendiente_historico = []
        self.jugador = jugador
        self.casillas_intermedias = nro_casillas * [0]
        self.casillas_ordenes = nro_casillas_ordenes * [0]
        self.estacion_anterior = estacion_anterior
        self.estacion_siguiente = estacion_siguiente

    def avanzar_casillas(self):
        '''
        Avanza las casillas intermedias de una estacion y agrega al inventario actual lo
        que deba agregarse
        '''
        tamano = len(self.casillas_intermedias)
        ultimo = tamano - 1

        if tamano > 1:
            for i in range(ultimo):
                self.casillas_intermedias[
                    i +
                    1] += self.casillas_intermedias[i]
                self.casillas_intermedias[i] = 0
        self.inventario_actual += self.casillas_intermedias[ultimo]
        self.casillas_intermedias[ultimo] = 0

    def avanzar_ordenes(self):
        tamano = len(self.casillas_ordenes)
        ultimo = tamano - 1

        orden_a_hacer = self.casillas_ordenes[ultimo] + self.pendiente_actual

        if self.inventario_actual < orden_a_hacer:
            self.inventario_actual = 0
            self.pendiente_actual = self.inventario_actual - orden_a_hacer
            pass
        else:
            self.inventario_actual -= orden_a_hacer

        if tamano > 1:
            for i in range(ultimo):
                self.casillas_ordenes[
                    i +
                    1] += self.casillas_ordenes[i]
                self.casillas_ordenes[i] = 0

    def hacer_pedido(self):

        if self.jugador:
            order = input('¿De cuanto desea hacer la orden?  ')
        else:
            order = 0
        self.estacion_anterior.casillas_ordenes[0] = order


class Planta(EstacionBase):
    '''
    classdocs
    '''

    NOMBRE = 'Planta'


class Distribuidor(EstacionBase):
    '''
    classdocs
    '''

    NOMBRE = 'Distribuidor'


class Mayorista(EstacionBase):
    '''
    classdocs
    '''

    NOMBRE = 'Mayorista'


class Minorista(EstacionBase):
    '''
    classdocs
    '''

    NOMBRE = 'Minorista'

    def __init__(self,
                 nombre=NOMBRE,
                 inventario_actual,
                 jugador=None,
                 nro_casillas=2):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.inventario_actual = inventario_actual
        self.jugador = jugador
        self.casillas_intermedias = nro_casillas * [0]

    def recibir_demanda(self):
        pass
