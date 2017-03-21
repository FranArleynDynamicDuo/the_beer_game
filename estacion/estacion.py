'''
Created on Mar 7, 2017

@author: francisco
'''


class EstacionBase(object):
    '''
    Estacion de juego
    '''

    NOMBRE = 'Generica'
    NRO_CASILLAS = 2
    NRO_CASILLAS_ORDENES = 2
    INVENTARIO_INICIAL = 4

    def __init__(self,
                 juego,
                 jugador=None,
                 estacion_anterior=None,
                 estacion_siguiente=None):
        '''
        Constructor
        '''
        # Juego al que pertenece esta estacion
        self.juego = juego
        # Nombre de la estacion, se usa para impresion
        self.nombre = self.NOMBRE
        # Cantidad de inventario actual en la estacion para despachar
        self.inventario_actual = self.INVENTARIO_INICIAL
        # Cantidad de inventario pendiente por enviar de semanas anteriores
        self.pendiente_actual = 0
        # Historico de los inventarios de cada semana
        self.inventario_historico = []
        # Historico de los pendientes de cada semana
        self.pendiente_historico = []
        # Jugador que maneja la estacion
        self.jugador = jugador
        
        self.ultima_orden = 0
        # Casillas intermedias en la estacion entre la llegada
        # de producto y el envio
        self.casillas_intermedias = self.NRO_CASILLAS * \
            [self.INVENTARIO_INICIAL]
        # Casillas intermedias en la estacion entre la llegada
        # de la orden y que la orden sea leida
        self.casillas_ordenes = self.NRO_CASILLAS_ORDENES * \
            [self.INVENTARIO_INICIAL]
        # Estacion anterior en la cadena de produccion
        self.estacion_anterior = estacion_anterior
        # Estacion siguiente en la cadena de produccion
        self.estacion_siguiente = estacion_siguiente

    def __str__(self, *args, **kwargs):
        if not self.jugador:
            jugador = "BOT"
        else:
            jugador = str(self.jugador)
        return "Nombre: %s | Inventario Actual: %d | Pendiente Actual: %d | Produccion: %s | Ordenes: %s | Jugador: %s" % (
            self.nombre,
            self.inventario_actual,
            self.pendiente_actual,
            str(self.casillas_intermedias),
            str(self.casillas_ordenes),
            jugador)

    def avanzar_casillas(self):
        '''
        Agrega al inventario actual lo que esta en la ultima casilla intermedia y
        avanza las casillas intermedias de una estacion
        '''
        tamano = len(self.casillas_intermedias)
        ultimo = tamano - 1

        self.inventario_actual += self.casillas_intermedias[ultimo]
        self.casillas_intermedias[ultimo] = 0

        if tamano > 1:
            for i in range(ultimo):
                self.casillas_intermedias[
                    i +
                    1] += self.casillas_intermedias[i]
                self.casillas_intermedias[i] = 0

    def avanzar_ordenes(self):
        '''
        Toma la orden en la ultima posicion de las casillas de ordenes y junto
        con el pendiente actual calcula el pedido que debe satisfacerse, luego
        coloca lo que puede cumplir del pedido en la primera casilla intermedia
        de la siguiente estacion
        '''
        # Calculamos el tamano de la lista de casillas
        tamano = len(self.casillas_ordenes)
        # Calculamos el indice del ultimo elemento
        ultimo = tamano - 1
        
        self.ultima_orden = self.casillas_ordenes[ultimo]
        # Calculamos la cantidad optima de inventario a enviar
        orden_a_entregar = self.casillas_ordenes[
            ultimo] + self.pendiente_actual
        # Si no podemos despachar toda la orden, despachamos cuanto podemos y
        # el resto se le asigna al pendiente actual
        if self.inventario_actual < orden_a_entregar:
            pedido_final = self.inventario_actual
            self.inventario_actual = 0
            self.pendiente_actual = orden_a_entregar - self.inventario_actual
        # En cualquier otro caso solo restamos del inventario lo despachado
        else:
            pedido_final = orden_a_entregar
            self.inventario_actual -= pedido_final
        # Agregamos lo despachado al inicio de las casillas intermedias de la
        # siguiente estacion
        self.estacion_siguiente.casillas_intermedias[0] += pedido_final

        if tamano > 1:
            for i in range(ultimo):
                self.casillas_ordenes[
                    i +
                    1] += self.casillas_ordenes[i]
                self.casillas_ordenes[i] = 0

    def hacer_pedido(self):
        '''
        Verifica si la estacion esta siendo manejada por un jugador, si es asi
        permite al jugador colocar de cuanto desea hacer la orden, si no es asi,
        lo hara por un comportamiento predeterminado del sistema.

        Luego de esto pasa coloca la orden en la primera casilla de ordenes de la
        estacion anterior
        '''
        if self.jugador:
            self.interfaz_jugador()
            order = int(input('¿De cuanto desea hacer la orden?  '))
        else:
            order = 4
        self.estacion_anterior.casillas_ordenes[0] = order
        
    
    def interfaz_jugador(self):
        print('') 
        print('*******************************************')
        print('*        Estado actual del juego          *')
        print('*******************************************')
        print('Estacion: ' + self.nombre)
        print('Jugador: ' + self.jugador.nombre)
        print('Pendiente actual:  ' +  str(self.pendiente_actual))
        print('Inventario actual: ' +  str(self.inventario_actual))
        print('Ultima orden:  ' +  str(self.ultima_orden))
        print('') 


