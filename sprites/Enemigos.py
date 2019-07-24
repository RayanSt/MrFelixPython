import random

import pygame


class Enemigos(pygame.sprite.Sprite):

    def __init__(self):
        self.imagen1 = pygame.image.load("../Allin/BirdLeft.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/BirdLeft2.png").convert_alpha()
        self.imagen3 = pygame.image.load("../Allin/BirdRight.png").convert_alpha()
        self.imagen4 = pygame.image.load("../Allin/BirdRight2.png").convert_alpha()
        self.imagen5 = pygame.image.load("../Allin/Block.png").convert_alpha()
        self.imagen6 = pygame.image.load("../Allin/Block2.png").convert_alpha()
        self.imagenes = [self.imagen1, self.imagen2]
        self.imagenesDe = [self.imagen3, self.imagen4]
        self.imagenesBlo = [self.imagen5, self.imagen6]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()

        leftrandom = random.randrange(480, 550)
        toprandom = random.randrange(10,590)
        (self.rect.top, self.rect.left) = (toprandom,leftrandom)


    def reagregar(self):
                leftrandom = random.randrange(480, 550)
                toprandom = random.randrange(590, 10)
                (self.rect.top, self.rect.left) = (toprandom, leftrandom)

    def agregarotro(self):
        pass

    def mover(self):
        self.rect.move_ip(-2,0)

    def pintar(self,superficie,t):
        if t%2 == 1:
            self.imagen_actual += 1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        #self.mover(vx, vy)
        self.imagen = self.imagenes[self.imagen_actual]
        #if self.moviendo == False:
            #self.imagen = self.imagenes[0]
        superficie.blit(self.imagen, self.rect)