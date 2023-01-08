import pygame
from Map import Board
from loadimage import load_image
import math

directions = {
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
    def __init__(self, map: pygame.sprite.Sprite, x: int, y: int, shot_warning: int, direction: str, *groups):
        super().__init__(*groups)
        self.shot_warning = shot_warning
        self.direction = direction
        self.map = map
        self.warning()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * CELL_SIZE, y * CELL_SIZE
        self.speed_x, self.speed_y = CELL_SIZE * round(math.cos(math.radians(directions[direction]))), \
                                     CELL_SIZE * round(-math.sin(math.radians(directions[direction])))

    def get_shot_warning(self):
        return self.shot_warning

    def update(self, *args):
        self.shot_warning -= 1
        if self.shot_warning > 0:
            self.warning()
        elif not self.shot_warning:
            self.shoot()
        else:
            self.rect = self.rect.move(self.speed_x, self.speed_y)
            if not pygame.sprite.spritecollideany(self, self.map):
                self.kill()

    def shoot(self):
        self.image = pygame.transform.scale(
            pygame.transform.rotate(load_image("bulet.png"), directions[self.direction] - 45),
            (CELL_SIZE, CELL_SIZE))

    def warning(self):
        self.image = pygame.transform.scale(
            pygame.transform.rotate(load_image("direction.png", colorkey=-1), directions[self.direction]),
            (CELL_SIZE, CELL_SIZE))
        self.image.blit(pygame.font.Font(None, 40).render(f"{self.shot_warning}",
                                                          True, (0, 0, 0)), (CELL_SIZE * 0.4, CELL_SIZE * 0.3))


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    # Тесты работоспособности пуль.
    # for i in range(16):
    #     Bullet(map, 24, i, 5, "west", all_sprites, bullets)
    # for i in range(25):
    #     Bullet(map, i, 15, 10, "north", all_sprites, bullets)
    # Bullet(map, 0, 0, 4, "south-east", all_sprites, bullets)
    # for i in directions.keys():
    #     Bullet(map, 12, 8, 5, i, all_sprites, bullets)
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
        clock.tick(1)
