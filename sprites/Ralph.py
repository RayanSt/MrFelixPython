import pygame


class Ralph(pygame.sprite.Sprite):
    # def __init__(self):
    #
    #     self.imagen_izquierda = pygame.image.load("../Allin/image02.png").convert_alpha()
    #     self.imagen2_izquierda = pygame.image.load("../Allin/image03.png").convert_alpha()
    #     self.imagen_derecha = pygame.image.load("../Allin/ralph02.png").convert_alpha()
    #     self.imagen2_derecha = pygame.image.load("../Allin/ralph03.png").convert_alpha()
    #     self.enojado1 = pygame.image.load("../Allin/ralph01.png").convert_alpha()
    #     self.enojado2 = pygame.image.load("../Allin/ralph04.png").convert_alpha()
    #     self.enojado3 = pygame.image.load("../Allin/ralph05.png").convert_alpha()
    #     self.enojado4 = pygame.image.load("../Allin/ralph06.png").convert_alpha()
    #     self.enojado5 = pygame.image.load("../Allin/ralph07.png").convert_alpha()
    #     self.enojado6 = pygame.image.load("../Allin/ralph08.png").convert_alpha()
    #     self.enojado7 = pygame.image.load("../Allin/ralph09.png").convert_alpha()
    #     self.enojado8 = pygame.image.load("../Allin/ralph10.png").convert_alpha()
    #     self.enojado9 = pygame.image.load("../Allin/ralph11.png").convert_alpha()
    #     self.enojado10 = pygame.image.load("../Allin/ralph12.png").convert_alpha()
    #     self.enojado11 = pygame.image.load("../Allin/ralph13.png").convert_alpha()
    #     self.imagenes_izquierda = [self.imagen_izquierda,self.imagen2_izquierda]
    #     self.imagenes_derecha = [self.imagen_derecha,self.imagen2_derecha]
    #     self.imagenes_enojo = [self.enojado1,self.enojado2,self.enojado3,self.enojado4,self.enojado5,self.enojado6,self.enojado7,
    #                             self.enojado8,self.enojado9,self.enojado10,self.enojado11]
    #     self.imagen_actual = 0
    #     self.moviendo = False
    #     self.sentido = True
    #     self.imagen = self.imagenes_izquierda[self.imagen_actual]
    #     self.rect = self.imagen.get_rect()
    #     (self.rect.top,self.rect.left) = (50,50)
    #
    # def mover(self, vx, vy):
    #     self.rect.move_ip(vx,vy)
    #
    # def update(self, superficie,vx,vy,t, sentidodere):
    #     self.sentido = sentidodere
    #     if (vx,vy) == (0,0):
    #         self.moviendo = False
    #     else:
    #         self.moviendo = True
    #     if t == 1:
    #         self.imagen_actual += 1
    #     if self.imagen_actual>(len(self.imagenes_izquierda)-1):
    #         self.imagen_actual=0
    #     #self.mover(vx, vy)
    #     if sentidodere == True:
    #         self.imagen = self.imagenes_izquierda[self.imagen_actual]
    #     if self.moviendo == False:
    #         self.imagen = self.imagenes_izquierda[0]
    #     superficie.blit(self.imagen, self.rect)

    def __init__(self):

        self.imagen_izquierda = pygame.image.load("../Allin/image02.png").convert_alpha()
        self.imagen2_izquierda = pygame.image.load("../Allin/image03.png").convert_alpha()
        self.imagen_derecha = pygame.image.load("../Allin/ralph02.png").convert_alpha()
        self.imagen2_derecha = pygame.image.load("../Allin/ralph03.png").convert_alpha()
        self.enojado1 = pygame.image.load("../Allin/ralph01.png").convert_alpha()
        self.enojado2 = pygame.image.load("../Allin/ralph04.png").convert_alpha()
        self.enojado3 = pygame.image.load("../Allin/ralph05.png").convert_alpha()
        self.enojado4 = pygame.image.load("../Allin/ralph06.png").convert_alpha()
        self.enojado5 = pygame.image.load("../Allin/ralph07.png").convert_alpha()
        self.enojado6 = pygame.image.load("../Allin/ralph08.png").convert_alpha()
        self.enojado7 = pygame.image.load("../Allin/ralph09.png").convert_alpha()
        self.enojado8 = pygame.image.load("../Allin/ralph10.png").convert_alpha()
        self.enojado9 = pygame.image.load("../Allin/ralph11.png").convert_alpha()
        self.enojado10 = pygame.image.load("../Allin/ralph12.png").convert_alpha()
        self.enojado11 = pygame.image.load("../Allin/ralph13.png").convert_alpha()
        self.imagen1 = pygame.image.load("../Allin/image02.png").convert_alpha()
        self.imagen2 = pygame.image.load("../Allin/image03.png").convert_alpha()
        self.imagenes = [self.imagen_derecha,self.imagen2_derecha]
        self.imagenesIz = [self.imagen_izquierda,self.imagen2_izquierda]
        self.imagenesEnojado = [self.enojado1,self.enojado2,self.enojado3,self.enojado4,self.enojado5,self.enojado6,self.enojado7,self.enojado8,self.enojado9,self.enojado10,self.enojado11]
        self.imagenesTemporales = []
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()
        (self.rect.top,self.rect.left) = (270,295)

    def mover(self, vx, vy):
        if ((self.rect.left,self.rect.top) < (490,270) and (self.rect.left,self.rect.top) > (70,270)):
            self.rect.move_ip(vx,vy)

    def update(self, superficie,vx,vy,t, sentido):
        if (vx, vy) == (0, 0):
            self.moviendo = False
        else:
            self.moviendo = True
        if sentido == 2:
            self.imagenesTemporales = self.imagenesEnojado
            if t % 1 == 1:
                self.imagen_actual += 1
            if self.imagen_actual > (len(self.imagenesTemporales) - 1):
                self.imagen_actual = 0
            self.imagen = self.imagenesTemporales[self.imagen_actual]
        if sentido == 0:
            self.imagenesTemporales = self.imagenes
            if t % 2 == 1:
                self.imagen_actual += 1
            if self.imagen_actual > (len(self.imagenesTemporales) - 1):
                self.imagen_actual = 0
            self.imagen = self.imagenesTemporales[self.imagen_actual]
        if sentido == 1:
            self.imagenesTemporales = self.imagenesIz
            if t % 2 == 1:
                self.imagen_actual += 1
            if self.imagen_actual > (len(self.imagenesTemporales) - 1):
                self.imagen_actual = 0
            self.imagen = self.imagenesTemporales[self.imagen_actual]

        #if self.moviendo == False:
        #    self.imagen = self.imagenesTemporales[0]
        superficie.blit(self.imagen, self.rect)
