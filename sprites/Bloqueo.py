import random

import pygame


class Bloqueo(object):
    def __init__(self):
        leftrandom = 0
        toprandom = 350
        width = 480
        hight = 20
        self.lista = pygame.Rect(leftrandom,toprandom,width,hight)


    def agregarotro(self):
        pass

    def mover(self):
        self.lista.top,self.lista.left = (350, 100)

    def pintar(self,superficie):
        pygame.draw.rect(superficie,(0,0,0),self.lista)