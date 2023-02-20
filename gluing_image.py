import pygame
from loadimage import load_image


def gluing_image(images, row, col):
    im = 0
    for i in range(row):
        for j in range(col):
            screen.blit(pygame.transform.scale(load_image(images[im]), (400, 400)), (400 * j, 400 * i))
            im += 1
    pygame.image.save(screen, "Textur/t.png")


if __name__ == "__main__":
    pygame.init()
    for i in range(12):
        print('"crab/crab-' + str(i) + '.png",', end="")
    col, row = 5, 2
    size = width, height = 400 * col, 400 * row
    screen = pygame.display.set_mode(size)
    gluing_image(
        ["b1/p1.png", "b1/p2.png", "b1/p3.png", "b1/p4.png", "b1/p5.png", "b1/p6.png", "b1/p7.png", "b1/p8.png",
         "b1/p9.png", "b1/p10.png"], row, col)
