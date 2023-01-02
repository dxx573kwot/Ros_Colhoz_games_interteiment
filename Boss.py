import random

import pygame
from Map import Board
from loadimage import load_image
from Bullet import Bullet, directions

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()


class Boss(pygame.sprite.Sprite):
    def __init__(self, bullet_group, image, difficult, *groups):
        super().__init__(*groups)
        self.difficult = difficult
        self.bullet_group = bullet_group
        self.image = pygame.transform.scale(load_image(image, -1), (CELL_SIZE * 3, CELL_SIZE * 3))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2 - self.rect.width // 2, HEIGHT // 2 - self.rect.height // 1.5
        self.mask = pygame.mask.from_surface(self.image)
        # Сложность и прочее
        self.min_number_bullet = 2 + difficult  # Минимальное количество пуль за одну атаку
        self.max_number_bullet = 4 + difficult  # Максимальное количество пуль за одну атаку
        self.min_delay = 3  # Минимальная задержка перед вылетом пули
        self.max_delay = 5  # Максимальная задержка перед вылетом пули
        self.kast_chance = 0.25 + difficult * 0.05  # Шанс атаки

    def update(self, *args):
        if self.kast_chance >= random.random() or self.kast_chance >= 1:
            for _ in range(random.randint(self.min_number_bullet, self.max_number_bullet)):
                Bullet(self.bullet_group[0], random.randrange(0, WIDTH // CELL_SIZE), random.randrange(0, HEIGHT // CELL_SIZE - 2),
                       random.randint(self.min_delay, self.max_delay), random.choice([i for i in directions.keys()]),
                       self.bullet_group[1], self.bullet_group[2])


# 11 6
if __name__ == "__main__":
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    boss = Boss((map, all_sprites, bullets), "boss12.jpg", 5, all_sprites, boss_group)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(2)
