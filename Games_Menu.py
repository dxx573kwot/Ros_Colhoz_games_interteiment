import random
import time
import librosa.display
import pygame
from multiprocessing import Process, Queue
from loadimage import load_image


class Board(pygame.sprite.Sprite):
    def __init__(self, width, height, cell_size):
        super().__init__(all_sprites)
        self.add(map)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = 0
        self.top = 0
        # Оставил нулевые отступы на случай, если мы потом решим их добавить
        self.board = [[random.choice(["Textur/CUMmen.jpg", "Textur/CUMmen_gold.jpg", "Textur/CUMmen_Iron.jpg"])
                       for _ in range(width)] for _ in range(height)]
        self.image = pygame.transform.scale(pygame.Surface([0, 0]), (WIDTH, HEIGHT))
        self.render(self.image)
        self.rect = self.image.get_rect()

    def render(self, screen):  # Генерация карты
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


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                            (cell_size, cell_size))
        self.cell_size = cell_size
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

    def update(self, *args):
        self.image = pygame.transform.scale(load_image(random.choice(["hero1.png", "hero2.png", "hero3.png"])),
                                            (CELL_SIZE, CELL_SIZE))
        start_pos = self.rect.copy()
        print(args)
        for i in args[0]:
            if i.type == pygame.KEYDOWN:
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
        if not pygame.sprite.spritecollideany(self, map):   # Проверка на выход за пределы поля
            self.rect = start_pos


class Musik_render(Process):
    def __init__(self, q, audio_data):
        Process.__init__(self)
        self.q = q
        self.audio_data = audio_data

    def run(self):
        print("Рендер " + self.audio_data + " начат")
        bits_in_minute = 60.0
        y, sr = librosa.load(self.audio_data)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                     trim=True)
        print("Рендер " + self.audio_data + " окончен")
        self.q.put([beat_frames, True])


def get_click(pos):
    if 1200 > pos[0] > 1000 and 600 > pos[1] > 500:
        return True
    else:
        return False


