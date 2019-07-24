import random

import pygame


class Blocks(pygame.sprite.Sprite):

    def __init__(self):
        self.imagen1 = pygame.image.load("../Allin/Block.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/Block2.png").convert_alpha()
        self.imagen3 = pygame.image.load("../Allin/Block.png").convert_alpha()
        self.imagen4 = pygame.image.load("../Allin/Block2.png").convert_alpha()
        self.rect = self.imagen1.get_rect()
        self.rect2 = self.imagen2.get_rect()
        self.rect3 = self.imagen3.get_rect()
        self.rect4 = self.imagen4.get_rect()
        self.lista = [self.rect,self.rect2,self.rect3,self.rect4]
        (self.rect.top, self.rect.left) = (-20,-20)
        (self.rect2.top, self.rect2.left) =(-20,-20)
        (self.rect3.top, self.rect3.left) = (-20,-20)
        (self.rect4.top, self.rect4.left) = (-20,-20)


    def reagregar(self,toprandom, leftrandom):
        (self.rect.top, self.rect.left) = (toprandom, leftrandom)
        (self.rect2.top, self.rect2.left) = (toprandom + 10, leftrandom + 10)
        (self.rect3.top, self.rect3.left) = (toprandom + 20, leftrandom)
        (self.rect4.top, self.rect4.left) = (toprandom + 30, leftrandom + 20)


    def agregarotro(self):
        pass

    def mover(self):
        self.rect.move_ip(0,2)
        self.rect2.move_ip(0, 2)
        self.rect3.move_ip(0, 2)
        self.rect4.move_ip(0, 2)

    def pintar(self,superficie):
        superficie.blit(self.imagen1, self.rect)
        superficie.blit(self.imagen2, self.rect2)
        superficie.blit(self.imagen3, self.rect3)
        superficie.blit(self.imagen4, self.rect4)