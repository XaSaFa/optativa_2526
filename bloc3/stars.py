import random

import pygame
from pygame.locals import *

class Star:
    def __init__(self, red, green, blue, min_speed, max_speed, min_size, max_size, AMPLE, ALT):
        max_color_r = random.randint(0, int(255 * red/100))
        max_color_g = random.randint(0, int(255 * green/100))
        max_color_b = random.randint(0, int(255 * blue/100))
        self.color = (max_color_r,max_color_g, max_color_b)
        self.size = random.randint(min_size, max_size)
        self.speed = random.randint(min_speed, max_speed)
        self.x = random.randint(0,AMPLE)
        self.y = random.randint(0, ALT) * -1


# Starfield es una clase que creará y controlará las estrellas que se ven de fondo
# en pantalla.
# Podemos elegir el número de estrellas, si se usa RGB con un multiplicador por color
# de modo que para hacer estrellas de tonos azules pasamos 0,0,100.
# velocidades mínimas y máximas y tamaños mínimos y máximos
class Starfield:

    def __init__(self, num_stars, red, green, blue, min_speed, max_speed, min_size, max_size):
        self.num_stars = num_stars
        self.color_r = red
        self.color_g = green
        self.color_b = blue
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.min_size = min_size
        self.max_size = max_size
        self.stars = []

    def start(self):
        for i in range(self.num_stars):
            s = Star(self.color_r,self.color_g,self.color_b,self.min_speed,self.max_speed,self.min_size, self.max_size,AMPLE, ALT)
            self.stars.append(s)

    def draw(self):
        for s in self.stars:
            if s.y >= 0:
                if s.size == 1:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 1, 1))
                if s.size == 2:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 2, 1))
                if s.size == 3:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 1, 2))
                if s.size == 4:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 2, 2))
                if s.size == 5:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 3, 2))
                if s.size == 6:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 2, 3))
                if s.size == 7:
                    pygame.draw.rect(pantalla, s.color, (s.x, s.y, 3, 3))
            s.y += s.speed
            if s.y >= ALT:
                s.y = random.randint(0, ALT) * -1


AMPLE = 800
ALT = 600

# iniciem pantalla
pygame.init()
pantalla = pygame.display.set_mode((AMPLE, ALT))



st = Starfield(600,0,100,0,1,10,1, 7)
st.start()

clock = pygame.time.Clock()
fps = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pantalla.fill((0, 0, 0))
    st.draw()
    pygame.display.update()
    clock.tick(fps)
