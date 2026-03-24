import time

import pygame
import random
from pygame.locals import *

# Mides de la finestra:
WIDTH = 640
HIGH = 480
# Frames per segon del joc:
FPS = 60
# Fem una superfície del tamany especificat abans:
pantalla = pygame.display.set_mode((WIDTH, HIGH))

# A partir d'aquí ja podem utilitzar funcions de pygame
pygame.init()
# Carregar font per als punts
font = pygame.font.SysFont(None,40)
# Creo una variable de rellotge per controlar els FPS del joc:
clock = pygame.time.Clock()
# carregar imatge de Game Over:
img_game_over = pygame.image.load('assets/game_over.jpg')
#carregar sprite de vida
img_vida = pygame.image.load('assets/cor.png')
#carregar sprite de nau (nau1.png)
img_nau1 = pygame.image.load('assets/nave1.png')
rect_nau1 = img_nau1.get_rect(midbottom=(300, 440))
#carregar sprite de meteorit (meteor.png)
img_meteor = pygame.image.load('assets/meteor.png')
rect_meteor = img_meteor.get_rect(midbottom=(0, 0))
# variables de control del meteorit
rect_meteor.y = -64
rect_meteor.x = random.randint(30,610)
meteor_velocitat = 6
# variables de control de la nau
nau1_velocitat = 5
vides = 3
punts = 0
# Bucle del joc:
while True:
    # Gestionar els events del joc:
    # Entrada de teclat i de ratolí, etc...
    for event in pygame.event.get():
        # Si activem un event de sortir, acaba el joc:
        if event.type == pygame.QUIT:
            pygame.quit()
    # comprovem si tenim 0 vides:
    if vides <= 0:
        # Mostrar Game Over
        pantalla.blit(img_game_over, (0, 0))
        # keys guarda quines tecles estan pulsades
        keys = pygame.key.get_pressed()
        # si hem presionat a anem a l'esquerra
        if keys[K_SPACE]:
            vides = 3
            punts = 0
    else:
        # keys guarda quines tecles estan pulsades
        keys = pygame.key.get_pressed()
        # si hem presionat a anem a l'esquerra
        if keys[K_a] or keys[K_LEFT]:
            rect_nau1.x -= nau1_velocitat
        # si hem presionat d anem a la dreta
        if keys[K_d] or keys[K_RIGHT]:
            rect_nau1.x += nau1_velocitat
        # Omplo la pantalla de color negre:
        pantalla.fill((0,0,0))
        # Mostrem la nau a pantalla:
        pantalla.blit(img_nau1, rect_nau1)

        # comprovem col·lisions:
        if rect_nau1.colliderect(rect_meteor):
            # perdre una vida
            vides -= 1
            # pujo el meteorit
            rect_meteor.y = -64
            rect_meteor.x = random.randint(30, 610)


        # Mostrem el meteorit a la pantalla:
        pantalla.blit(img_meteor, (rect_meteor.x, rect_meteor.y))
        rect_meteor.y += meteor_velocitat
        # Si el meteor baixa a fora de la pantalla el recol·loquem a dalt
        if rect_meteor.y > 544:
            rect_meteor.y = -64
            rect_meteor.x = random.randint(30,610)
            punts += 10
        # dibuixar vides:
        if vides >= 1:
            pantalla.blit(img_vida, (30, 30))
        if vides >= 2:
            pantalla.blit(img_vida, (70, 30))
        if vides >= 3:
            pantalla.blit(img_vida, (110, 30))
        # dibuixar punts:
        img_punts = font.render(str(punts), True, (255, 255, 255))
        pantalla.blit(img_punts, (500, 30))


    # Actualitzar la pantalla:
    pygame.display.update()
    # fem que la nau no surti de la pantalla:
    rect_nau1.clamp_ip(pantalla.get_rect())
    #Comptar els frames del joc i regular el temps d'execució de cada bucle
    clock.tick(FPS)
