import time

import pygame
import random
from pygame.locals import *

# constants amb la mida de la finestra i FPS:
WIDTH = 640
HEIGHT = 480
FPS = 60

# definim una superficie de dibuix:
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
# vides inicials = 3
vides = 3
# punts inicials = 0
punts = 0
pygame.init()
# font de la puntuació
font = pygame.font.SysFont(None, 32)


# carregar imatge de nau:
img_nau1 = pygame.image.load('assets/nave1.png')
rect_nau1 = img_nau1.get_rect(midbottom=(300, 440))
# variables de control de la nau:
nau1_velocitat = 5
nau1_x = 300
nau1_y = 400
# carregar imatge de meteorit:
img_meteor = pygame.image.load('assets/meteor.png')
rect_meteor = img_meteor.get_rect(midbottom=(0, 0))
# carregar imatge de vida:
img_vida = pygame.image.load('assets/vida.png')
# carregar imatge game_over:
img_game_over = pygame.image.load('assets/game_over.jpg')

# funcior dibuixar vides:
def dibuixar_vides():
    # tinc 1 vida o més:
    if vides >= 1:
        pantalla.blit(img_vida, (580, 20))
    # tinc 2 vides o més:
    if vides >= 2:
        pantalla.blit(img_vida, (540, 20))
    # tinc 3 vides o més:
    if vides >= 3:
        pantalla.blit(img_vida, (500, 20))
# funció game over, mostra la pantalla de game over: 3 segons i torna al joc
def game_over():
    pantalla.blit(img_game_over,(0,0))
    pygame.display.update()
    time.sleep(3)

# funció que dibuixa els punts del jugador per pantalla
def dibuixar_punts():
    img_punts = font.render(str(punts), True, (255,255,255))
    pantalla.blit(img_punts,(140,30))

# variables de control del meteorit:
meteor_x = random.randint(30,610)
meteor_y = -64
meteor_velocitat = 4
rect_meteor.x = meteor_x
rect_meteor.y = meteor_y
# Control de FPS
rellotge = pygame.time.Clock()
# bucle de joc:
while True:
    # gestionem els events del videojoc:
    # entrada de l'usuari de teclat, ratolí, joystick:
    for event in pygame.event.get():
        # si presiona l'usuari el botó de sortir del programa acaba el joc
        if event.type == pygame.QUIT:
            pygame.quit()
    #keys guarda a true les tecles que estan presionades
    keys = pygame.key.get_pressed()
    if keys[K_a] or keys[K_LEFT]:
        rect_nau1.x -= nau1_velocitat
    if keys[K_d] or keys[K_RIGHT]:
        rect_nau1.x += nau1_velocitat
    if keys[K_l]:
        vides = 0
        punts = 0
    # Omplin la pantalla de color negre:
    pantalla.fill((0, 0, 0))
    # Dibuixem la nau per pantalla:
    pantalla.blit(img_nau1, rect_nau1)
    # Dibuixem el meteorit per pantalla:
    pantalla.blit(img_meteor, rect_meteor)
    # actualitzem posició meteorit:
    meteor_y += meteor_velocitat
    rect_meteor.y = meteor_y
    if meteor_y > HEIGHT:
        meteor_x = random.randint(30, 610)
        meteor_y = -64
        punts += 10
        rect_meteor.x = meteor_x
        rect_meteor.y = meteor_y
    # Dibuixar vides:
    dibuixar_vides()
    # Dibuixar puntuació
    dibuixar_punts()
    # controlem les vides del jugador:
    if vides <= 0:
        game_over()
        vides = 3
    #Actualitzem la pantalla de joc
    pygame.display.update()
    # Comptar FPS
    rellotge.tick(FPS)
    #controlem la col·lisió amb els meteorits
    if rect_nau1.colliderect(rect_meteor):
        vides -= 1
        meteor_x = random.randint(30, 610)
        meteor_y = -64
        rect_meteor.x = meteor_x
        rect_meteor.y = meteor_y
    #fem que la nau no surti de la pantalla:
    rect_nau1.clamp_ip(pantalla.get_rect())
    print(punts)

