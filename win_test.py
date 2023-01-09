import pygame
SIZE = WIDTH, HEIGHT = 1250, 800
screen = pygame.display.set_mode(SIZE)
a = 0
b = 0
c = 0
while True:
    if a >= 255:
        a = 0
        b += 1
    if b >= 255:
        b = 0
        c += 1
    if c >= 255:
        a = 0
        b = 0
        c = 0
    a += 1
    screen.fill((a, b, c))
    pygame.display.flip()