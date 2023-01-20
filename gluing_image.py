import pygame
from loadimage import load_image


def gluing_image(images, row, col):
    im = 0
    for i in range(row):
        for j in range(col):
            screen.blit(pygame.transform.scale(load_image(images[im]), (128, 128)), (128 * j, 128 * i))
            im += 1
    pygame.image.save(screen, "Textur/exploooosion2.png")


if __name__ == "__main__":
    pygame.init()
    col, row = 2, 2
    size = width, height = 128 * col, 128 * row
    screen = pygame.display.set_mode(size)
    gluing_image(["1.png", "2.png", "3.png", "4.png", ], row, col)

