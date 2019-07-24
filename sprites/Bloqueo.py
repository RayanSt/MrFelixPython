import random

import pygame


class Bloqueo(object):
    def __init__(self):
        self.leftrandom = 90
        self.toprandom = 345
        self.width = 300
        self.hight = 10
        self.lista = pygame.Rect(self.leftrandom, self.toprandom, self.width, self.hight)


    def agregarotro(self):
        pass

    def regresar(self):
        self.lista = pygame.Rect(self.leftrandom, self.toprandom, self.width, self.hight)

    def mover(self):
        (self.lista.top,self.lista.left) = (-345, -190)

    def pintar(self,superficie):
        pygame.draw.rect(superficie,(0,0,0),self.lista)