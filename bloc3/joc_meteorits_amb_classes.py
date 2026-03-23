# Classe meteor
import random
import pygame
import time
from pygame.locals import *

class Joc:
    def __init__(self, AMPLE, ALT, FPS, nombre_meteors):
        self.ample = AMPLE
        self.alt = ALT
        self.fps = FPS
        self.pantalla = pygame.display.set_mode((self.ample, self.alt))
        self.meteors = []
        self.numero_meteors = nombre_meteors
        self.rellotge = pygame.time.Clock()
        self.nau = Nau('assets/nave1.png',5,0,0,3, 'assets/vida.png')
        self.punts = 0
        pygame.init()

    def iniciar_joc(self):
        while True:
            self.preparar_partida()
            self.mostrar_pantalla_inici()
            self.mostrar_pantalla_joc()

    def preparar_partida(self):

        # generar els meteors
        for i in range (self.numero_meteors):
            meteor_aux = Meteor('assets/meteor.png',0,0,0)
            meteor_aux.start()
            self.meteors.append(meteor_aux)
        self.nau = Nau('assets/nave1.png',5,300,450,3, 'assets/vida.png')




    def mostrar_pantalla_inici(self):
        for event in pygame.event.get():
            # si presiona l'usuari el botó de sortir del programa acaba el joc
            if event.type == pygame.QUIT:
                pygame.quit()
        self.pantalla.fill((255,0,255))
        pygame.display.update()
        time.sleep(5)
    def mostrar_pantalla_game_over(self):
        for event in pygame.event.get():
            # si presiona l'usuari el botó de sortir del programa acaba el joc
            if event.type == pygame.QUIT:
                pygame.quit()

        img_game_over = pygame.image.load('assets/game_over.jpg')
        self.pantalla.blit(img_game_over, (0, 0))
        pygame.display.update()
        time.sleep(5)

    def mostrar_pantalla_joc(self):
        while True:
            # gestionem els events del videojoc:
            # entrada de l'usuari de teclat, ratolí, joystick:
            for event in pygame.event.get():
                # si presiona l'usuari el botó de sortir del programa acaba el joc
                if event.type == pygame.QUIT:
                    pygame.quit()
            # Ficar pantalla en negre
            self.pantalla.fill((0, 0, 0))
            # moure meteors
            self.moure_meteors()
            # moure nau
            self.moure_nau()
            # dibuixar meteors
            self.dibuixar_meteors()
            # dibuixar nau
            self.dibuixar_nau()
            # controlar col·lisions
            self.control_colisions()
            # dibuixar vides
            self.dibuixar_vides()
            # dibuixar punts
            self.dibuixar_punts()
            # actualitzar pantalla
            self.actualitzar_pantalla()

    def control_colisions(self):
        for met in (self.meteors):
            if met.rect_meteor.colliderect(self.nau.rect):
                met.start()
                self.nau.restar_vida()

    def moure_nau(self):
        # keys guarda a true les tecles que estan presionades
        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            self.nau.rect.x -= self.nau.velocitat
        if keys[K_d] or keys[K_RIGHT]:
            self.nau.rect.x += self.nau.velocitat
        if keys[K_w] or keys[K_UP]:
            self.nau.rect.y -= self.nau.velocitat
        if keys[K_s] or keys[K_DOWN]:
            self.nau.rect.y += self.nau.velocitat
        self.nau.rect
    def dibuixar_vides(self):
        # tinc 1 vida o més:
        if self.nau.vides >= 1:
            self.pantalla.blit(self.nau.img_vida, (580, 20))
        # tinc 2 vides o més:
        if self.nau.vides >= 2:
            self.pantalla.blit(self.nau.img_vida, (540, 20))
        # tinc 3 vides o més:
        if self.nau.vides >= 3:
            self.pantalla.blit(self.nau.img_vida, (500, 20))
        if self.nau.vides <= 0:
            self.mostrar_pantalla_game_over()

    def dibuixar_punts(self):
        # font de la puntuació
        font = pygame.font.SysFont(None, 32)
        img_punts = font.render(str(self.punts), True, (255, 255, 255))
        self.pantalla.blit(img_punts, (140, 30))

    def moure_meteors(self):
        for met in (self.meteors):
            met.y += met.velocitat
            met.rect_meteor = met.img_meteor.get_rect(midbottom=(met.x, met.y))

    def dibuixar_meteors(self):
        for met in (self.meteors):
            self.pantalla.blit(met.img_meteor, met.rect_meteor)
            self.punts += met.end()

    def dibuixar_nau(self):
        self.pantalla.blit(self.nau.img, self.nau.rect)
        self.nau.rect.clamp_ip(self.pantalla.get_rect())


    def actualitzar_pantalla(self):
        # Actualitzem la pantalla de joc
        pygame.display.update()
        # Comptar FPS
        self.rellotge.tick(self.fps)

class Meteor:
    # funció de creació d'un objecte meteor
    def __init__(self, imatge, velocitat, pos_x, pos_y):
        self.imatge = imatge
        self.velocitat = velocitat
        self.x = pos_x
        self.y = pos_y
        self.img_meteor = pygame.image.load(self.imatge)
        self.rect_meteor = self.img_meteor.get_rect(midbottom=(self.x, self.y))

    # Funció que col·loca el meteorit a una posició aleatòria a sobre de la pantalla
    def start(self):
        self.x = random.randint(30, 610)
        self.y = -64
        self.velocitat = random.randint(2, 10)

    # Collide
    def collide(self):
        pass

    # End
    def end(self):
        p = 0
        if self.y >= 480:
            self.start()
            p = 5 # 5 punts
        return p

class Nau:
    # funció de creació d'un objecte meteor
    def __init__(self, imatge, velocitat, pos_x, pos_y, vides, imatge_vida):
        self.imatge = imatge
        self.velocitat = velocitat
        self.x = pos_x
        self.y = pos_y
        self.img = pygame.image.load(self.imatge)
        self.rect = self.img.get_rect(midbottom=(self.x, self.y))
        self.vides = vides
        self.vides_originals = vides
        self.img_vida = pygame.image.load(imatge_vida)

    # Funció que col·loca el meteorit a una posició aleatòria a sobre de la pantalla
    def start(self):
        self.x = 300
        self.y = 460
        self.vides = self.vides_originals

    # Collide
    def moure(self):
        pass

    # End
    def restar_vida(self):
        self.vides -= 1

# Creem la nau
# Creem el joc
partida = Joc(640,480,60, 8)
partida.iniciar_joc()
