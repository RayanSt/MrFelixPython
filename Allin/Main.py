import random
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):

        self.imagen1 = pygame.image.load("quieto.png").convert_alpha()
        self.imagen2 = pygame.image.load("arriba.png").convert_alpha()
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
        self.mover(vx, vy)
        self.imagen = self.imagenes[self.imagen_actual]
        if self.moviendo == False:
            self.imagen = self.imagenes[0]
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
    explosion = pygame.mixer.Sound("explosion.wav")
    exploto = pygame.image.load("explosion.png")
    salir = False
    #reloj
    reloj1 = pygame.time.Clock()
    imagen1 = pygame.image.load("quieto.png").convert_alpha()
    imagenfondo = pygame.image.load("fondo.png").convert_alpha()
    pygame.mixer.music.load("musica.mp3")

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
                        vx = -velocidadX
                    if event.key == pygame.K_RIGHT:
                        right_apretada = True
                        vx = velocidadX
                    if event.key == pygame.K_UP:
                        top_apretada = True
                        vy = -velocidadY
                    if event.key == pygame.K_DOWN:
                        down_apretada = True
                        vy = velocidadY
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