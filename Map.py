import random
import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
screen = pygame.display.set_mode(SIZE)
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class Board(pygame.sprite.Sprite):
    def __init__(self, width, height, cell_size):
        super().__init__(all_sprites)
        self.add(map)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = 0
        self.top = 0
        # Оставил нулевые отступы на случай, если мы потом решим их добавить
        self.board = [[random.choice(["Textur/CUMmen.jpg", "Textur/CUMmen_gold.jpg", "Textur/CUMmen_Iron.jpg"])
                           for _ in range(width)] for _ in range(height)]
        self.image = pygame.transform.scale(pygame.Surface([0, 0]), (WIDTH, HEIGHT))
        self.render(self.image)
        self.rect = self.image.get_rect()

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, "white", (
                    self.left + j * self.cell_size, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                dog_surf = pygame.transform.scale(pygame.image.load(self.board[i][j]),
                                                  (self.cell_size - 1, self.cell_size - 1))
                rot_rect = dog_surf.get_rect(
                    center=(self.left + j * self.cell_size + (self.cell_size / 2),
                            self.top + i * self.cell_size + (self.cell_size / 2)))
                screen.blit(dog_surf, rot_rect)


if __name__ == "__main__":
    board = Board(25, 16, CELL_SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
