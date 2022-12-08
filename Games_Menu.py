import time
import librosa.display
import numpy as np
import pygame
import random


def get_click(pos):
    if 1200 > pos[0] > 1000 and 600 > pos[1] > 500:
        return True
    else:
        return False


def draw_titri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("модные титры", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_titri_v_nachale_igri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("модные титры", True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("в начале игры", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2 + 50
    text_y = height // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_creator_oleg(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("от создателя олега", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_news(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("от создателя олега", True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("чёт давно никаких новостей", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2 + 50
    text_y = height // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_balli(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("более 90 баллов", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_drugie_igri(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("более 90 баллов", True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("есть у других проектов", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2 + 50
    text_y = height // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_rehizer(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("режисёр", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_ne_nuhen(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("режисёр", True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("здесь вообще не нужен", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2 + 50
    text_y = height // 2 - text.get_height() // 2 + 50
    screen.blit(text, (text_x, text_y))


def draw_name(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Round and bits", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def draw_creator(screen, color):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Round and bits", True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    text = font.render("от Ros Colhoz Games intertaimont", True, (color, color, color))
    text_x = width // 2 - text.get_width() // 2 + 50
    text_y = height // 2 - text.get_height() // 2 + 50
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


def test_level(beat_frames):
    global rady
    audio_data = 'Musik/Sacrifice.wav'
    pygame.mixer.music.load(audio_data)
    tr, tic, toc = 0, 0, 0
    bits_in_minute = 60.0
    er = 1
    y, sr = librosa.load(audio_data)
    print(type(y), type(sr))
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print('Detected Tempo: ' + str(tempo) + ' beats/min')
    pygame.mixer.music.play()
    rady = True
    for i in beat_frames:
        # print(i, "секунда")
        time.sleep(i - tr - (toc - tic))
        tic = time.perf_counter()
        # основной код начинается
        render()
        print(1)
        pygame.display.flip()
        # основной код заканчивается
        toc = time.perf_counter()


def render():
    global hit_map, point_map, hero_texture, wall_texture
    screen.fill((0, 0, 0))
    for w, y in enumerate(hit_map):
        for r, x in enumerate(y):
            if "H" in x:
                try:
                    dog_surf = pygame.image.load(
                        random.choice(wall_texture)).convert()
                    rot_rect = dog_surf.get_rect(
                        center=point_map[w][r])
                    screen.blit(dog_surf, rot_rect)
                    dog_surf = pygame.image.load(
                        random.choice(hero_texture))
                    rot_rect = dog_surf.get_rect(
                        bottomright=point_map[w][r])
                    screen.blit(dog_surf, rot_rect)
                except IndexError:
                    continue
            if "s" in x:
                try:
                    dog_surf = pygame.image.load(
                        random.choice(wall_texture)).convert()
                    rot_rect = dog_surf.get_rect(
                        center=point_map[w][r])
                    screen.blit(dog_surf, rot_rect)
                except IndexError:
                    continue


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


pygame.init()
clock = pygame.time.Clock()
run = True
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
wall_texture = ["Textur/CUMmen.jpg"]
hero_texture = ["Textur/hero1.png", "Textur/hero2.png", "Textur/hero3.png"]
color = 0
roteit = 0
audio_data_main = 'Musik/main.wav'
audio_data_Sacrifice = 'Musik/Sacrifice.wav'
render_audio_Sacrifice = musik_render(audio_data_Sacrifice)
audio_data_Forever_Mine = 'Musik/Forever_Mine.wav'
render_audio_Forever_Mine = musik_render(audio_data_Forever_Mine)
audio_data_The_Jounrey_Home = 'Musik/The_Jounrey_Home.wav'
render_audio_Jounrey_Home = musik_render(audio_data_The_Jounrey_Home)
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
size = width, height = 1280, 640
fullscreen = False
if fullscreen:
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)
while run:
    if main:
        if cutschen:
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
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
                pygame.display.flip()
        else:
            # меню
            sun_surf = pygame.image.load('Textur/main.jpg')
            sun_rect = sun_surf.get_rect()
            screen.blit(sun_surf, sun_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if get_click(event.pos):
                        main = False
                        game = True
            pygame.display.flip()

    elif game:
        test_level()
        pygame.display.flip()
