import sys
import time
import librosa.display
import pygame
from multiprocessing import Process, Queue, Pipe
import threading
import queue
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication
import random
import matplotlib
import pyautogui
import keyboard
import os
import shutil
import sqlite3
from Hotbar import Hotbar
from Map import Board
from Player import Player
from Boss import Boss
from Fracture import Fracture
from Uncommon_boss import UncommonBoss
from loadimage import load_image


class GetAudio(QWidget):
    def __init__(self):
        super().__init__()
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать музыку', '', 'Музыка (*.wav)')[0]


class Musik_render(Process):
    def __init__(self, q, audio_data, bits_in_minute):
        Process.__init__(self)
        self.q = q
        self.bits_in_minute = bits_in_minute
        self.audio_data = audio_data

    def run(self):
        bits_in_minute = self.bits_in_minute
        y, sr = librosa.load(self.audio_data)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        if bits_in_minute != -1:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                         trim=True)
        else:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)
        self.q.put([beat_frames, True])


class Musik_render2(Process):
    def __init__(self, q, audio_data, bits_in_minute, conn):
        Process.__init__(self)
        self.q = q
        self.con = conn
        self.bits_in_minute = bits_in_minute
        self.audio_data = audio_data
        self.work = True

    def run(self):
        self.con.send([True])
        bits_in_minute = self.bits_in_minute
        y, sr = librosa.load(self.audio_data)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        if bits_in_minute != -1:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                         trim=True)
        else:
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)
        self.work = False
        self.q.put([beat_frames, True])
        self.con.send([False])
        self.con.close()


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
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
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
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    q.put([beat_frames, True])


def musik_render_The_Jounrey_Home(audio_data, q):
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
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


def take_name(keybrd, tap, fullscreen):
    SIZE = WIDTH, HEIGHT = 1250, 800
    if fullscreen:
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    else:
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


def all_sprites_kill():
    for group in (
            player_group, boss_group, all_sprites, map, bullets, hotbars, hotbar_elements, fractures, redness, rockets):
        for sprite in group.sprites():
            sprite.kill()


def get_add_result(pos):
    if 1196 > pos[0] > 847 and 760 > pos[1] > 728:
        return True
    return False


def get_tabl_lider(pos):
    if 277 > pos[0] > 93 and 719 > pos[1] > 695:
        return True
    return False


def renred_musik(qe):
    bits_in_minute = -1
    y, sr = librosa.load('Musik/custom_music.wav')
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    if bits_in_minute != -1:
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                     trim=True)
    else:
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)
    '''
    bits_in_minute = -1
    y, sr = librosa.load('Musik/custom_music.wav')
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    if bits_in_minute != -1:
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                     trim=True)
    else:
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)'''
    qe.put_nowait([beat_frames])


def registrate_user(player_name):
    con = sqlite3.connect("base_score.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT name_user FROM score WHERE name_user = '{player_name}'""").fetchall()
    flag = True
    for i in result:
        if player_name in i:
            flag = False
    if flag:
        cur.execute(
            f"""INSERT INTO level_score(name_user, level_1, level_2, level_3) VALUES ('{player_name}', 1, 1, 1)""")
        cur.execute(f"""INSERT INTO score(name_user, score) VALUES ('{player_name}', 3)""")
        con.commit()


def gift_score(player_name, mush):
    con = sqlite3.connect("base_score.db")
    cur = con.cursor()
    score = 10 * player.get_hp() + a * 50
    if mush == 3:
        star_score = cur.execute(f"""SELECT level_1 FROM level_score WHERE name_user = '{player_name}'""").fetchall()
        #print(star_score, score)
        if int(star_score[0][0]) < score:
            cur.execute(f"""UPDATE level_score SET level_1 = {score} WHERE name_user = '{player_name}'""")
            con.commit()
    elif mush == 7:
        score *= 1.5
        star_score = cur.execute(f"""SELECT level_2 FROM level_score WHERE name_user = '{player_name}'""").fetchall()
        if int(star_score[0][0]) < score:
            cur.execute(f"""UPDATE level_score SET level_2 = {score} WHERE name_user = '{player_name}'""")
            con.commit()
    elif mush == 10:
        score *= 3
        star_score = cur.execute(f"""SELECT level_3 FROM level_score WHERE name_user = '{player_name}'""").fetchall()
        if int(star_score[0][0]) < score:
            cur.execute(f"""UPDATE level_score SET level_3 = {score} WHERE name_user = '{player_name}'""")
            con.commit()

    score = cur.execute(f"""SELECT level_1, level_2, level_3 FROM level_score WHERE
        name_user = '{player_name}'""").fetchall()
    oll_score = 0
    for i in score:
        oll_score += sum(i)

    cur.execute(f"""UPDATE score SET score = {oll_score} WHERE name_user = '{player_name}'""")
    con.commit()


