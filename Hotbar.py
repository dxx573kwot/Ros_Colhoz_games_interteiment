import time

import pygame
from Map import Board
from HotbarElement import HotbarElement
from Heart import Heart

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
FPS = 60
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
hotbar_elements = pygame.sprite.Group()
heart_group = pygame.sprite.Group()


class Hotbar(pygame.sprite.Sprite):
    def __init__(self, elements_group: tuple, heart_group: tuple, *group):
        super().__init__(*group)
        self.elements_group = elements_group
        self.image = pygame.transform.scale(pygame.Surface([0, 0]), (900, 10))
        pygame.draw.rect(self.image, "violet", (0, 0, 4000, 1000))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.1
        self.rect.y = HEIGHT * 0.93
        self.h = Heart(*heart_group)

    def create_hotbar_element(self):
        HotbarElement(self.rect.x, self.rect.y - 20, *self.elements_group)

    def get_heart(self):
        return self.h


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board("classic_pack", 25, 14, CELL_SIZE, all_sprites, map)
    hotbar = Hotbar((all_sprites, hotbar_elements), (all_sprites, heart_group), all_sprites)
    hotbar.create_hotbar_element()
    clock = pygame.time.Clock()
    t = time.perf_counter()

    ti = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        if pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True):
            print(time.perf_counter() - t)
            ti.append(time.perf_counter() - t)
            t = time.perf_counter()
            hotbar.create_hotbar_element()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    print(f"Среднее время: {sum(ti) / len(ti)}")