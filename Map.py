import random

import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 10
        self.top = 10
        self.cell_size = 30
        if self.__class__.__name__ == "Board":
            self.board = [[random.choice(["Textur/CUMmen.jpg", "Textur/CUMmen_gold.jpg", "Textur/CUMmen_Iron.jpg"])
                           for _ in range(width)] for _ in range(height)]

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

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left <= x <= self.left + self.width * self.cell_size and \
                self.top <= y <= self.top + self.height * self.cell_size:
            return (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        return None

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1250, 600
    screen = pygame.display.set_mode(size)
    board = Board(25, 12)
    board.set_view(0, 0, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
