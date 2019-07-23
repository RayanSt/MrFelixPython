import random
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        (self.rect.top,self.rect.left) = (560,95)

    def set_imagen(self,imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()

    def mover(self, vx, vy):
        self.rect.move_ip(vx,vy)

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)

class Recs(object):
    def __init__(self):
        self.lista = []


def main():
    pygame.init()
    blanco = (255, 255, 255)
    rojizo = (200, 20, 50)
    azulado = (70, 70, 190)
    negro = (0,0,0)
    pantalla = pygame.display.set_mode([480,640])
    pygame.display.set_caption("Ventana")
    salir = False
    #reloj
    reloj1 = pygame.time.Clock()
    quieto = pygame.image.load("quieto.png").convert_alpha()
    imagenfondo = pygame.image.load("fondo.png").convert_alpha()
    salto = pygame.image.load("arriba.png").convert_alpha()

    #variable auxiliares
    (vx,vy) = (0,0)
    player = Player(quieto)
    velocidadX = 65
    velocidadY = 100

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.set_imagen(salto)
                    player.mover(-velocidadX,0)

                if event.key == pygame.K_RIGHT:
                    player.set_imagen(salto)
                    player.mover(velocidadX,0)

                if event.key == pygame.K_UP:
                    player.mover(0,-velocidadY)
                if event.key == pygame.K_DOWN:
                    player.mover(0,velocidadY)
        reloj1.tick(15) #15 fps
        pantalla.fill(blanco)
        pantalla.blit(imagenfondo,(0,0))
        player.update(pantalla)
        player.set_imagen(quieto)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()