import time
import librosa.display
import pygame
from multiprocessing import Process, Queue
import random

from Hotbar import Hotbar
from Map import Board
from Player import Player
from Boss import Boss


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


def get_main(pos):
    if 132 >= pos[1] >= 39:
        return "лёгкий"
    elif 286 >= pos[1] >= 238:
        return "средний"
    elif 438 >= pos[1] >= 393:
        return "тяжёлый"
    else:
        return "ERROR"


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
    text_x = WIDTH // 2 - text.get_width() // 2 + 100
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
        text_x = 1000
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


def sniper(cor):
    dog_surf = pygame.image.load(
        'Textur/popal.png')
    rot_rect = dog_surf.get_rect(
        center=cor)
    screen.blit(dog_surf, rot_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("снайперская рота ждёт тебя", True, (color, color, color))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = 600
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    pygame.mixer.music.load("Musik/piu.wav")
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.load("Musik/reload.wav")
    pygame.mixer.music.play()
    time.sleep(3)


def game_over(text, restart_text):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(text, True, (255, 0, 0))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    restart(restart_text)
    quit()


def restart(text):
    font = pygame.font.Font(None, 50)
    text = font.render(text, True, (255, 0, 0))  # random.choice(["пострадать ещё раз!", "хочу ещё!"])
    text_x = 850
    text_y = 730
    screen.blit(text, (text_x, text_y))


def quit():
    font = pygame.font.Font(None, 50)
    text = font.render("выйти", True, (255, 0, 0))
    text_x = 50
    text_y = 730
    screen.blit(text, (text_x, text_y))


def tap_restart(pos):
    if 1215 > pos[0] > 843 and 764 > pos[1] > 734:
        return True
    return False


def tap_quit(pos):
    if 163 > pos[0] > 48 and 767 > pos[1] > 728:
        return True
    return False


def da(pos):
    if 83 > pos[0] > 42 and 267 > pos[1] > 245:
        return True
    return False


def net(pos):
    if 349 > pos[0] > 311 and 267 > pos[1] > 245:
        return True
    return False


def fullscren_dialog():
    SIZE = WIDTH, HEIGHT = 400, 300
    run = True
    screen = pygame.display.set_mode(SIZE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if da(pos):
                    return True
                if net(pos):
                    return False
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 35)
        text = font.render("Полноэкранный режим?", True, (255, 255, 255))
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = HEIGHT // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        text = font.render("Да", True, (255, 255, 255))
        text_x = 50
        text_y = 250
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        text = font.render("Нет", True, (255, 255, 255))
        text_x = 315
        text_y = 250
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    main2 = True
    first = True
    main = True
    main1 = True
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
    rady2 = False
    rady3 = False
    seting = False
    light = False
    medium = False
    hard = False
    life = True
    text = ["Игра отстой!", "Садись, два по киберспорту!", "Не бей пожалуйста :)"]  # любой текст окончания игры
    restart_text = ["пострадать ещё раз!", "хочу ещё!"]
    text_over = random.choice(text)
    text_restart = random.choice(restart_text)
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

    fullscreen = fullscren_dialog()

    pygame.init()
    SIZE = WIDTH, HEIGHT = 1250, 800
    CELL_SIZE = 50
    FPS = 60
    screen = pygame.display.set_mode(SIZE)

    all_sprites = pygame.sprite.Group()
    map = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    hotbar_elements = pygame.sprite.Group()

    board = Board(25, 14, CELL_SIZE, map, all_sprites)
    boss = Boss((map, all_sprites, bullets), "boss12.jpg", 5, all_sprites, boss_group)
    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites)
    hotbar = Hotbar((hotbar_elements,), (all_sprites,), all_sprites)
    player_move = False  # Изначально персонаж не двигается
    music_start = True

    if fullscreen:
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(SIZE)
    pygame.mixer.music.load(audio_data_main)
    pygame.mixer.music.play(-1)
    while run:
        if main:
            if cutschen == False and (rady1 == False or rady2 == False or rady3 == False):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                loading(screen, roteit)
                roteit += 1
                pygame.display.flip()
            elif cutschen:
                if schena:
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
                    for event in pygame.event.get():
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
            elif main1:
                # меню
                main2 = False
                sun_surf = pygame.image.load('Textur/main.jpg')
                sun_rect = sun_surf.get_rect()
                screen.blit(sun_surf, sun_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if get_click(event.pos):
                            main1 = False
                            # game = True
            else:
                sun_surf = pygame.image.load('Textur/load.png')
                sun_rect = sun_surf.get_rect()
                screen.blit(sun_surf, sun_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        fgh = get_main(event.pos)
                        if fgh == "лёгкий":
                            light = True
                            main = False
                            game = True
                        elif fgh == "средний":
                            medium = True
                            main = False
                            game = True
                        elif fgh == "тяжёлый":
                            hard = True
                            main = False
                            game = True
                        elif fgh == "ERROR":
                            sniper(event.pos)
                            print("снайперская рота ждёт тебя")
            pygame.display.flip()
        elif game:  # НАЧАЛО ИГРЫ
            events = pygame.event.get()
            if light:
                if first:
                    first = False
                    pygame.mixer.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                print("Выход")
                            if tap_restart(pos):
                                print("restart")
                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            player_move = event

                if toc > render_audio_Sacrifice[a]:
                    hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                    a += 1
                if toc > 3.35 and music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_Sacrifice)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(player_move, *events)
                    player.change_hp(bullets=bullets)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    player.change_hp(bullets=bullets, early_or_latter_input=True)
                elif player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(early_or_latter_input=True)

                hotbar_elements.update()
                screen.fill((0, 0, 0))
                player.render()
                all_sprites.draw(screen)
                hotbar_elements.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text)
                    text_restart = random.choice(restart_text)
                    life = False
            elif medium:
                pass
            elif hard:
                pass
            pygame.display.flip()
            clock.tick(FPS)
            player_move = False
