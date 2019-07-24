import random

import pygame


class Bloqueo(object):
    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2,790)
            toprandom = random.randrange(-590,-10)
            width = random.randrange(1,5)
            hight = random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,hight))

    def reagregar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 600:
                leftrandom = random.randrange(2, 790)
                toprandom = random.randrange(-590, -10)
                width = random.randrange(1, 5)
                hight = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, hight))

    def agregarotro(self):
        pass

    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,2)

    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(255,255,255),rectangulo)