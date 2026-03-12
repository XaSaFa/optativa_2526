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

# Creo una variable de rellotge per controlar els FPS del joc:
clock = pygame.time.Clock()

#carregar sprite de nau (nau1.png)
nau1 = pygame.image.load('assets/nave1.png')
#carregar sprite de meteorit (meteor.png)
meteor = pygame.image.load('assets/meteor.png')
# variables de control del meteorit
meteor_y = -64
meteor_x = random.randint(30,610)
meteor_velocitat = 4
# variables de control de la nau
nau1_y = 300
nau1_x = 400
nau1_velocitat = 5
# Bucle del joc:
while True:
    # Gestionar els events del joc:
    # Entrada de teclat i de ratolí, etc...
    for event in pygame.event.get():
        # Si activem un event de sortir, acaba el joc:
        if event.type == pygame.QUIT:
            pygame.quit()

        # keys guarda quines tecles estan pulsades
        keys = pygame.key.get_pressed()
        # si hem presionat a anem a l'esquerra
        if keys[K_a]:
            nau1_x -= nau1_velocitat
        # si hem presionat d anem a la dreta
        if keys[K_d]:
            nau1_x += nau1_velocitat


    # Omplo la pantalla de color magenta:
    pantalla.fill((0,0,0))
    # Mostrem la nau a pantalla:
    pantalla.blit(nau1, (nau1_x, nau1_y))

    # Mostrem el meteorit a la pantalla:
    pantalla.blit(meteor, (meteor_x, meteor_y))
    meteor_y += meteor_velocitat

    if meteor_y > 544:
        meteor_y = -64
        meteor_x = random.randint(30,610)
    # Actualitza la pantalla:
    pygame.display.update()
    #Comptar els frames del joc i regular el temps d'execució de cada bucle
    clock.tick(FPS)
