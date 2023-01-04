import pygame
from Map import Board
from loadimage import load_image

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class Heart(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image("heart.png"), (110, 90))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.1 + 850
        self.rect.y = HEIGHT * 0.93 - 36


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 14, CELL_SIZE, all_sprites, map)
    heart = Heart(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
