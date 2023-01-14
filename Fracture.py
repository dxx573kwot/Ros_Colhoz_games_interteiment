import random
import pygame

from Map import Board
from loadimage import load_image
from Textur.cv.cv1 import screenshot

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()


class Fracture(pygame.sprite.Sprite):
    def __init__(self, board, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.Surface([0, 0], pygame.SRCALPHA), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.screen = board
        self.lines = {}
        self.color = (0, 0, 0)

    def create_fracture(self, pos):
        color = (254, 254, 254, 254)
        coords = []
        for i, j in ((1 * random.random(), 1 * random.random()),
                     (1 * random.random(), -1 * random.random()),
                     (-1 * random.random(), 1 * random.random()),
                     (-1 * random.random(), -1 * random.random())):
            start_x, start_y = pos
            while 0 < start_x < WIDTH and 0 < start_y < HEIGHT:
                next_x, next_y = random.randint(1, 20) * i * random.randint(0, 1), random.randint(1, 20) * j * random.randint(0, 1)
                coords.append(((start_x, start_y), (start_x + next_x, start_y + next_y)))
                start_x, start_y = start_x + next_x, start_y + next_y
        self.lines[tuple(coords)] = color

    def update(self, *args):
        new = {}
        for coords, color in self.lines.items():
            if color[3] > 0:
                color_2 = (color[0] - 2, color[1] - 2, color[2] - 2, 255)
                color = (color[0] - 2, color[1] - 2, color[2] - 2, color[3] - 2)
                for coord in coords:
                    pygame.draw.line(self.screen.image, color, *coord, 3)
                    pygame.draw.line(self.image, color_2, *coord, 3)
                new[coords] = color
        self.lines = new


if __name__ == "__main__":
    screenshot("Textur/cv/screenshot.png")
    screen = pygame.display.set_mode(SIZE)
    im = pygame.transform.scale(load_image("cv/screenshot.png"), (WIDTH, HEIGHT))
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    fr = Fracture(board, all_sprites)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                fr.create_fracture(pygame.mouse.get_pos())
        screen.blit(im, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