class Planta(EstacionBase):
    '''
    classdocs
    '''
    NOMBRE = 'Planta'
    NRO_CASILLAS_ORDENES = 1

    def __init__(self,
                 juego,
                 jugador=None,
                 estacion_siguiente=None):
        '''
        Constructor
        '''
        # Juego al que pertenece esta estacion
        self.juego = juego
        # Nombre de la estacion, se usa para impresion
        self.nombre = self.NOMBRE
        # Cantidad de inventario actual en la estacion para despachar
        self.inventario_actual = self.INVENTARIO_INICIAL
        # Cantidad de inventario pendiente por enviar de semanas anteriores
        self.pendiente_actual = 0
        # Historico de los inventarios de cada semana
        self.inventario_historico = []
        # Historico de los pendientes de cada semana
        self.pendiente_historico = []
        # Jugador que maneja la estacion
        self.jugador = jugador
        self.ultima_orden = 0
        # Casillas intermedias en la estacion entre la llegada
        # de producto y el envio
        self.casillas_intermedias = self.NRO_CASILLAS * \
            [self.INVENTARIO_INICIAL]
        # Casillas intermedias en la estacion entre la llegada
        # de la orden y que la orden sea leida
        self.casillas_ordenes = self.NRO_CASILLAS_ORDENES * \
            [self.INVENTARIO_INICIAL]
        # Estacion siguiente en la cadena de produccion
        self.estacion_siguiente = estacion_siguiente

    def hacer_pedido(self):

        if self.jugador:
            self.interfaz_jugador()
            order = int(input('¿De cuanto desea hacer la orden?  '))
        else:
            order = 4
        self.casillas_intermedias[0] += order


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
    NRO_CASILLAS_ORDENES = 0

    def __init__(self,
                 juego,
                 jugador=None,
                 estacion_anterior=None):
        '''
        Constructor
        '''
        # Juego al que pertenece esta estacion
        self.juego = juego
        # Nombre de la estacion, se usa para impresion
        self.nombre = self.NOMBRE
        # Cantidad de inventario actual en la estacion para despachar
        self.inventario_actual = self.INVENTARIO_INICIAL
        # Cantidad de inventario pendiente por enviar de semanas anteriores
        self.pendiente_actual = 0
        # Historico de los inventarios de cada semana
        self.inventario_historico = []
        # Historico de los pendientes de cada semana
        self.pendiente_historico = []
        # Jugador que maneja la estacion
        self.jugador = jugador
        self.ultima_orden = 0
        # Casillas intermedias en la estacion entre la llegada
        # de producto y el envio
        self.casillas_intermedias = self.NRO_CASILLAS * \
            [self.INVENTARIO_INICIAL]
        # Casillas intermedias en la estacion entre la llegada
        # de la orden y que la orden sea leida
        self.casillas_ordenes = self.NRO_CASILLAS_ORDENES * \
            [self.INVENTARIO_INICIAL]
        # Estacion anterior en la cadena de produccion
        self.estacion_anterior = estacion_anterior

    def avanzar_ordenes(self):
        '''
        Obtenemos una demanda e intentamos satisfacerla, sino se logra se agrega la diferencia
        a los pendientes
        '''
        if self.juego.semana_actual > self.juego.configuracion.semana_de_salto_de_demanda:
            demanda = 8
        else:
            demanda = 4
        # Guardamos la demanda en el historico
        self.juego.demandas_historico.append(demanda)
        # Calculamos la cantidad optima de inventario a enviar
        orden_a_entregar = demanda + self.pendiente_actual
        # Si no podemos despachar toda la orden, despachamos cuanto podemos y
        # el resto se le asigna al pendiente actual
        if self.inventario_actual < orden_a_entregar:
            pedido_final = self.inventario_actual
            self.inventario_actual = 0
            self.pendiente_actual = orden_a_entregar - self.inventario_actual
        # En cualquier otro caso solo restamos del inventario lo despachado
        else:
            pedido_final = orden_a_entregar
            self.inventario_actual -= pedido_final
