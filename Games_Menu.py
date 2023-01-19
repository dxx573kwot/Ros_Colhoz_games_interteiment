import time
import librosa.display
import pygame
from multiprocessing import Process, Queue
import random
import matplotlib
import pyautogui
import keyboard
import os
from Hotbar import Hotbar
from Map import Board
from Player import Player
from Boss import Boss
from Fracture import Fracture
from loadimage import load_image


class Musik_render(Process):
    def __init__(self, q, audio_data, bits_in_minute):
        Process.__init__(self)
        self.q = q
        self.bits_in_minute = bits_in_minute
        self.audio_data = audio_data

    def run(self):
        print("Рендер " + self.audio_data + " начат")
        bits_in_minute = self.bits_in_minute
        y, sr = librosa.load(self.audio_data)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        if bits_in_minute != -1:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                         trim=True)
        else:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)
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
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time",
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
    text = font.render("снайперская рота ждёт тебя", True, (255, 255, 255))
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


def get_final(pos):
    if 261 > pos[0] > 53 and 124 > pos[1] > 96:
        return True
    return False


def get_privat_musik(pos):
    if 1203 > pos[0] > 1094 and 723 > pos[1] > 695:
        return True
    return False


# Add by dxx573kwot


def add_score(name, score):
    f = open('score.txt', 'w')
    f.write(name + "///" + str(score) + '\n')
    f.close()


def get_any_score():
    f = open('score.txt', 'r')
    score = {

    }
    for index in f.read().split("\n"):
        score[index.split("///")[0]] = index.split("///")[1]
    f.close()
    return score


def get_name_score(name):
    try:
        return get_any_score()[name]
    except IndexError:
        return "ERROR1"


def screenshot(file):
    keyboard.press("alt+tab")
    time.sleep(0.1)
    keyboard.press("left")
    keyboard.release("left")
    keyboard.press("left")
    keyboard.release("left")
    keyboard.release("alt+tab")
    time.sleep(3)
    pyautogui.screenshot(file)


def take_name(keybrd, tap):
    SIZE = WIDTH, HEIGHT = 1250, 800
    screen = pygame.display.set_mode(SIZE)
    run = True
    a = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                try:
                    if keybrd[event.key] == "dell":
                        if len(a) != 0:
                            a = a[:-1]
                            pygame.mixer.Sound(random.choice(tap)).play()
                    elif keybrd[event.key] == "continue":
                        pygame.mixer.Sound(random.choice(tap)).play()
                        if len(a) != 0:
                            return a
                    else:
                        a += keybrd[event.key]
                        pygame.mixer.Sound(random.choice(tap)).play()
                except KeyError:
                    continue
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 35)
        text = font.render(a, True, (255, 255, 255))
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = HEIGHT // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 35)
        text = font.render("Ваш никнейм", True, (255, 255, 255))
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = 100
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()


def who_boss_the_gym():
    f = open('who_is_my_boss.txt', 'r')
    a = f.read()
    if a == "I":
        f.close()
        return True
    f.close()
    return False


