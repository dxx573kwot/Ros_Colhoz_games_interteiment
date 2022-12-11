import random
import pygame
from Map import Board


class Player(Board):
    def __init__(self, x, y, width_board, height_board):
        super().__init__(width_board, height_board)
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        x, y = self.get_coords()
        if direction == "up":
            self.set_coords(x, y - 1)
        elif direction == "down":
            self.set_coords(x, y + 1)
        elif direction == "left":
            self.set_coords(x - 1, y)
        elif direction == "right":
            self.set_coords(x + 1, y)
        x_new, y_new = self.get_coords()
        if x_new < 0 or x_new > self.width - 1 or y_new < 0 or y_new > self.height - 1:
            self.set_coords(x, y)

    def render(self, screen):
        dog_surf = pygame.transform.scale(
            pygame.image.load(random.choice(['Textur/hero1.png', 'Textur/hero2.png', 'Textur/hero3.png'])),
            (self.cell_size - 1, self.cell_size - 1))
        rot_rect = dog_surf.get_rect(
            center=(self.left + self.x * self.cell_size + (self.cell_size / 2),
                    self.top + self.y * self.cell_size + (self.cell_size / 2)))
        screen.blit(dog_surf, rot_rect)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1250, 800
    screen = pygame.display.set_mode(size)
    board = Board(25, 16)
    board.set_view(0, 0, 50)
    hero = Player(3, 3, 25, 16)
    hero.set_view(0, 0, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.move("right")
                if event.key == pygame.K_DOWN:
                    hero.move("down")
                if event.key == pygame.K_UP:
                    hero.move("up")
                if event.key == pygame.K_LEFT:
                    hero.move("left")
        screen.fill((0, 0, 0))
        board.render(screen)
        hero.render(screen)
        pygame.display.flip()
