import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):

        self.imagen1 = pygame.image.load("../Allin/quieto.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/arriba.png").convert_alpha()
        self.imagenes = [self.imagen1,self.imagen2]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()
        (self.rect.top,self.rect.left) = (560,95)

    def mover(self, vx, vy):
        (oldx,oldy) = (self.rect.left, self.rect.top)
        self.rect.move_ip(vx, vy)
        if ((self.rect.left, self.rect.top) > (350, 570) and (self.rect.left, self.rect.top) < (70, 270)):
            (self.rect.left, self.rect.top) = (oldx, oldy)


    def update(self, superficie,vx,vy,t):
        if (vx,vy) == (0,0):
            self.moviendo = False
        else:
            self.moviendo = True
        if t%2 == 1:
            self.imagen_actual += 1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        #self.mover(vx, vy)
        self.imagen = self.imagenes[self.imagen_actual]
        if self.moviendo == False:
            self.imagen = self.imagenes[0]
        superficie.blit(self.imagen, self.rect)