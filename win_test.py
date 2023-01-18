import pygame
a = "qwertyuiopasdfghjklzxcvbnm1234567890"
b = 0
c = {

}
print(a[:-1])
SIZE = WIDTH, HEIGHT = 1250, 800
screen = pygame.display.set_mode(SIZE)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(event.key)