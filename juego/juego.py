'''
Created on Mar 7, 2017

@author: francisco
'''
from estacion.estacion import Planta, Distribuidor, Mayorista, Minorista
from jugador.jugador import Jugador


class Juego(object):
    '''
    Informacion Basica del juego
    '''

    def __init__(self, planta=None, distribuidor=None,
                 mayorista=None, minorista=None, configuracion=None):
        '''
        Constructor
        '''
        self.planta = planta
        self.distribuidor = distribuidor
        self.mayorista = mayorista
        self.minorista = minorista
        self.semana_actual = 0
        self.demandas_historico = []
        self.costo = 0
        self.configuracion = configuracion

    def __str__(self, *args, **kwargs):
        return "Semana Actual: %d | Costo: %.2f | Configuracion: [%s]" % (
            self.semana_actual, self.costo, str(self.configuracion))

    def configurar(self):
        '''
        Configura los atributos generales del juego y define los jugadores
        que jugaran y con que estacion
        '''
        planta = None
        while not planta:
            jugador_comfirmacion = input(
                '¿Desea que algun jugador represente a la planta?  (S/N)')
            if jugador_comfirmacion == 'S':
                nombre = input('    Nombre del jugador: ')
                planta = Planta(juego=self,
                                jugador=Jugador(nombre=nombre))
            elif jugador_comfirmacion == 'N':
                planta = Planta(juego=self)

        distribuidor = None
        while not distribuidor:
            jugador_comfirmacion = input(
                '¿Desea que algun jugador represente al distribuidor?  (S/N)')
            if jugador_comfirmacion == 'S':
                nombre = input('    Nombre del jugador: ')
                distribuidor = Distribuidor(juego=self,
                                            jugador=Jugador(nombre=nombre))
            elif jugador_comfirmacion == 'N':
                distribuidor = Distribuidor(juego=self)

        mayorista = None
        while not mayorista:
            jugador_comfirmacion = input(
                '¿Desea que algun jugador represente al mayorista?  (S/N)')
            if jugador_comfirmacion == 'S':
                nombre = input('    Nombre del jugador: ')
                mayorista = Mayorista(juego=self,
                                      jugador=Jugador(nombre=nombre))
            elif jugador_comfirmacion == 'N':
                mayorista = Mayorista(juego=self)

        minorista = None
        while not minorista:
            jugador_comfirmacion = input(
                '¿Desea que algun jugador represente al minorista?  (S/N)')
            if jugador_comfirmacion == 'S':
                nombre = input('    Nombre del jugador: ')
                minorista = Minorista(juego=self,
                                      jugador=Jugador(nombre=nombre))
            elif jugador_comfirmacion == 'N':
                minorista = Minorista(juego=self)

        self.planta = planta
        self.distribuidor = distribuidor
        self.mayorista = mayorista
        self.minorista = minorista

        planta.estacion_siguiente = distribuidor

        distribuidor.estacion_anterior = planta
        distribuidor.estacion_siguiente = mayorista

        mayorista.estacion_anterior = distribuidor
        mayorista.estacion_siguiente = minorista

        minorista.estacion_anterior = mayorista

    def registrar_semana(self):
        '''
        Registra los costos de la semana y guarda sus historicos
        '''
        # Planta
        self.planta.inventario_historico.append(self.planta.inventario_actual)
        self.planta.pendiente_historico.append(self.planta.pendiente_actual)
        self.costo += self.planta.inventario_actual * \
            self.configuracion.precio_por_mantener
        self.costo += self.planta.pendiente_actual * \
            self.configuracion.precio_por_pendiente
        # Distribuidor
        self.distribuidor.inventario_historico.append(
            self.distribuidor.inventario_actual)
        self.distribuidor.pendiente_historico.append(
            self.distribuidor.pendiente_actual)
        self.costo += self.distribuidor.inventario_actual * \
            self.configuracion.precio_por_mantener
        self.costo += self.distribuidor.pendiente_actual * \
            self.configuracion.precio_por_pendiente
        # Mayorista
        self.mayorista.inventario_historico.append(
            self.mayorista.inventario_actual)
        self.mayorista.pendiente_historico.append(
            self.mayorista.pendiente_actual)
        self.costo += self.mayorista.inventario_actual * \
            self.configuracion.precio_por_mantener
        self.costo += self.mayorista.pendiente_actual * \
            self.configuracion.precio_por_pendiente
        # Minorista
        self.minorista.inventario_historico.append(
            self.minorista.inventario_actual)
        self.minorista.pendiente_historico.append(
            self.minorista.pendiente_actual)
        self.costo += self.minorista.inventario_actual * \
            self.configuracion.precio_por_mantener
        self.costo += self.minorista.pendiente_actual * \
            self.configuracion.precio_por_pendiente

    def ejecutar(self):
        '''
        Jugar una partida del juego de la cerveza
        '''
        while(self.semana_actual < self.configuracion.semana_maxima):
            # Avanzar Casillas
            self.planta.avanzar_casillas()
            self.distribuidor.avanzar_casillas()
            self.mayorista.avanzar_casillas()
            self.minorista.avanzar_casillas()
            # Avanzar Ordenes
            self.planta.avanzar_ordenes()
            self.distribuidor.avanzar_ordenes()
            self.mayorista.avanzar_ordenes()
            self.minorista.avanzar_ordenes()
            # Hacer pedidos
            self.planta.hacer_pedido()
            self.distribuidor.hacer_pedido()
            self.mayorista.hacer_pedido()
            self.minorista.hacer_pedido()
            # Registramos los datos de la semana
            self.registrar_semana()
            # Avanzamos el contador de semanas
            self.semana_actual += 1
