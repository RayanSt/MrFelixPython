import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.puntaje = 0
        self.vidas = 3
        self.imagen1 = pygame.image.load("../Allin/quieto.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/arriba.png").convert_alpha()
        self.imagen3 = pygame.image.load("../Allin/martillo1.png").convert_alpha()
        self.imagen4 = pygame.image.load("../Allin/martillo1.png").convert_alpha()
        self.imagen5 = pygame.image.load("../Allin/gameOver.png").convert_alpha()
        self.imagen6 = pygame.image.load("../Allin/vida.png").convert_alpha()
        self.imagen7 = pygame.image.load("../Allin/vida1.png").convert_alpha()
        self.imagen8 = pygame.image.load("../Allin/vida2.png").convert_alpha()
        self.imagenes = [self.imagen1,self.imagen2]
        self.martillado = [self.imagen3,self.imagen4]
        self.itemTomado = [self.imagen6,self.imagen7,self.imagen8]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.Martillo = self.martillado
        self.rect = self.imagen.get_rect()
        (self.rect.top,self.rect.left) = (560,95)

    def RestarVida(self):
        self.vidas -= 1

    def TomoItem(self):
        self.puntaje += 100

    def AumentarPuntaje(self):
        self.puntaje += 0.1

    def mover(self, vx, vy):
        (oldx,oldy) = (self.rect.left, self.rect.top)
        self.rect.move_ip(vx, vy)
        if ((self.rect.left) > 400 or (self.rect.left) < 70):
            self.rect.left = oldx
        if self.rect.top > 570:
            self.rect.top = oldy

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