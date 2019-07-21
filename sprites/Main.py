import random
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
        self.rect.move_ip(vx,vy)

    def update(self, superficie,vx,vy,t):
        if (vx,vy) == (0,0):
            self.moviendo = False
        else:
            self.moviendo = True
        if t == 1:
            self.imagen_actual += 1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        #self.mover(vx, vy)
        self.imagen = self.imagenes[self.imagen_actual]
        if self.moviendo == False:
            self.imagen = self.imagenes[0]
        superficie.blit(self.imagen, self.rect)

class Ralph(pygame.sprite.Sprite):
    def __init__(self):

        self.imagen_izquierda = pygame.image.load("../Allin/imagen02.png").convert_alpha()
        self.imagen2_izquierda = pygame.image.load("../Allin/imagen03.png").convert_alpha()
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
        self.imagenes = [[self.imagen_izquierda,self.imagen2_izquierda],
                         [self.imagen_derecha,self.imagen2_derecha],
                         [self.enojado1,self.enojado2,self.enojado3,self.enojado4,self.enojado5,self.enojado6,self.enojado7,
                          self.enojado8,self.enojado9,self.enojado10,self.enojado11]]
        self.imagen_actual = 0
        self.moviendo = False
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()
        (self.rect.top,self.rect.left) = (560,95)

    def mover(self, vx, vy):
        self.rect.move_ip(vx,vy)

    def update(self, superficie,vx,vy,t):
        if (vx,vy) == (0,0):
            self.moviendo = False
        else:
            self.moviendo = True
        if t == 1:
            self.imagen_actual += 1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        #self.mover(vx, vy)
        self.imagen = self.imagenes[0][self.imagen_actual]
        if self.moviendo == False:
            self.imagen = self.imagenes[0][0]
        superficie.blit(self.imagen, self.rect)


class Recs(object):
    def __init__(self, numeroinicial):
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

def colisiones(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def main():
    pygame.init()
    blanco = (255, 255, 255)
    rojizo = (200, 20, 50)
    azulado = (70, 70, 190)
    negro = (0,0,0)
    pantalla = pygame.display.set_mode([480,640])
    pygame.display.set_caption("Ventana")
    explosion = pygame.mixer.Sound("../Allin/explosion.wav")
    exploto = pygame.image.load("../Allin/explosion.png")
    salir = False
    #reloj
    reloj1 = pygame.time.Clock()
    imagenfondo = pygame.image.load("../Allin/fondo.png").convert_alpha()
    pygame.mixer.music.load("../Allin/musica.mp3")

    #variable auxiliares
    (vx,vy) = (0,0)
    player = Player()
    velocidadX = 65
    velocidadY = 100
    recs1 = Recs(25)
    left_apretada, right_apretada,top_apretada, down_apretada = False,False,False,False
    colisiono = False
    t=0

    pygame.mixer.music.play(2)
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if colisiono == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left_apretada = True
                        player.mover(-velocidadX,0)
                        vx = -velocidadX
                        #vy = 0
                    if event.key == pygame.K_RIGHT:
                        right_apretada = True
                        vx = velocidadX
                        #vy = 0
                        player.mover(velocidadX,0)
                    if event.key == pygame.K_UP:
                        top_apretada = True
                        vy = -velocidadY
                        #vx = 0
                        player.mover(0,-velocidadY)
                    if event.key == pygame.K_DOWN:
                        down_apretada = True
                        vy = velocidadY
                        #vx = 0
                        player.mover(0,velocidadY)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        left_apretada = False
                        if right_apretada:
                            vx = -velocidadX
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        right_apretada = False
                        if left_apretada:
                            vx = velocidadX
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        top_apretada = False
                        if down_apretada:
                            vy = -velocidadY
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        down_apretada = False
                        if top_apretada:
                            vy = velocidadY
                        else:
                            vy = 0
        reloj1.tick(20) #20 fps
        t += 1
        if t > 1:
            t = 0
        pantalla.fill(blanco)
        pantalla.blit(imagenfondo,(0,0))
        if colisiones(player,recs1):
            colisiono = True
            player.imagen = exploto
            explosion.play()
            pygame.mixer.music.stop()
        if colisiono == False:
            recs1.mover()
            player.update(pantalla,vx,vy,t)
        recs1.pintar(pantalla)
        pygame.display.update()

        recs1.reagregar()
    pygame.quit()

if __name__ == "__main__":
    main()