if __name__ == '__main__':
    pygame.init()

    screenshot("Textur/cv/screenshot.png")

    #print(matplotlib.get_data_path())
    #print(os.cpu_count())

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
    my_level = False
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
    status = False
    tabl_lider = True
    tabl_lider2 = False
    text123 = ["Игра отстой!", "Садись, два по киберспорту!", "Не бей пожалуйста :)", "ERROR: Oleg 715",
               "alt+f4"]  # любой текст окончания игры
    restart_text = ["пострадать ещё раз!", "хочу ещё!", "не опять, а снова!", "всеравно проиграешь", "alt+ctrl+delete"]
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
    all_render_music = {}
    for i in os.listdir("render_music"):
        with open(f"render_music/{i}", mode="r", encoding="UTF-8") as f:
            all_render_music[i.split(".")[0]] = list(map(float, f.read().split()))
    #print(all_render_music.keys())

    audio_data_main = 'Musik/main.wav'
    audio_data_The_Jounrey_Home = 'Musik/The_Jounrey_Home.wav'  # Musik/test.wav Musik/The_Jounrey_Home.wav Musik/Sacrifice.wav
    audio_data_Forever_Mine = 'Musik/Forever_Mine.wav'
    # audio_data_Sacrifice = 'Musik/test.wav'
    audio_data_secret1 = 'Musik/Riverside.wav'
    audio_data_secret2 = 'Musik/I.wav'
    audio_data_my_level = 'Musik/custom_music.wav'
    audio_data_Sacrifice = 'Musik/Sacrifice.wav'
    rady1, rady2, rady3 = True, True, True
    '''
    if I:
        q1 = Queue()
        p = Musik_render(q1, audio_data_secret2, -1)
        p.start()
        a1 = q1.get()
        render_audio_secret2 = a1[0]
        rady1 = a1[1]
        rady2 = a1[1]
        rady3 = a1[1]
    elif os.cpu_count() <= 4:
        q1 = Queue()
        q2 = Queue()
        q3 = Queue()
        p = Musik_render(q1, audio_data_The_Jounrey_Home, 60)  # 60
        p2 = Musik_render(q2, audio_data_Forever_Mine, 90)  # 90
        p3 = Musik_render(q3, audio_data_Sacrifice, 120)  # 120
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
        q3 = Queue()
        p = Musik_render(q1, audio_data_secret1, -1)
        p3 = Musik_render(q3, audio_data_my_level, -1)
        p.start()
        p2.start()
        p3.start()
        a1 = q1.get()
        a3 = q3.get()
        render_audio_secret1 = a1[0]
        render_audio_my_level = a3[0]
    else:
        q1 = Queue()
        q2 = Queue()
        q3 = Queue()
        q4 = Queue()
        q6 = Queue()
        p = Musik_render(q1, audio_data_The_Jounrey_Home, 60)  # 60
        p2 = Musik_render(q2, audio_data_Forever_Mine, 90)  # 90
        p3 = Musik_render(q3, audio_data_Sacrifice, 120)  # 120
        p4 = Musik_render(q4, audio_data_secret1, -1)
        p6 = Musik_render(q6, audio_data_my_level, -1)
        p.start()
        p2.start()
        p3.start()
        p4.start()
        p6.start()
        a1 = q1.get()
        a2 = q2.get()
        a3 = q3.get()
        a4 = q4.get()
        a6 = q6.get()
        render_audio_Sacrifice = a1[0]
        render_audio_The_Forever_Mine = a2[0]
        render_audio_The_Jounrey_Home = a3[0]
        render_audio_secret1 = a4[0]
        render_audio_my_level = a6[0]
        rady1 = a1[1]
        rady2 = a2[1]
        rady3 = a3[1]
    with open(f"render_music/{audio_data_Sacrifice.split('/')[-1].split(',')[0]}.txt", encoding="UTF-8", mode="w") as f:
        for i in render_audio_data_Sacrifice:
            f.wirte(str(i) + " ")
    '''
    #print(rady1)
    a2 = ""
    keybrd = {113: 'q', 119: 'w', 101: 'e', 114: 'r', 116: 't', 121: 'y', 117: 'u', 105: 'i', 111: 'o', 112: 'p',
              97: 'a', 115: 's', 100: 'd', 102: 'f', 103: 'g', 104: 'h', 106: 'j', 107: 'k', 108: 'l', 122: 'z',
              120: 'x', 99: 'c', 118: 'v', 98: 'b', 110: 'n', 109: 'm', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5',
              54: '6', 55: '7', 56: '8', 57: '9', 48: "0", 8: "dell", 13: "continue"}
    numpad = {49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 48: '0'}
    secret_cod = ""
    fullscreen = fullscren_dialog()
    #print(rady1, rady2, rady3)
    #print("время запуска составило " + str(time.process_time()))

    player_name = take_name(keybrd, tap, fullscreen)
    registrate_user(player_name)
    #print("Привет " + player_name)

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
    rockets = pygame.sprite.Group()
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
                        if b >= len("Почему какай то шарик уклоняется от пуль?"):
                            part1 = False
                            part2 = True
                            time.sleep(2)
                            continue
                        a2 += "Почему какай-то шарик уклоняется от пуль?"[b]
                        text = font.render(a2, True, (255, 255, 255))
                        text_x = 60
                        text_y = 625
                        screen.blit(text, (text_x, text_y))
                        if "Почему какай-то шарик уклоняется от пуль?"[b] != " ":
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
                font = pygame.font.Font(None, 30)
                text = font.render("лидер", True, (255, 255, 255))
                text_x = 100
                text_y = 700
                screen.blit(text, (text_x, text_y))
                sun_surf = pygame.image.load('Textur/load.png')
                sun_rect = sun_surf.get_rect()
                screen.blit(sun_surf, sun_rect)
                settings_boss = False
                fgh = False
                if tabl_lider2:
                    font = pygame.font.Font(None, 30)
                    con = sqlite3.connect('base_score.db')
                    cur = con.cursor()
                    lider = cur.execute("""SELECT * FROM score""").fetchall()
                    index = 0
                    score = 0
                    for x, i in enumerate(lider):
                        if i[1] > score:
                            index = x
                            score = i[1]
                    text = font.render(f"Лидер по очкам: {lider[index][0]} - {lider[index][1]}", True, (255, 255, 255))
                    text_x = 640
                    text_y = 700
                    screen.blit(text, (text_x, text_y))
                if I:
                    tabl_lider2 = False
                    settings_boss = ("special", 1, 1, 8)
                    texture_pack = "classic_pack"
                    music_play_now = audio_data_secret2
                    music_render_now = all_render_music["I"]
                if secret_cod == "715":
                    tabl_lider2 = False
                    settings_boss = ("oleg.png", 10, 5, 8)
                    texture_pack = "special_pack_1"
                    music_play_now = audio_data_secret1
                    music_render_now = all_render_music["Riverside"]
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        fgh = get_main(event.pos)
                        if get_privat_musik(event.pos):
                            if not ("custom_music" in all_render_music.keys()):
                                tabl_lider2 = False
                                app = QApplication(sys.argv)
                                ex = GetAudio()
                                fname = ex.fname
                                ex.close()
                                shutil.copy(fname, 'Musik/custom_music.wav')
                                qe = queue.Queue()
                                p = threading.Thread(target=renred_musik, args=[qe])
                                p.start()
                                while p.is_alive():
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            run = False
                                    loading(screen, roteit)
                                    roteit += 1
                                    pygame.display.flip()
                                vfgnxnxgfjx = qe.get()[0]
                                all_render_music["custom_music"] = vfgnxnxgfjx
                            settings_boss = ("custom_music.png", 2, 2, 4)
                            texture_pack = "classic_pack"
                            music_play_now = audio_data_my_level
                            music_render_now = all_render_music["custom_music"]
                            # Кирилл, при нажатии свой трек всё идёт сюда
                        elif get_tabl_lider(event.pos):
                            tabl_lider2 = True
                            font = pygame.font.Font(None, 30)
                            con = sqlite3.connect('base_score.db')
                            cur = con.cursor()
                            lider = cur.execute("""SELECT * FROM score""").fetchmany(1)
                            text = font.render(f"{lider[0][0]} - {lider[0][1]}", True, (255, 255, 255))
                            text_x = 640
                            text_y = 700
                            screen.blit(text, (text_x, text_y))
                            pygame.display.flip()
                            continue
                        elif fgh == "лёгкий":
                            diffff = 3
                            tabl_lider2 = False
                            settings_boss = ("boss1.png", 4, 2, 3)
                            texture_pack = "classic_pack"
                            music_play_now = audio_data_The_Jounrey_Home
                            music_render_now = all_render_music["Sacrifice"]
                        elif fgh == "средний":
                            diffff = 7
                            tabl_lider2 = False
                            settings_boss = ("boss2.png", 5, 2, 7)
                            texture_pack = "classic_pack"
                            music_play_now = audio_data_Forever_Mine
                            music_render_now = all_render_music["Forever_Mine"]
                        elif fgh == "тяжёлый":
                            diffff = 10
                            tabl_lider2 = False
                            settings_boss = ("boss3.png", 4, 3, 10)
                            texture_pack = "classic_pack"
                            music_play_now = audio_data_Sacrifice
                            music_render_now = all_render_music["The_Jounrey_Home"]
                        elif fgh == "ERROR":
                            sniper(event.pos)
                            #print("снайперская рота ждёт тебя")
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
                if settings_boss:
                    if settings_boss[0] == "special":
                        boss = UncommonBoss(5, all_sprites, boss_group)
                    else:
                        boss = Boss(*settings_boss, all_sprites, boss_group)
                    player = Player(3, 3, CELL_SIZE, (map, boss), all_sprites, player_group)
                    board = Board(texture_pack, 25, 14, CELL_SIZE, all_sprites, map)
                    hotbar = Hotbar((hotbar_elements,), (all_sprites, hotbars), all_sprites, hotbars)
                    fr = Fracture(board, fractures)
                    main = False
                    game = True
            pygame.display.flip()
        elif game:  # НАЧАЛО ИГРЫ
            events = pygame.event.get()
            if win:
                gift_score(player_name, diffff)
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
                            if b >= len("Почему какой то шарик уклоняется от пуль?"):
                                part1 = False
                                part2 = True
                                time.sleep(2)
                                continue
                            a2 += "Почему какой-то шарик уклоняется от пуль?"[b]
                            text = font.render(a2, True, (255, 255, 255))
                            text_x = 60
                            text_y = 625
                            screen.blit(text, (text_x, text_y))
                            if "Почему какой-то шарик уклоняется от пуль?"[b] != " ":
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
                    font = pygame.font.Font(None, 50)
                    text = font.render("добавить результат", True, (0, 255, 0))
                    text_x = 850
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
                            if get_add_result(event.pos):
                                pass
                    pygame.display.flip()
                    continue
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
                    if event.type == pygame.QUIT or settings_boss[0] == "special":
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
                            secret_cod = ""
                            all_sprites_kill()
                game_over(text_over, text_restart)
                pygame.display.flip()
                clock.tick(FPS)
                continue
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                    pygame.mixer.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT):
                        is_player_move = event
                    if event.key == 1073741911:
                        player.cheat_hp()
            try:
                if toc > music_render_now[a]:
                    hotbar.create_hotbar_element()  # Создание элементов в хотбаре
                    a += 1
            except IndexError:
                win = True
                continue
            if toc > 3.35 and is_music_start:  # Музыка начинается после 3.35 секунды
                # (время прохождения элементом хотбара)
                pygame.mixer.music.load(music_play_now)
                time.sleep(0.1)
                pygame.mixer.music.play()
                is_music_start = False
            for i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False):
                i.change_condition()
            if pygame.sprite.spritecollideany(hotbar.get_heart(), hotbar_elements) and is_player_move:
                # Ход делается, если элемент достиг сердца, игрок сделал шаг и элемент ещё находится внутри сердца.
                pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements, False)[0].kill()
                all_sprites.update(is_player_move, *events)
                rockets.update()
                boss.attack((map, all_sprites, bullets), (player, rockets))
                player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets, rockets=rockets,
                                 early_or_latter_input=False)
            elif [i for i in hotbar_elements.sprites() if not (
                    i in pygame.sprite.spritecollide(hotbar.get_heart(), hotbar_elements,
                                                     False)) and i.get_condition()]:
                # Ход делается, если элемент пересёк сердце, но при этом игрок не сделал шаг.
                hotbar_elements.sprites()[0].kill()
                all_sprites.update(*events)
                rockets.update()
                boss.attack((map, all_sprites, bullets), (player, rockets))
                player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets, rockets=rockets,
                                 early_or_latter_input=True)
            elif is_player_move:
                # Если игрок попытался сделать шаг, но при этом элемент не достиг сердца.
                player.change_hp(fracture=fr, redness_groups=redness, bullets=bullets, rockets=rockets,
                                 early_or_latter_input=True)

            hotbar_elements.update()
            fractures.update()
            redness.update()
            boss.update()
            player.render()
            for i in rockets.sprites():
                i.explosion()
            player.change_hp(fracture=fr, rockets=rockets, move_check=False)
            # Отдельная проверка, если взрыв ракеты произошёл около персонажа

            screen.fill((0, 0, 0))
            hotbars.draw(screen)
            fractures.draw(screen)
            screen.blit(secret_screen, (0, 0))
            map.draw(screen)
            boss_group.draw(screen)
            hotbar_elements.draw(screen)
            bullets.draw(screen)
            player_group.draw(screen)
            rockets.draw(screen)
            redness.draw(screen)

            if player.get_hp() < 1:
                gift_score(player_name, diffff)
                text_over = random.choice(text123)
                text_restart = random.choice(restart_text)
                life = False

            pygame.display.flip()
            clock.tick(FPS)
            is_player_move = False
