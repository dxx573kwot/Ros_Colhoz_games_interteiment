import os
import random
import pygame
import cv2

from Map import Board
from Bullet import Bullet, directions
from Rocket import Rocket
from loadimage import load_image

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
rockets = pygame.sprite.Group()


class UncommonBoss(pygame.sprite.Sprite):
    def __init__(self, difficult: int, *groups):
        super().__init__(*groups)
        self.difficult = difficult

        self.frame = 0
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        result, image = self.cam.read()
        cv2.imwrite("Textur/stupid_a_piece_of_picture.png", image)
        self.image = pygame.transform.scale(load_image("stupid_a_piece_of_picture.png"), (CELL_SIZE * 3, CELL_SIZE * 3))
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

    def update(self, *args):
        self.frame += 1
        if self.frame > 25:
            self.frame = 0
            result, image = self.cam.read()
            cv2.imwrite("Textur/stupid_a_piece_of_picture.png", image)
            self.image = pygame.transform.scale(load_image("stupid_a_piece_of_picture.png"), (CELL_SIZE * 3, CELL_SIZE * 3))


# 11 6
if __name__ == "__main__":
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    board = Board("classic_pack", 25, 14, CELL_SIZE, all_sprites, map)
    boss = UncommonBoss(5, all_sprites, boss_group)
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
        clock.tick(50)
