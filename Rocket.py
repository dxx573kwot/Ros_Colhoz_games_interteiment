import pygame
from Map import Board
from loadimage import load_image

pygame.init()
SIZE = WIDTH, HEIGHT = 1250, 800
CELL_SIZE = 50
all_sprites = pygame.sprite.Group()
map = pygame.sprite.Group()
rockets = pygame.sprite.Group()


class Rocket(pygame.sprite.Sprite):
    def __init__(self, player: pygame.sprite.Sprite, x: int, y: int, shot_warning: int, live: int, *groups):
        super().__init__(*groups)

        self.frames = []
        self.cut_sheet(load_image("exploooosion.png", -1), 6, 2)
        self.cur_frame = 0
        self.fr = 49.5

        self.move = False
        self.hit = False
        self.im = load_image("rocket.png")
        self.shot_warning = shot_warning
        self.live = live
        self.player = player
        self.warning()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * CELL_SIZE, y * CELL_SIZE

    def get_shot_warning(self):
        return self.shot_warning

    def update(self, *args):  # *self.player.get_pos()
        change_x, change_y = self.has_path(self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE, *self.player.get_pos())
        new_x, new_y = (change_x - self.rect.x // CELL_SIZE), (change_y - self.rect.y // CELL_SIZE)
        self.shot_warning -= 1
        if self.shot_warning > 0:
            self.warning()
        elif not self.shot_warning:
            self.render((new_x, new_y))
        elif self.live > 0:
            if self.move:
                self.render((new_x, new_y))
                self.rect = self.rect.move(new_x * CELL_SIZE, new_y * CELL_SIZE)
                self.live -= 1
            self.move = not self.move
        if (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE) == self.player.get_pos() and self.shot_warning < 1:
            self.live = 0

    def explosion(self):
        if self.fr == 49.5 and self.live < 1:
            self.rect.x, self.rect.y = self.rect.x - CELL_SIZE, self.rect.y - CELL_SIZE
            pygame.mixer.Sound("Sounds/rocket explosion.mp3").play()
        if self.live < 1:
            self.fr += 1
            if self.fr >= 50 // len(self.frames):
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                if not self.cur_frame:
                    self.kill()
                self.image = self.frames[self.cur_frame]
                self.fr = 1

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), (CELL_SIZE * 3, CELL_SIZE * 3)))

    def render(self, coords):
        rotate = -1
        if coords == (1, 1):
            rotate = 315
        elif coords == (0, 1):
            rotate = 270
        elif coords == (-1, 1):
            rotate = 225
        elif coords == (-1, 0):
            rotate = 180
        elif coords == (-1, -1):
            rotate = 135
        elif coords == (0, -1):
            rotate = 90
        elif coords == (1, -1):
            rotate = 45
        elif coords == (1, 0):
            rotate = 0
        self.image = pygame.transform.scale(pygame.transform.rotate(self.im, rotate), (CELL_SIZE, CELL_SIZE))

    def warning(self):
        self.image = pygame.transform.scale(load_image("rocket_warning.png"), (CELL_SIZE, CELL_SIZE))
        self.image.blit(pygame.font.Font(None, 30).render(f"{self.shot_warning}",
                                                          True, (0, 0, 0)), (CELL_SIZE * 0.4, CELL_SIZE * 0.3))

    def has_path(self, x1, y1, x2, y2):
        start = (x1, y1)
        target = (x2, y2)
        INF = 1000
        x, y = start
        distance = [[INF] * 25 for _ in range(16)]
        distance[y][x] = 0
        prev = [[None] * 25 for _ in range(16)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1):
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < 25 and 0 <= next_y < 16 and distance[next_y][next_x] == INF:
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = target
        if distance[y][x] == INF or start == target:
            return start
        while prev[y][x] != start:
            x, y = prev[y][x]
        return x, y

    def set_hit(self, hit):
        self.hit = hit

    def get_hit(self):
        return self.hit


if __name__ == "__main__":
    screen = pygame.display.set_mode(SIZE)
    board = Board("classic_pack", 25, 14, CELL_SIZE, all_sprites, map)
    r = Rocket(False, 10, 10, 5, 30, all_sprites, rockets)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update()
        r.explosion()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(1)
