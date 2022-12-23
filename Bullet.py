import pygame
from Map import Board
from loadimage import load_image
import math

diretions = {
    "east": 0,
    "north-east": 45,
    "north": 90,
    "north-west": 135,
    "west": 180,
    "south-west": 225,
    "south": 270,
    "south-east": 315,
}  # Словарь. Нужен для поворота изображения.

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
bullets = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, map, x=None, y=None, diretion="east", *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(
            pygame.transform.rotate(load_image("bulet.png"), diretions[diretion] - 45),
            (CELL_SIZE, CELL_SIZE))
        self.map = map
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * CELL_SIZE, y * CELL_SIZE
        self.speed_x, self.speed_y = CELL_SIZE * round(math.cos(math.radians(diretions[diretion]))), \
                                     CELL_SIZE * round(-math.sin(math.radians(diretions[diretion])))

    def update(self, *args):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if not pygame.sprite.spritecollideany(self, self.map):
            self.kill()


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    # Тесты работоспособности пуль.
    # for i in range(16):
    #   Bullet(map, 24, i, "west", all_sprites, bullets)
    # for i in range(25):
    #   Bullet(map, i, 15, "north", all_sprites, bullets)
    # Bullet(map, 0, 0, "south-east", all_sprites, bullets)
    # for i in diretions.keys():
    #     Bullet(map, 12, 8, i, all_sprites, bullets)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(2)
