import random
import pygame

pygame.init()
size = width, height = 1250, 800
all_sprites = pygame.sprite.Group()


class Fracture(pygame.sprite.Sprite):
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.Surface([0, 0], pygame.SRCALPHA), (width, height))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.color = (254, 254, 254)
        self.coords = []
        for i, j in ((1 * random.random(), 1 * random.random()),
                     (1 * random.random(), -1 * random.random()),
                     (-1 * random.random(), 1 * random.random()),
                     (-1 * random.random(), -1 * random.random())):
            start_x, start_y = self.pos
            while 0 < start_x < width and 0 < start_y < height:
                next_x, next_y = random.randint(1, 20) * i * random.randint(0, 1), random.randint(1, 20) * j * random.randint(0, 1)
                self.coords.append(((start_x, start_y), (start_x + next_x, start_y + next_y)))
                start_x, start_y = start_x + next_x, start_y + next_y

    def update(self, *args):
        if self.color[0] > 0 and self.color[1] > 0 and self.color[2] > 0:
            self.color = tuple(map(lambda x: x - 2, self.color))
        for coord in self.coords:
            pygame.draw.line(self.image, self.color, *coord)


if __name__ == "__main__":
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Fracture(pygame.mouse.get_pos(), all_sprites)
        screen.fill((120, 120, 120))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
