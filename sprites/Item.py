import random

import pygame


class Item(pygame.sprite.Sprite):

    def __init__(self):
        self.imagen1 = pygame.image.load("../Allin/Item.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/Item2.png").convert_alpha()

        self.imagenes = [self.imagen1, self.imagen2]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()

    def RandomPosiscion(self):
        numero = random.randrange(0,2)
        if numero == 0:
            (self.rect.top, self.rect.left) = (520, 105)
        if numero == 1:
            (self.rect.top, self.rect.left) = (520, 305)


    def pintar(self,superficie,t):
        if t%2 == 1:
            self.imagen_actual += 1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        #self.mover(vx, vy)
        self.imagen = self.imagenes[self.imagen_actual]
        #if self.moviendo == False:
        #    self.imagen = self.imagenes[0]
        superficie.blit(self.imagen,self.rect)