import pygame
from Map import Board
from Player import Player


class RoundAndBits:
    def __init__(self, map, player):
        self.map = map
        self.player = player

    def render(self, screen):
        self.map.render(screen)
        self.player.render(screen)

    def set_view(self, left, top, cell_size):
        self.map.set_view(left, top, cell_size)
        self.player.set_view(left, top, cell_size)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1250, 800
    screen = pygame.display.set_mode(size)

    WIDTH, HEIGHT, CELL_SIZE = 25, 16, 50

    board = Board(WIDTH, HEIGHT)
    hero = Player(3, 3, WIDTH, HEIGHT)
    game = RoundAndBits(board, hero)
    game.set_view(0, 0, 50)

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
        game.render(screen)
        pygame.display.flip()
