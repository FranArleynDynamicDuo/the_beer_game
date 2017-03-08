'''
Created on Mar 7, 2017

@author: francisco
'''


class Jugador(object):
    '''
    classdocs
    '''

    def __init__(self, nombre):
        '''
        Constructor
        '''
        self.nombre = nombre

    def __str__(self, *args, **kwargs):
        return self.nombre
