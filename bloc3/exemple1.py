# Crea un programa que pregunta a l'usuari:
#
#     Títol de finestra.
#     Amplada de finestra.
#     Alçada de finestra.
#     Quantitat de vermell al color de fons.
#     Quantitat de verd al color de fons.
#     Quantitat de blau al color de fons.
#     Si el programa és a pantalla sencera o en mode finestra.
#     Després el programa crea la finestra demanada per l'usuari.
import pygame

pygame.init()

titol_finestra = input("Escriu el títol de la finestra: ")
amplada_finestra = int(input("Escriu l'amplada en píxels de la finestra: "))
altura_finestra = int(input("Escriu l'alçada en píxels de la finestra: "))
vermell = int(input("Escriu la quantitat de vermell del fons de la finestra: "))
verd = int(input("Escriu la quantitat de verd del fons de la finestra: "))
blau = int(input("Escriu la quantitat de blau del fons de la finestra: "))
fullscreen = input("Vols la finestra en tamany de pantalla sencera (S/N): ")

if fullscreen == "S":
    screen = pygame.display.set_mode((amplada_finestra, altura_finestra),pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((amplada_finestra, altura_finestra))
pygame.display.set_caption(titol_finestra)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.fill((vermell, verd, blau))
        pygame.display.update()
