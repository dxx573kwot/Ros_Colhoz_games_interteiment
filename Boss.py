import random

import pygame
from Map import Board
from loadimage import load_image
from Bullet import Bullet, directions
from Rocket import Rocket

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
rockets = pygame.sprite.Group()


class Boss(pygame.sprite.Sprite):
    def __init__(self, image: str, columns: int, rows: int, difficult: int, *groups):
        super().__init__(*groups)
        self.difficult = difficult

        self.frames = []
        self.cut_sheet(load_image(image, -1), columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.fr = 0

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2 - self.rect.width // 2, HEIGHT // 2 - self.rect.height // 1.5
        self.mask = pygame.mask.from_surface(self.image)
        # Сложность и прочее
        self.min_number_bullet = 2 + difficult  # Минимальное количество пуль за одну атаку
        self.max_number_bullet = 4 + difficult  # Максимальное количество пуль за одну атаку
        self.min_delay = 3  # Минимальная задержка перед вылетом пули
        self.max_delay = 5  # Максимальная задержка перед вылетом пули
        self.kast_chance = 0.25 + difficult * 0.05  # Шанс атаки
        self.kast_rocket_chance = 0.15 + difficult * 0.05 # Шанс запуска ракеты

    def update(self, *args):
        self.fr += 1
        if self.fr >= 40 // len(self.frames):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.fr = 0

    def attack(self, bullet_group: tuple, rocket_group: tuple):
        if self.kast_chance >= random.random() or self.kast_chance >= 1:
            for _ in range(random.randint(self.min_number_bullet, self.max_number_bullet)):
                Bullet(bullet_group[0], random.randrange(0, WIDTH // CELL_SIZE), random.randrange(0, HEIGHT // CELL_SIZE - 2),
                       random.randint(self.min_delay, self.max_delay), random.choice([i for i in directions.keys()]),
                       bullet_group[1], bullet_group[2])
        if (self.kast_rocket_chance >= random.random() or self.kast_rocket_chance >= 1) and not rocket_group[1].sprites():
            for _ in range(random.randint(3, 5)):
                Rocket(rocket_group[0], random.randrange(0, WIDTH // CELL_SIZE), random.randrange(0, HEIGHT // CELL_SIZE - 2),
                  random.randint(5, 8), random.randint(15, 30), *rocket_group[1:])  # 15 30

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), (CELL_SIZE * 3, CELL_SIZE * 3)))


# 11 6
if __name__ == "__main__":
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    boss = Boss("boss1.jpg", 2, 1, 5, all_sprites, boss_group)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        rockets.update()
        boss.attack((map, all_sprites, bullets), (False, rockets))
        all_sprites.draw(screen)
        rockets.draw(screen)
        pygame.display.flip()
        clock.tick(2)
