import pygame
import random


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


pygame.init()
fullscreen = False
run = True
text = ["Игра отстой!", "Садись, два по киберспорту!", "Не бей пожалуйста :)"]  # любой текст окончания игры
restart_text = ["пострадать ещё раз!", "хочу ещё!"]
text_over = random.choice(text)
text_restart = random.choice(restart_text)
SIZE = WIDTH, HEIGHT = 1250, 800
screen = pygame.display.set_mode(SIZE)
if fullscreen:
    screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(SIZE)
while run:
    for event in pygame.event.get():
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