def draw_titri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("модные титры", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_titri_v_nachale_igri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("модные титры", True, (255, 255, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("в начале игры", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2 + 50
    text_y = HEIGHT // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_creator_oleg(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("от создателя олега", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_news(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("от создателя олега", True, (255, 255, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("чёт давно никаких новостей", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2 + 50
    text_y = HEIGHT // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_balli(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("более 90 баллов", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_drugie_igri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("более 90 баллов", True, (255, 255, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("есть у других проектов", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2 + 50
    text_y = HEIGHT // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_rehizer(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("режисёр", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_ne_nuhen(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("режисёр", True, (255, 255, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("здесь вообще не нужен", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2 + 50
    text_y = HEIGHT // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_name(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Round and bits", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_creator(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Round and bits", True, (255, 255, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("от Ros Colhoz Games intertaimont", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2 + 50
    text_y = HEIGHT // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_lkm(screen, i):
    if i:
        font = pygame.font.Font(None, 20)
        text = font.render("нажмите лкм для пропуска", True, (255, 255, 255))
        text_x = 1100
        text_y = 600
        screen.blit(text, (text_x, text_y))


def loading(screen, rotaite):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Loading", True, (255, 255, 255))
    text_x = 1000
    text_y = 500
    screen.blit(text, (text_x, text_y))
    dog_surf = pygame.image.load(
        'Textur/loading.png').convert()
    rot = pygame.transform.rotate(
        dog_surf, rotaite)
    rot_rect = rot.get_rect(
        center=(1200, 580))
    screen.blit(rot, rot_rect)


def musik_render(audio_data):
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    return beat_frames


def musik_render_Sacrifice(audio_data, q):
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    q.put([beat_frames, True])


def musik_render_Forever_Mine(audio_data, q):
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    q.put([beat_frames, True])


def musik_render_The_Jounrey_Home(audio_data, q):
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    q.put([beat_frames, True])


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    main2 = True
    first = True
    main = True
    game = False
    cutschen = True
    schena = True
    schena0 = False
    schena1 = False
    schena2 = False
    schena3 = False
    schena4 = False
    schena5 = False
    schena6 = False
    schena7 = False
    schena8 = False
    load = True
    rady = False
    roteit_hero = False
    up = False
    down = False
    left = False
    right = False
    rady1 = False
    rady2 = False
    rady3 = False
    wall_texture = ["Textur/CUMmen.jpg"]
    hero_texture = ["Textur/hero1.png", "Textur/hero2.png", "Textur/hero3.png"]
    invalid_texture = ["Textur/error1.png"]  # Textur/error1.png or Textur/error2.png
    color = 0
    roteit = 0
    a = 0
    i = 0.1
    toc = 0
    tic = 0
    audio_data_main = 'Musik/main.wav'
    audio_data_Sacrifice = 'Musik/Sacrifice.wav'
    audio_data_Forever_Mine = 'Musik/Forever_Mine.wav'
    audio_data_The_Jounrey_Home = 'Musik/The_Jounrey_Home.wav'
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    p = Musik_render(q1, "Musik/Sacrifice.wav")
    p2 = Musik_render(q2, "Musik/Forever_Mine.wav")
    p3 = Musik_render(q3, "Musik/The_Jounrey_Home.wav")
    p.start()
    p2.start()
    p3.start()
    a1 = q1.get()
    a2 = q2.get()
    a3 = q3.get()
    render_audio_Sacrifice = a1[0]
    render_audio_The_Forever_Mine = a2[0]
    render_audio_The_Jounrey_Home = a3[0]
    rady1 = a1[1]
    rady2 = a2[1]
    rady3 = a3[1]
    print(rady1, rady2, rady3)
    pygame.mixer.music.load(audio_data_main)
    pygame.mixer.music.play(-1)
    point_map = [
        [(54, 54), (182, 54), (310, 54), (438, 54), (566, 54), (694, 54), (822, 54), (950, 54), (1078, 54), (1206, 54)],
        [(54, 182), (182, 182), (310, 182), (438, 182), (566, 182), (694, 182), (822, 182), (950, 182), (1078, 182),
         (1206, 182)],
        [(54, 310), (182, 310), (310, 310), (438, 310), (566, 310), (694, 310), (822, 310), (950, 310), (1078, 310),
         (1206, 310)],
        [(54, 438), (182, 438), (310, 438), (438, 438), (566, 438), (694, 438), (822, 438), (950, 438), (1078, 438),
         (1206, 438)],
        [(54, 566), (182, 566), (310, 566), (438, 566), (566, 566), (694, 566), (822, 566), (950, 566), (1078, 566),
         (1206, 566)]]
    '''
    коды объектов:
    H - персонаж
    s - задний фон
    '''
    hit_map = [[["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"]],
               [["s"], ["s"], ["H"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"]],
               [["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"]],
               [["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"]],
               [["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"], ["s"]]]

    fullscreen = False

    pygame.init()
    SIZE = WIDTH, HEIGHT = 1250, 800
    CELL_SIZE = 50
    screen = pygame.display.set_mode(SIZE)
    all_sprites = pygame.sprite.Group()
    map = pygame.sprite.Group()
    board = Board(25, 16, CELL_SIZE)
    player = Player(3, 3, CELL_SIZE)

    if fullscreen:
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(SIZE)
    while run:
        events = pygame.event.get()
        if main:
            if cutschen == False and (rady1 == False or rady2 == False or rady3 == False):
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                loading(screen, roteit)
                roteit += 1
                pygame.display.flip()
            elif cutschen:
                if schena:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_titri(screen, color)
                        color = 0
                        time.sleep(1)
                        schena = False
                        schena0 = True
                        pygame.display.flip()
                        continue
                    draw_titri(screen, color)
                    color += 1
                    time.sleep(0.01)
                    pygame.display.flip()
                elif schena0:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_titri_v_nachale_igri(screen, color)
                        color = 0
                        time.sleep(1)
                        schena0 = False
                        schena1 = True
                        pygame.display.flip()
                        continue
                    draw_titri_v_nachale_igri(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena1:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_creator_oleg(screen, color)
                        color = 0
                        time.sleep(1)
                        schena1 = False
                        schena2 = True
                        pygame.display.flip()
                        continue
                    draw_creator_oleg(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena2:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_news(screen, color)
                        color = 0
                        time.sleep(3)
                        schena2 = False
                        schena3 = True
                        pygame.display.flip()
                        continue
                    draw_news(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena3:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_balli(screen, color)
                        color = 0
                        time.sleep(3)
                        schena3 = False
                        schena4 = True
                        pygame.display.flip()
                        continue
                    draw_balli(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena4:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_drugie_igri(screen, color)
                        color = 0
                        time.sleep(3)
                        schena4 = False
                        schena5 = True
                        pygame.display.flip()
                        continue
                    draw_drugie_igri(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena5:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_rehizer(screen, color)
                        color = 0
                        time.sleep(3)
                        schena5 = False
                        schena6 = True
                        pygame.display.flip()
                        continue
                    draw_rehizer(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena6:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_ne_nuhen(screen, color)
                        color = 0
                        time.sleep(3)
                        schena6 = False
                        schena7 = True
                        pygame.display.flip()
                        continue
                    draw_ne_nuhen(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena7:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_name(screen, color)
                        color = 0
                        time.sleep(3)
                        schena7 = False
                        schena8 = True
                        pygame.display.flip()
                        continue
                    draw_name(screen, color)
                    color += 1
                    time.sleep(0.01)
                elif schena8:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cutschen = False
                    if color == 255:
                        draw_creator(screen, color)
                        color = 0
                        time.sleep(3)
                        schena8 = False
                        pygame.display.flip()
                        cutschen = False
                        continue
                    draw_creator(screen, color)
                    color += 1
                    time.sleep(0.01)
                draw_lkm(screen, main2)
            else:
                # меню
                main2 = False
                sun_surf = pygame.image.load('Textur/main.jpg')
                sun_rect = sun_surf.get_rect()
                screen.blit(sun_surf, sun_rect)
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if get_click(event.pos):
                            main = False
                            game = True

            pygame.display.flip()
        elif game:  # НАЧАЛО ИГРЫ
            if first:
                pygame.mixer.music.load(audio_data_Sacrifice)
                pygame.mixer.music.play()
                first = False
                tic = time.perf_counter()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            if toc > render_audio_Sacrifice[a]:
                print("Bit!")
                a += 1
            toc = time.perf_counter() - tic
            screen.fill((0, 0, 0))
            all_sprites.update(events)
            all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(60)
