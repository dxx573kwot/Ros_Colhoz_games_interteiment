import pygame
from Map import Board

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
FPS = 60
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class HotbarElement(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.Surface([0, 0]), (10, 50))
        pygame.draw.rect(self.image, "yellow", (0, 0, 4000, 1000))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.condition = 0  # Элемент не дошёл до сердца - 0, в пределах сердца - 1.

    def update(self, *args):
        self.rect = self.rect.move(250 / FPS, 0)

    def change_condition(self):
        self.condition += 1

    def get_condition(self):
        return self.condition


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 14, CELL_SIZE, all_sprites, map)
    h1 = HotbarElement(WIDTH * 0.1, HEIGHT * 0.93 - 20, all_sprites)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
