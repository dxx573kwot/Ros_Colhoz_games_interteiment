import time

import pygame


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
color = 0
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
                    cutschen = False
                    continue
                draw_news(screen, color)
                color += 1
                time.sleep(0.01)
                pygame.display.flip()
        else:
            print("катсцена окончена")
            screen.fill((0, 0, 0))
            pygame.display.flip()
            run = False
    elif game:
        pass
        # сдесь пишем игру
