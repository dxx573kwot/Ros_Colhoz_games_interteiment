import random
import pygame
import os

from loadimage import load_image

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class Board(pygame.sprite.Sprite):
    def __init__(self, texture_pack: str, width: int, height: int, cell_size: int, *group):
        super().__init__(*group)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = 0
        self.top = 0
        texturs = [load_image(f"{texture_pack}/{i}") for i in os.listdir(f"Textur/{texture_pack}")]  # Текстурки
        # Оставил нулевые отступы на случай, если мы потом решим их добавить
        self.board = [[random.choice(texturs)
                       for _ in range(width)] for _ in range(height)]
        self.image = pygame.transform.scale(pygame.Surface([0, 0]), (self.width * self.cell_size, self.height * self.cell_size))
        self.render(self.image)
        self.rect = self.image.get_rect()

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, "white", (
                    self.left + j * self.cell_size, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                dog_surf = pygame.transform.scale(self.board[i][j],
                                                  (self.cell_size - 1, self.cell_size - 1))
                rot_rect = dog_surf.get_rect(
                    center=(self.left + j * self.cell_size + (self.cell_size / 2),
                            self.top + i * self.cell_size + (self.cell_size / 2)))
                screen.blit(dog_surf, rot_rect)

    def update(self, *args):
        self.image = self.image.convert_alpha()


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board("special_pack_1", 25, 14, CELL_SIZE, all_sprites, map)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

