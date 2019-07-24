import random

import pygame


class Enemigos(pygame.Sprites.sprites):

    def __init__(self, numeroinicial):
        self.imagen1 = pygame.image.load("../Allin/BirdLeft.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/BirdLeft2.png").convert_alpha()
        self.imagen3 = pygame.image.load("../Allin/BirdRight.png").convert_alpha()
        self.imagen4 = pygame.image.load("../Allin/BirdRight2.png").convert_alpha()
        self.imagenes = [self.imagen1, self.imagen2]
        self.imagenesDe = [self.imagen3, self.imagen4]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()
        (self.rect.top, self.rect.left) = (560, 95)
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2,790)
            toprandom = random.randrange(-590,-10)
            width = random.randrange(15,30)
            hight = random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,hight))

    def reagregar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 600:
                leftrandom = random.randrange(2, 790)
                toprandom = random.randrange(-590, -10)
                width = random.randrange(15, 30)
                hight = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, hight))

    def agregarotro(self):
        pass

    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,2)

    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(0,0,255),rectangulo)