if __name__ == '__main__':
    pygame.init()

    screenshot("Textur/cv/screenshot.png")

    print(matplotlib.get_data_path())
    print(os.cpu_count())

    I = who_boss_the_gym()

    clock = pygame.time.Clock()
    run = True
    run2 = True
    first = True
    part1 = True
    part2 = False
    part3 = False
    part4 = False
    part5 = False
    part6 = False
    part7 = False
    main2 = True
    first2 = True
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
    rady3 = False
    seting = False
    light = False
    medium = False
    hard = False
    secret_level1 = False
    secret_level2 = False
    life = True
    chaet_menu = False
    final = False
    win = False
    complite_light = False
    complite_medium = False
    complite_hard = False
    final2 = False
    text123 = ["Игра отстой!", "Садись, два по киберспорту!", "Не бей пожалуйста :)"]  # любой текст окончания игры
    restart_text = ["пострадать ещё раз!", "хочу ещё!"]
    text_over = random.choice(text123)
    text_restart = random.choice(restart_text)
    wall_texture = ["Textur/CUMmen.jpg"]
    hero_texture = ["Textur/hero1.png", "Textur/hero2.png", "Textur/hero3.png"]
    invalid_texture = ["Textur/error1.png"]  # Textur/error1.png or Textur/error2.png
    tap = ['Musik/keybord/tap1.wav', 'Musik/keybord/tap2.wav', 'Musik/keybord/tap3.wav', 'Musik/keybord/tap4.wav']
    space = ['Musik/keybord/space.wav', 'Musik/keybord/space2.wav']
    color = 0
    roteit = 0
    a = 0
    i = 0.1
    toc = 0
    tic = 0
    b = 0
    c = 0
    audio_data_main = 'Musik/main.wav'
    audio_data_Sacrifice = 'Musik/The_Jounrey_Home.wav'  # Musik/test.wav Musik/The_Jounrey_Home.wav Musik/Sacrifice.wav
    audio_data_Forever_Mine = 'Musik/Forever_Mine.wav'
    # audio_data_Sacrifice = 'Musik/test.wav'
    audio_data_secret1 = 'Musik/Riverside.wav'
    audio_data_secret2 = 'Musik/I.wav'
    audio_data_The_Jounrey_Home = 'Musik/Sacrifice.wav'
    if os.cpu_count() <= 4:
        q1 = Queue()
        q2 = Queue()
        q3 = Queue()
        p = Musik_render(q1, audio_data_Sacrifice, 60)
        p2 = Musik_render(q2, audio_data_Forever_Mine, 90)
        p3 = Musik_render(q3, audio_data_The_Jounrey_Home, 120)
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
        q1 = Queue()
        q2 = Queue()
        p = Musik_render(q1, audio_data_secret1, -1)
        p2 = Musik_render(q2, audio_data_secret2, -1)
        p.start()
        p2.start()
        a1 = q1.get()
        a2 = q2.get()
        render_audio_secret1 = a1[0]
        render_audio_secret2 = a2[0]
    else:
        q1 = Queue()
        q2 = Queue()
        q3 = Queue()
        q4 = Queue()
        q5 = Queue()
        p = Musik_render(q1, audio_data_Sacrifice, 60)
        p2 = Musik_render(q2, audio_data_Forever_Mine, 90)
        p3 = Musik_render(q3, audio_data_The_Jounrey_Home, 120)
        p4 = Musik_render(q4, audio_data_secret1, -1)
        p5 = Musik_render(q5, audio_data_secret2, -1)
        p.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        a1 = q1.get()
        a2 = q2.get()
        a3 = q3.get()
        a4 = q4.get()
        a5 = q5.get()
        render_audio_Sacrifice = a1[0]
        render_audio_The_Forever_Mine = a2[0]
        render_audio_The_Jounrey_Home = a3[0]
        render_audio_secret1 = a4[0]
        render_audio_secret2 = a5[0]
        rady1 = a1[1]
        rady2 = a2[1]
        rady3 = a3[1]
    a2 = ""
    keybrd = {113: 'q', 119: 'w', 101: 'e', 114: 'r', 116: 't', 121: 'y', 117: 'u', 105: 'i', 111: 'o', 112: 'p',
              97: 'a', 115: 's', 100: 'd', 102: 'f', 103: 'g', 104: 'h', 106: 'j', 107: 'k', 108: 'l', 122: 'z',
              120: 'x', 99: 'c', 118: 'v', 98: 'b', 110: 'n', 109: 'm', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5',
              54: '6', 55: '7', 56: '8', 57: '9', 48: "0", 8: "dell", 13: "continue"}
    numpad = {49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 48: '0'}
    secret_cod = ""
    print(rady1, rady2, rady3)
    print("время запуска составило " + str(time.process_time()))
    player_name = take_name(keybrd, tap)
    print("Привет " + player_name)
    fullscreen = fullscren_dialog()
    pygame.init()
    SIZE = WIDTH, HEIGHT = 1250, 800
    CELL_SIZE = 50
    FPS = 60
    screen = pygame.display.set_mode(SIZE)
    secret_screen = pygame.transform.scale(load_image("cv/screenshot.png"), (CELL_SIZE * 25, CELL_SIZE * 14))

    all_sprites = pygame.sprite.Group()
    map = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    hotbars = pygame.sprite.Group()
    hotbar_elements = pygame.sprite.Group()
    fractures = pygame.sprite.Group()
    redness = pygame.sprite.Group()

    is_player_move = False  # Изначально персонаж не двигается
    is_music_start = True
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
            elif final:
                while run2:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run2 = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pass
                    screen.fill((0, 0, 0))
                    if part1:
                        font = pygame.font.Font(None, 35)
                        text = font.render("Загадочная личность 1:", True, (255, 255, 255))
                        text_x = 60
                        text_y = 580
                        screen.blit(text, (text_x, text_y))
                        font = pygame.font.Font(None, 30)
                        if b >= len("Почему какай то шарик укланяется от пуль?"):
                            part1 = False
                            part2 = True
                            time.sleep(2)
                            continue
                        a2 += "Почему какай-то шарик укланяется от пуль?"[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "Почему какай-то шарик укланяется от пуль?"[b] != " ":
                            pygame.mixer.music.load(random.choice(tap))
                        else:
                            pygame.mixer.music.load(random.choice(space))
                        pygame.mixer.music.play()
                        time.sleep(0.125)
                        b += 1
                    if part2:
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        font = pygame.font.Font(None, 35)
                        text = font.render("Загадочная личность 1:", True, (255, 255, 255))
                        text_x = 60
                        text_y = 580
                        screen.blit(text, (text_x, text_y))
                        font = pygame.font.Font(None, 30)
                        if b >= len("И почему это всё происходит под музыку?"):
                            part2 = False
                            part3 = True
                            first2 = True
                            time.sleep(2)
                            continue
                        a2 += "И почему это всё происходит под музыку?"[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "И почему это всё происходит под музыку?"[b] != " ":
                            pygame.mixer.music.load(random.choice(tap))
                        else:
                            pygame.mixer.music.load(random.choice(space))
                        pygame.mixer.music.play()
                        time.sleep(0.125)
                        b += 1
                    if part3:
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        font = pygame.font.Font(None, 35)
                        text = font.render("Загадочная личность 2:", True, (255, 255, 255))
                        text_x = 60
                        text_y = 580
                        screen.blit(text, (text_x, text_y))
                        font = pygame.font.Font(None, 30)
                        if b >= len("Я не знаю, может мы получим ответ в продолжении?"):
                            part3 = False
                            part4 = True
                            first2 = True
                            time.sleep(2)
                            continue
                        a2 += "Я не знаю, может мы получим ответ в продолжении?"[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "Я не знаю, может мы получим ответ в продолжении?"[b] != " ":
                            pygame.mixer.music.load(random.choice(tap))
                        elif b == 9:
                            pygame.mixer.music.load(random.choice(tap))
                            c = 1
                        else:
                            pygame.mixer.music.load(random.choice(space))
                        pygame.mixer.music.play()
                        time.sleep(0.125 + c)
                        c = 0
                        b += 1
                    if part4:
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(".", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(". .", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(". . .", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        if b != 0:
                            part4 = False
                            part5 = True
                            first2 = True
                            time.sleep(2)
                            continue
                        font = pygame.font.Font(None, 80)
                        text = font.render("НЕТ!!!", True, (255, 0, 0))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.mixer.music.load('Musik/keybord/boom.mp3')
                        pygame.mixer.music.play()
                        pygame.display.flip()
                        time.sleep(3)
                        b += 1
                    if part5:
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        font = pygame.font.Font(None, 35)
                        text = font.render("Oбе загадочные личности:", True, (255, 255, 255))
                        text_x = 60
                        text_y = 580
                        screen.blit(text, (text_x, text_y))
                        font = pygame.font.Font(None, 30)
                        if b >= len("Но почему?"):
                            part5 = False
                            part6 = True
                            first2 = True
                            time.sleep(2)
                            continue
                        a2 += "Но почему?"[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "Но почему?"[b] != " ":
                            pygame.mixer.music.load(random.choice(tap))
                        else:
                            pygame.mixer.music.load(random.choice(space))
                        pygame.mixer.music.play()
                        time.sleep(0.125)
                        b += 1
                    if part6:
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        font = pygame.font.Font(None, 35)
                        text = font.render("Авторы:", True, (255, 255, 255))
                        text_x = 60
                        text_y = 580
                        screen.blit(text, (text_x, text_y))
                        font = pygame.font.Font(None, 30)
                        if b >= len("Потому-что..."):
                            part6 = False
                            part7 = True
                            first2 = True
                            time.sleep(2)
                            continue
                        a2 += "Потому-что..."[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "Потому-что..."[b] != " ":
                            pygame.mixer.music.load(random.choice(tap))
                        else:
                            pygame.mixer.music.load(random.choice(space))
                        pygame.mixer.music.play()
                        time.sleep(0.125)
                        b += 1
                    if part7:
                        if first2:
                            b = 0
                            a2 = ""
                            first2 = False
                        if b != 0:
                            part7 = False
                            run2 = False
                            final = False
                            time.sleep(2)
                            continue
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(".", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(". .", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 35)
                        text = font.render(". . .", True, (255, 255, 255))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 80)
                        text = font.render("ПРОДОЛЖЕНИЯ НЕ БУДЕТ!!", True, (255, 0, 0))
                        text_x = WIDTH // 2 - text.get_width() // 2
                        text_y = HEIGHT // 2 - text.get_height() // 2
                        screen.blit(text, (text_x, text_y))
                        pygame.mixer.music.load('Musik/keybord/boom.mp3')
                        pygame.mixer.music.play()
                        pygame.display.flip()
                        time.sleep(3)
                        b += 1
                    pygame.display.flip()

            elif chaet_menu:
                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 35)
                text = font.render("Чит меню", True, (255, 255, 255))
                text_x = 60
                text_y = 60
                screen.blit(text, (text_x, text_y))
                font = pygame.font.Font(None, 35)
                text = font.render("Показать финал", True, (255, 255, 255))
                text_x = 60
                text_y = 100
                screen.blit(text, (text_x, text_y))
                font = pygame.font.Font(None, 50)
                text = font.render("выйти", True, (255, 0, 0))
                text_x = 50
                text_y = 730
                screen.blit(text, (text_x, text_y))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if tap_quit(event.pos):
                            run = False
                            continue
                        if get_final(event.pos):
                            final = True
                pygame.display.flip()
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
                    if event.type == pygame.KEYDOWN:
                        if event.key == 1105:
                            chaet_menu = True
                            # game = True
            else:
                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 30)
                text = font.render("свой трек", True, (255, 255, 255))
                text_x = 1100
                text_y = 700
                screen.blit(text, (text_x, text_y))
                sun_surf = pygame.image.load('Textur/load.png')
                sun_rect = sun_surf.get_rect()
                screen.blit(sun_surf, sun_rect)
                if I:
                    boss = Boss((map, all_sprites, bullets), "zatik.png", 1, 1, 5, all_sprites, boss_group)
                    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                    board = Board(25, 14, CELL_SIZE, map, all_sprites)
                    hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                    fr = Fracture(board, fractures)
                    main = False
                    game = True
                if secret_cod == "715":
                    boss = Boss((map, all_sprites, bullets), "oleg.png", 1, 1, 5, all_sprites, boss_group)
                    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                    board = Board(25, 14, CELL_SIZE, map, all_sprites)
                    hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                    fr = Fracture(board, fractures)
                    secret_level1 = True
                    main = False
                    game = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        fgh = get_main(event.pos)
                        if get_privat_musik(event.pos):
                            pass
                            # Кирилл, при нажатии свой трек всё идёт сюда
                        elif fgh == "лёгкий":
                            boss = Boss((map, all_sprites, bullets), "boss1.jpg", 2, 1, 5, all_sprites, boss_group)
                            player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                            board = Board(25, 14, CELL_SIZE, map, all_sprites)
                            hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                            fr = Fracture(board, fractures)
                            light = True
                            main = False
                            game = True
                        elif fgh == "средний":
                            boss = Boss((map, all_sprites, bullets), "boss2.png", 4, 3, 5, all_sprites, boss_group)
                            player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                            board = Board(25, 14, CELL_SIZE, map, all_sprites)
                            hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                            fr = Fracture(board, fractures)
                            medium = True
                            main = False
                            game = True
                        elif fgh == "тяжёлый":
                            boss = Boss((map, all_sprites, bullets), "boss3.png", 1, 1, 5, all_sprites, boss_group)
                            player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                            board = Board(25, 14, CELL_SIZE, map, all_sprites)
                            hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                            fr = Fracture(board, fractures)
                            hard = True
                            main = False
                            game = True
                        elif fgh == "ERROR":
                            sniper(event.pos)
                            print("снайперская рота ждёт тебя")
                    if event.type == pygame.KEYDOWN:
                        try:
                            if numpad[event.key] != 0:
                                pass
                        except KeyError:
                            pygame.display.flip()
                            continue
                        if len(secret_cod) > 3:
                            secret_cod = ""
                        secret_cod += numpad[event.key]
            pygame.display.flip()

        elif game:  # НАЧАЛО ИГРЫ
            events = pygame.event.get()
            if win:
                if (complite_light and complite_medium and complite_hard) or final2:
                    while run2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run2 = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pass
                        screen.fill((0, 0, 0))
                        if part1:
                            font = pygame.font.Font(None, 35)
                            text = font.render("Загадочная личность 1:", True, (255, 255, 255))
                            text_x = 60
                            text_y = 580
                            screen.blit(text, (text_x, text_y))
                            font = pygame.font.Font(None, 30)
                            if b >= len("Почему какай то шарик укланяется от пуль?"):
                                part1 = False
                                part2 = True
                                time.sleep(2)
                                continue
                            a2 += "Почему какай-то шарик укланяется от пуль?"[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "Почему какай-то шарик укланяется от пуль?"[b] != " ":
                                pygame.mixer.music.load(random.choice(tap))
                            else:
                                pygame.mixer.music.load(random.choice(space))
                            pygame.mixer.music.play()
                            time.sleep(0.125)
                            b += 1
                        if part2:
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            font = pygame.font.Font(None, 35)
                            text = font.render("Загадочная личность 1:", True, (255, 255, 255))
                            text_x = 60
                            text_y = 580
                            screen.blit(text, (text_x, text_y))
                            font = pygame.font.Font(None, 30)
                            if b >= len("И почему это всё происходит под музыку?"):
                                part2 = False
                                part3 = True
                                first2 = True
                                time.sleep(2)
                                continue
                            a2 += "И почему это всё происходит под музыку?"[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "И почему это всё происходит под музыку?"[b] != " ":
                                pygame.mixer.music.load(random.choice(tap))
                            else:
                                pygame.mixer.music.load(random.choice(space))
                            pygame.mixer.music.play()
                            time.sleep(0.125)
                            b += 1
                        if part3:
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            font = pygame.font.Font(None, 35)
                            text = font.render("Загадочная личность 2:", True, (255, 255, 255))
                            text_x = 60
                            text_y = 580
                            screen.blit(text, (text_x, text_y))
                            font = pygame.font.Font(None, 30)
                            if b >= len("Я не знаю, может мы получим ответ в продолжении?"):
                                part3 = False
                                part4 = True
                                first2 = True
                                time.sleep(2)
                                continue
                            a2 += "Я не знаю, может мы получим ответ в продолжении?"[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "Я не знаю, может мы получим ответ в продолжении?"[b] != " ":
                                pygame.mixer.music.load(random.choice(tap))
                            elif b == 9:
                                pygame.mixer.music.load(random.choice(tap))
                                c = 1
                            else:
                                pygame.mixer.music.load(random.choice(space))
                            pygame.mixer.music.play()
                            time.sleep(0.125 + c)
                            c = 0
                            b += 1
                        if part4:
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(".", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(". .", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(". . .", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            if b != 0:
                                part4 = False
                                part5 = True
                                first2 = True
                                time.sleep(2)
                                continue
                            font = pygame.font.Font(None, 80)
                            text = font.render("НЕТ!!!", True, (255, 0, 0))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.mixer.music.load('Musik/keybord/boom.mp3')
                            pygame.mixer.music.play()
                            pygame.display.flip()
                            time.sleep(3)
                            b += 1
                        if part5:
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            font = pygame.font.Font(None, 35)
                            text = font.render("Oбе загадочные личности:", True, (255, 255, 255))
                            text_x = 60
                            text_y = 580
                            screen.blit(text, (text_x, text_y))
                            font = pygame.font.Font(None, 30)
                            if b >= len("Но почему?"):
                                part5 = False
                                part6 = True
                                first2 = True
                                time.sleep(2)
                                continue
                            a2 += "Но почему?"[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "Но почему?"[b] != " ":
                                pygame.mixer.music.load(random.choice(tap))
                            else:
                                pygame.mixer.music.load(random.choice(space))
                            pygame.mixer.music.play()
                            time.sleep(0.125)
                            b += 1
                        if part6:
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            font = pygame.font.Font(None, 35)
                            text = font.render("Авторы:", True, (255, 255, 255))
                            text_x = 60
                            text_y = 580
                            screen.blit(text, (text_x, text_y))
                            font = pygame.font.Font(None, 30)
                            if b >= len("Потому-что..."):
                                part6 = False
                                part7 = True
                                first2 = True
                                time.sleep(2)
                                continue
                            a2 += "Потому-что..."[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "Потому-что..."[b] != " ":
                                pygame.mixer.music.load(random.choice(tap))
                            else:
                                pygame.mixer.music.load(random.choice(space))
                            pygame.mixer.music.play()
                            time.sleep(0.125)
                            b += 1
                        if part7:
                            if first2:
                                b = 0
                                a2 = ""
                                first2 = False
                            if b != 0:
                                part7 = False
                                run2 = False
                                final = False
                                time.sleep(2)
                                continue
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(".", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(". .", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 35)
                            text = font.render(". . .", True, (255, 255, 255))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pass
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 80)
                            text = font.render("ПРОДОЛЖЕНИЯ НЕ БУДЕТ!!", True, (255, 0, 0))
                            text_x = WIDTH // 2 - text.get_width() // 2
                            text_y = HEIGHT // 2 - text.get_height() // 2
                            screen.blit(text, (text_x, text_y))
                            pygame.mixer.music.load('Musik/keybord/boom.mp3')
                            pygame.mixer.music.play()
                            pygame.display.flip()
                            time.sleep(3)
                            b += 1
                        pygame.display.flip()
                    win = False
                    game = False
                    main = True
                    main1 = True
                    final2 = False
                    continue
                else:
                    screen.fill((0, 0, 0))
                    font = pygame.font.Font(None, 80)
                    text = font.render("Победа!!!", True, (0, 255, 0))
                    text_x = WIDTH // 2 - text.get_width() // 2
                    text_y = HEIGHT // 2 - text.get_height() // 2
                    screen.blit(text, (text_x, text_y))
                    font = pygame.font.Font(None, 35)
                    text = font.render("Показать финал", True, (255, 255, 255))
                    text_x = 60
                    text_y = 100
                    screen.blit(text, (text_x, text_y))
                    font = pygame.font.Font(None, 50)
                    text = font.render("выйти", True, (255, 0, 0))
                    text_x = 50
                    text_y = 730
                    screen.blit(text, (text_x, text_y))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if tap_quit(event.pos):
                                run = False
                                continue
                            if get_final(event.pos):
                                final2 = True
                    pygame.display.flip()
                    continue
            if I:
                # здесь должен быть бос вебка
                if first:
                    first = False
                    pygame.mixer.music.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    if first2:
                        first2 = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Musik/dead.mp3")
                        pygame.mixer.music.play()
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                run = False
                            if tap_restart(pos):
                                a = 0
                                I = False
                                is_music_start = True
                                first2 = True
                                first = True
                                life = True
                                main = True
                                for i in player_group.sprites():
                                    i.kill()
                                for i in boss_group.sprites():
                                    i.kill()
                                for i in all_sprites.sprites():
                                    i.kill()
                                for i in map.sprites():
                                    i.kill()
                                for i in bullets.sprites():
                                    i.kill()
                                for i in hotbars.sprites():
                                    i.kill()
                                for i in hotbar_elements.sprites():
                                    i.kill()
                                for i in fractures.sprites():
                                    i.kill()
                                for i in redness.sprites():
                                    i.kill()
                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            is_player_move = event
                        if event.key == 1073741911:
                            player.cheat_hp()
                try:
                    if toc > render_audio_secret2[a]:
                        hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                        a += 1
                except IndexError:
                    win = True
                    continue
                if toc > 3.35 and is_music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_secret2)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    is_music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(is_player_move, *events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=False)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                elif is_player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                hotbar_elements.update()
                fractures.update()
                redness.update()
                boss.update()
                player.render()

                screen.fill((0, 0, 0))
                hotbars.draw(screen)
                fractures.draw(screen)
                screen.blit(secret_screen, (0, 0))

                map.draw(screen)
                boss_group.draw(screen)
                hotbar_elements.draw(screen)
                bullets.draw(screen)
                player_group.draw(screen)
                redness.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text123)
                    text_restart = random.choice(restart_text)
                    life = False
            elif secret_level1:
                if first:
                    first = False
                    pygame.mixer.music.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    if first2:
                        first2 = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Musik/dead.mp3")
                        pygame.mixer.music.play()
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                run = False
                            if tap_restart(pos):
                                a = 0
                                secret_level1 = False
                                is_music_start = True
                                first2 = True
                                first = True
                                life = True
                                main = True
                                for i in player_group.sprites():
                                    i.kill()
                                for i in boss_group.sprites():
                                    i.kill()
                                for i in all_sprites.sprites():
                                    i.kill()
                                for i in map.sprites():
                                    i.kill()
                                for i in bullets.sprites():
                                    i.kill()
                                for i in hotbars.sprites():
                                    i.kill()
                                for i in hotbar_elements.sprites():
                                    i.kill()
                                for i in fractures.sprites():
                                    i.kill()
                                for i in redness.sprites():
                                    i.kill()
                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            is_player_move = event
                        if event.key == 1073741911:
                            player.cheat_hp()
                try:
                    if toc > render_audio_secret1[a]:
                        hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                        a += 1
                except IndexError:
                    win = True
                    continue
                if toc > 3.35 and is_music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_secret1)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    is_music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(is_player_move, *events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=False)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                elif is_player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                hotbar_elements.update()
                fractures.update()
                redness.update()
                boss.update()
                player.render()

                screen.fill((0, 0, 0))
                hotbars.draw(screen)
                fractures.draw(screen)
                screen.blit(secret_screen, (0, 0))

                map.draw(screen)
                boss_group.draw(screen)
                hotbar_elements.draw(screen)
                bullets.draw(screen)
                player_group.draw(screen)
                redness.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text123)
                    text_restart = random.choice(restart_text)
                    life = False
            elif light:
                if first:
                    first = False
                    pygame.mixer.music.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    if first2:
                        first2 = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Musik/dead.mp3")
                        pygame.mixer.music.play()
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                run = False
                            if tap_restart(pos):
                                a = 0
                                light = False
                                is_music_start = True
                                first2 = True
                                first = True
                                life = True
                                main = True
                                for i in player_group.sprites():
                                    i.kill()
                                for i in boss_group.sprites():
                                    i.kill()
                                for i in all_sprites.sprites():
                                    i.kill()
                                for i in map.sprites():
                                    i.kill()
                                for i in bullets.sprites():
                                    i.kill()
                                for i in hotbars.sprites():
                                    i.kill()
                                for i in hotbar_elements.sprites():
                                    i.kill()
                                for i in fractures.sprites():
                                    i.kill()
                                for i in redness.sprites():
                                    i.kill()

                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            is_player_move = event
                        if event.key == 1073741911:
                            player.cheat_hp()
                try:
                    if toc > render_audio_Sacrifice[a]:
                        hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                        a += 1
                except IndexError:
                    win = True
                    continue
                if toc > 3.35 and is_music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_Sacrifice)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    is_music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(is_player_move, *events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=False)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                elif is_player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                hotbar_elements.update()
                fractures.update()
                redness.update()
                boss.update()
                player.render()

                screen.fill((0, 0, 0))
                hotbars.draw(screen)
                fractures.draw(screen)
                screen.blit(secret_screen, (0, 0))

                map.draw(screen)
                boss_group.draw(screen)
                hotbar_elements.draw(screen)
                bullets.draw(screen)
                player_group.draw(screen)
                redness.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text123)
                    text_restart = random.choice(restart_text)
                    life = False
            elif medium:
                if first:
                    first = False
                    pygame.mixer.music.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    if first2:
                        first2 = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Musik/dead.mp3")
                        pygame.mixer.music.play()
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                run = False
                            if tap_restart(pos):
                                a = 0
                                medium = False
                                is_music_start = True
                                first2 = True
                                first = True
                                life = True
                                main = True
                                for i in player_group.sprites():
                                    i.kill()
                                for i in boss_group.sprites():
                                    i.kill()
                                for i in all_sprites.sprites():
                                    i.kill()
                                for i in map.sprites():
                                    i.kill()
                                for i in bullets.sprites():
                                    i.kill()
                                for i in hotbars.sprites():
                                    i.kill()
                                for i in hotbar_elements.sprites():
                                    i.kill()
                                for i in fractures.sprites():
                                    i.kill()
                                for i in redness.sprites():
                                    i.kill()
                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            is_player_move = event
                        if event.key == 1073741911:
                            player.cheat_hp()
                try:
                    if toc > render_audio_The_Forever_Mine[a]:
                        hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                        a += 1
                except IndexError:
                    win = True
                    continue
                if toc > 3.35 and is_music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_Forever_Mine)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    is_music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(is_player_move, *events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=False)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                elif is_player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                hotbar_elements.update()
                fractures.update()
                redness.update()
                boss.update()
                player.render()

                screen.fill((0, 0, 0))
                hotbars.draw(screen)
                fractures.draw(screen)
                screen.blit(secret_screen, (0, 0))

                map.draw(screen)
                boss_group.draw(screen)
                hotbar_elements.draw(screen)
                bullets.draw(screen)
                player_group.draw(screen)
                redness.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text123)
                    text_restart = random.choice(restart_text)
                    life = False
            elif hard:
                if first:
                    first = False
                    pygame.mixer.music.stop()
                    tic = time.perf_counter()  # Время до начала игры
                toc = time.perf_counter() - tic
                if not life:
                    if first2:
                        first2 = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Musik/dead.mp3")
                        pygame.mixer.music.play()
                    for event in events:
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            if tap_quit(pos):
                                run = False
                            if tap_restart(pos):
                                a = 0
                                hard = False
                                is_music_start = True
                                first2 = True
                                first = True
                                life = True
                                main = True
                                for i in player_group.sprites():
                                    i.kill()
                                for i in boss_group.sprites():
                                    i.kill()
                                for i in all_sprites.sprites():
                                    i.kill()
                                for i in map.sprites():
                                    i.kill()
                                for i in bullets.sprites():
                                    i.kill()
                                for i in hotbars.sprites():
                                    i.kill()
                                for i in hotbar_elements.sprites():
                                    i.kill()
                                for i in fractures.sprites():
                                    i.kill()
                                for i in redness.sprites():
                                    i.kill()
                    game_over(text_over, text_restart)
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                            is_player_move = event
                        if event.key == 1073741911:
                            player.cheat_hp()
                try:
                    if toc > render_audio_The_Jounrey_Home[a]:
                        hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                        a += 1
                except IndexError:
                    win = True
                    continue
                if toc > 3.35 and is_music_start:  # Музыка начинается после 3.31 секунды
                    # (время прохождения элементом хотбара)
                    pygame.mixer.music.load(audio_data_The_Jounrey_Home)
                    time.sleep(0.1)
                    pygame.mixer.music.play()
                    is_music_start = False
                for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                    i.change_condition()

                if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                    # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                    pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, True)
                    all_sprites.update(is_player_move, *events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=False)
                elif [i for i in hotbar_elements.sprites() if not (
                        i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                         False)) and i.get_condition()]:
                    # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                    for i in hotbar_elements.sprites():
                        if i.get_condition():
                            i.kill()
                    all_sprites.update(*events)
                    boss.attack()
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                elif is_player_move:
                    # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                    player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets,
                                     early_or_latter_input=True)
                hotbar_elements.update()
                fractures.update()
                redness.update()
                boss.update()
                player.render()

                screen.fill((0, 0, 0))
                hotbars.draw(screen)
                fractures.draw(screen)
                screen.blit(secret_screen, (0, 0))

                map.draw(screen)
                boss_group.draw(screen)
                hotbar_elements.draw(screen)
                bullets.draw(screen)
                player_group.draw(screen)
                redness.draw(screen)

                if player.get_hp() < 1:
                    text_over = random.choice(text123)
                    text_restart = random.choice(restart_text)
                    life = False

            pygame.display.flip()
            clock.tick(FPS)
            is_player_move = False
