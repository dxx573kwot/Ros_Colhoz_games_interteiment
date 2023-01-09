import random
import pygame

pygame.init()
size = width, height = 1250, 800
all_sprites = pygame.sprite.Group()


class Fracture(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.Surface([0, 0], pygame.SRCALPHA), (width, height))
        self.rect = self.image.get_rect()
        self.lines = {}
        self.color = (0, 0, 0)

    def create_fracture(self, pos):
        color = (254, 254, 254)
        coords = []
        for i, j in ((1 * random.random(), 1 * random.random()),
                     (1 * random.random(), -1 * random.random()),
                     (-1 * random.random(), 1 * random.random()),
                     (-1 * random.random(), -1 * random.random())):
            start_x, start_y = pos
            while 0 < start_x < width and 0 < start_y < height:
                next_x, next_y = random.randint(1, 20) * i * random.randint(0, 1), random.randint(1, 20) * j * random.randint(0, 1)
                coords.append(((start_x, start_y), (start_x + next_x, start_y + next_y)))
                start_x, start_y = start_x + next_x, start_y + next_y
        self.lines[tuple(coords)] = color

    def update(self, *args):
        new = {}
        for coords, color in self.lines.items():
            if color[0] > 0 and color[1] > 0 and color[2] > 0:
                color = tuple(map(lambda x: x - 2, color))
                for coord in coords:
                    pygame.draw.line(self.image, color, *coord)
                self.lines[coords] = color
                new[coords] = color
        self.lines = new


if __name__ == "__main__":
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fr = Fracture(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                fr.create_fracture(pygame.mouse.get_pos())
        screen.fill((120, 120, 120))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
