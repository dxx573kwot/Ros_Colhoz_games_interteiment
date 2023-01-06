import pygame
from loadimage import load_image

pygame.init()
size = width, height = 1250, 800
all_sprites = pygame.sprite.Group()


class ScreenRedness(pygame.sprite.Sprite):
    def __init__(self, group):
        for i in group.sprites():
            i.kill()
        super().__init__(group)
        self.image = pygame.transform.scale(load_image("red_screen.png"), (width, height))
        self.rect = self.image.get_rect()
        self.alfa = 255
        self.color = (254, 254, 254)

    def update(self, *args):
        self.alfa -= 1
        self.image.set_alpha(self.alfa)
        if self.image.get_alpha() < 1:
            self.kill()


if __name__ == "__main__":
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ScreenRedness(all_sprites)
        screen.fill((255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
