import pygame
from loadimage import load_image


def gluing_image(images, row, col):
    im = 0
    for i in range(row):
        for j in range(col):
            screen.blit(pygame.transform.scale(load_image(images[im]), (128, 128)), (128 * j, 128 * i))
            im += 1
    pygame.image.save(screen, "Textur/exploooosion4.png")


if __name__ == "__main__":
    pygame.init()
    col, row = 10, 5
    size = width, height = 128 * col, 128 * row
    screen = pygame.display.set_mode(size)
    gluing_image(
        ["oleg/1.png", "oleg/2.png", "oleg/3.png", "oleg/4.png", "oleg/5.png", "oleg/6.png", "oleg/7.png", "oleg/8.png",
         "oleg/9.png", "oleg/10.png", "oleg/11.png", "oleg/12.png", "oleg/13.png", "oleg/14.png", "oleg/15.png",
         "oleg/16.png", "oleg/17.png", "oleg/18.png", "oleg/19.png", "oleg/20.png", "oleg/21.png", "oleg/22.png",
         "oleg/23.png", "oleg/24.png", "oleg/25.png", "oleg/26.png", "oleg/27.png", "oleg/28.png", "oleg/29.png",
         "oleg/30.png", "oleg/31.png", "oleg/32.png", "oleg/33.png", "oleg/34.png", "oleg/35.png", "oleg/36.png",
         "oleg/37.png", "oleg/38.png", "oleg/39.png", "oleg/40.png", "oleg/41.png", "oleg/42.png", "oleg/43.png",
         "oleg/44.png", "oleg/45.png", "oleg/46.png", "oleg/47.png", "oleg/48.png", "oleg/49.png", "oleg/50.png",], row, col)
