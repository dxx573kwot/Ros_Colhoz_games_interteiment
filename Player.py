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
    def __init__(self, x: int, y: int, cell_size: int, groups: tuple, *group):
        super().__init__(*group)
        self.map = groups[0]
        self.boss = groups[1]
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

    def change_hp(self, fracture, redness_groups=[], bullets=[], rockets=[], early_or_latter_input=False,
                  move_check=True):
        if (early_or_latter_input or self.rect == self.pos) and move_check:
            ScreenRedness(redness_groups)
            pygame.mixer.Sound("Sounds/downed_rhythm.mp3").play()
            self.hp -= 1
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet) and bullet.get_shot_warning() < 1:
                bullet.kill()
                self.hp -= 10
                pygame.mixer.Sound("Sounds/broken_glass.mp3").play()
                fracture.create_fracture((self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))
        for rocket in rockets:
            if pygame.sprite.collide_mask(self, rocket) and rocket.get_shot_warning() < 1 and not rocket.get_hit():
                rocket.set_hit(True)
                self.hp -= 20
                for _ in range(3):
                    fracture.create_fracture((self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))

    def render(self):
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                            (self.cell_size, self.cell_size))
        self.image.blit(pygame.font.Font(None, 20).render(f"{self.hp}",
                                                          True, (255, 0, 0)), (CELL_SIZE * 0.4, CELL_SIZE * 0.3))

    def get_hp(self):
        return self.hp

    def get_pos(self):
        return self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE

    def cheat_hp(self):
        self.hp += 10000


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board("classic_pack", 25, 14, CELL_SIZE, all_sprites, map)
    boss = Boss((map, all_sprites, bullets), "boss12.jpg", 5, all_sprites, boss_group)
    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites)
    fr = Fracture(fractures)
    clock = pygame.time.Clock()
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update(*events)
        player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets)
        player.render()
        fractures.update()
        redness.update()
        all_sprites.draw(screen)
        fractures.draw(screen)
        redness.draw(screen)
        pygame.display.flip()
        clock.tick(1)
