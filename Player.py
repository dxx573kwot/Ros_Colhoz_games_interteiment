import random
import pygame
from loadimage import load_image
from Map import Board
from Boss import Boss
from Fracture import Fracture
from Screen_redness import ScreenRedness

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
fractures = pygame.sprite.Group()
redness = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, gr, *group):
        super().__init__(*group)
        self.map = gr[0]
        self.boss = gr[1]
        self.cell_size = cell_size
        self.hp = 100
        self.render()
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.pos = self.rect
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        self.pos = self.rect  # Проверка на выход за пределы поля
        for i in args:
            if i and i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    self.rect = self.rect.move(self.cell_size, 0)
                    break
                elif i.key == pygame.K_DOWN:
                    self.rect = self.rect.move(0, self.cell_size)
                    break
                elif i.key == pygame.K_UP:
                    self.rect = self.rect.move(0, -self.cell_size)
                    break
                elif i.key == pygame.K_LEFT:
                    self.rect = self.rect.move(-self.cell_size, 0)
                    break
        # break нужен, чтобы игрок не ходил по диагонали
        if not pygame.sprite.spritecollideany(self, self.map) or pygame.sprite.collide_mask(self, self.boss):
            self.rect = self.pos

    def change_hp(self, fracture_groups=[], redness_groups=[], bullets=[], early_or_latter_input=False):
        if early_or_latter_input or self.rect == self.pos:
            ScreenRedness(redness_groups)
            self.hp -= 1
        for i in bullets:
            if pygame.sprite.collide_mask(self, i) and i.get_shot_warning() < 1:
                i.kill()
                self.hp -= 10
                pygame.mixer.Sound("Sounds/broken_glass.mp3").play()
                Fracture((self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2), fracture_groups)

    def render(self):
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                         (self.cell_size, self.cell_size))
        self.image.blit(pygame.font.Font(None, 20).render(f"{self.hp}",
                                                          True, (255, 0, 0)), (CELL_SIZE * 0.4, CELL_SIZE * 0.3))

    def get_hp(self):
        return self.hp


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board(25, 16, CELL_SIZE, all_sprites, map)
    boss = Boss((map, all_sprites, bullets), "boss12.jpg", 5, all_sprites, boss_group)
    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites)
    clock = pygame.time.Clock()
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update(*events)
        player.change_hp(fracture_groups=fractures, redness_groups=redness, bullets=bullets)
        player.render()
        fractures.update()
        redness.update()
        all_sprites.draw(screen)
        fractures.draw(screen)
        redness.draw(screen)
        pygame.display.flip()
        clock.tick(1)
