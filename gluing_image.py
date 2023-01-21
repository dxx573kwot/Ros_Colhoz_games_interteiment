import pygame
from loadimage import load_image


def gluing_image(images, row, col):
    im = 0
    for i in range(row):
        for j in range(col):
            screen.blit(pygame.transform.scale(load_image(images[im]), (400, 400)), (400 * j, 400 * i))
            im += 1
    pygame.image.save(screen, "Textur/exploooosion4.png")


if __name__ == "__main__":
    pygame.init()
    for i in range(12):
        print('"crab/crab-' + str(i) + '.png",', end="")
    col, row = 4, 3
    size = width, height = 400 * col, 400 * row
    screen = pygame.display.set_mode(size)
    gluing_image(
        ["crab/crab-0.png", "crab/crab-1.png", "crab/crab-2.png", "crab/crab-3.png", "crab/crab-4.png",
         "crab/crab-5.png", "crab/crab-6.png", "crab/crab-7.png", "crab/crab-8.png", "crab/crab-9.png",
         "crab/crab-10.png", "crab/crab-11.png"], row, col)
