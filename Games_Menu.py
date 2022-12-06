import time

import pygame


def get_click(screen, pos):
    if 1200 > pos[0] > 1000 and 600 > pos[1] > 500:
        print("Игра началась")


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


pygame.init()
size = width, height = 1280, 640
screen = pygame.display.set_mode(size)
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
color = 0
audio_data = 'Musik/main.wav'
pygame.mixer.music.load(audio_data)
pygame.mixer.music.play(-1)
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
                    get_click(screen, event.pos)
            pygame.display.flip()

    elif game:
        pass
        # сдесь пишем игру
