import random
import pygame
from loadimage import load_image
from Map import Board

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, map, *group):
        super().__init__(*group)
        self.map = map
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                            (cell_size, cell_size))
        self.cell_size = cell_size
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def update(self, *args):
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                            (CELL_SIZE, CELL_SIZE))
        start_pos = self.rect.copy()  # Проверка на выход за пределы поля
        for i in args:
            if i and i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    self.rect = self.rect.move(self.cell_size, 0)
                    break
                elif i.key == pygame.K_DOWN:
                    self.rect = self.rect.move(0, self.cell_size)
                    break
                elif i.key == pygame.K_UP:
                    self.rect = self.rect.move(0, -self.cell_size)
                    break
                elif i.key == pygame.K_LEFT:
                    self.rect = self.rect.move(-self.cell_size, 0)
                    break
        # break нужен, чтобы игрок не ходил по диагонали
        if not pygame.sprite.spritecollideany(self, self.map):
            self.rect = start_pos


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    player = Player(3, 3, CELL_SIZE, map, all_sprites)
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update(False, *events)
        all_sprites.draw(screen)
        pygame.display.flip()
