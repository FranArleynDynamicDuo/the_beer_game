'''
Created on Mar 7, 2017

@author: francisco
'''

class Settings(object):
    '''
    classdocs
    '''
    SEMANA_MAXIMA = 80
    SEMANA_DE_SALTO_DE_DEMANDA_POR_DEFECTO = 4
    PRECIO_POR_MANTENER = 0.5
    PRECIO_POR_PENDIENTE = 1

    def __init__(self, 
                 semana_maxima = SEMANA_MAXIMA,
                 semana_de_salto_de_demanda = SEMANA_DE_SALTO_DE_DEMANDA_POR_DEFECTO,
                 precio_por_mantener = PRECIO_POR_MANTENER,
                 precio_por_pendiente = PRECIO_POR_PENDIENTE):
        '''
        Constructor
        '''
        self.semana_maxima = semana_maxima
        self.semana_de_salto_de_demanda = semana_de_salto_de_demanda
        self.precio_por_mantener = precio_por_mantener
        self.precio_por_pendiente = precio_por_pendiente