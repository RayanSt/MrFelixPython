import random
import pygame

from sprites.Blocks import Blocks
from sprites.Enemigos import Enemigos
from sprites.Item import Item
from sprites.Player import Player
from sprites.Ralph import Ralph
from sprites.Recs import Recs


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
    pygame.display.set_caption("Game")
    explosion = pygame.mixer.Sound("../Allin/explosion.wav")
    MusicItem = pygame.mixer.Sound("../Allin/item.wav")
    exploto = pygame.image.load("../Allin/explosion.png").convert_alpha()
    salir = False
    #reloj
    reloj1 = pygame.time.Clock()
    imagenfondo = pygame.image.load("../Allin/fondo.png").convert_alpha()
    pygame.mixer.music.load("../Allin/music.mp3")
    fuente = pygame.font.SysFont("Arcade Normal", 24, True, False)

    #variable auxiliares
    segundosint = 0
    segundos = ""
    (vx,vy) = (0,0)
    player = Player()
    ralph = Ralph()
    enemigos = Enemigos()
    bloques = Blocks()
    items = Item()
    velocidadX = 65
    velocidadY = 100
    recs1 = Recs(25)
    left_apretada, right_apretada,top_apretada, down_apretada = False,False,False,False
    colisiono = False
    t=0

    pygame.mixer.music.play(5)
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
                    if event.key == pygame.K_SPACE:

                        if player.rect.colliderect(ralph.rect):
                            ralph.RestarVida()

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
        reloj1.tick(20)
        segundosint = int(pygame.time.get_ticks() / 1000)
        segundos = str(segundosint)
        pantalla.fill(blanco)
        pantalla.blit(imagenfondo, (0, 0))
        if segundosint % 5 == 0:
            termino = True
            aleatorio = random.randrange(0,3)
        if segundosint % 10 == 0:
            items.RandomPosiscion()
        if segundosint % 19 == 0:
            items.rect.left = -20
            items.rect.top = -20
        if aleatorio == 2:
            ralph.mover(0,0)
            bloques.reagregar(ralph.rect.top + 80,ralph.rect.left)
        if aleatorio == 0:
            ralph.mover(2,0)
        if aleatorio == 1:
            ralph.mover(-2,0)

         #20 fps
        t += 1
        if t > 11:
            t = 0
        bloques.pintar(pantalla)
        ralph.update(pantalla, vx, vy, t,aleatorio)

        if colisiones(player,recs1) or player.rect.colliderect(enemigos.rect) or colisiones(player,bloques):
            colisiono = True
            pygame.mixer.music.stop()
            player.imagen = exploto
            explosion.play(1)
            explosion.set_volume(-80)

        if player.rect.colliderect(items.rect):
            player.TomoItem()
            items.rect.left = -20
            items.rect.top = -20
            MusicItem.play()


        if colisiono == False:
            bloques.mover()
            recs1.mover()
            enemigos.mover()
            player.update(pantalla,vx,vy,t)
            player.AumentarPuntaje()
            contador = fuente.render(segundos + "'s", 0, blanco)
            contador2 = fuente.render("score: " + str(int(player.puntaje)), 0, blanco)
            contador3 = fuente.render("vida Ralph: " + str((ralph.vida)), 0, blanco)

        pantalla.blit(contador2, (80, 10))
        pantalla.blit(contador, (350, 10))
        pantalla.blit(contador3,(170, 15))
        items.pintar(pantalla,t)
        recs1.pintar(pantalla)
        enemigos.pintar(pantalla,t)
        pygame.display.update()
      #  pantalla.blit(ralphIma,(360,95))


        recs1.reagregar()
    pygame.quit()

if __name__ == "__main__":
    main()