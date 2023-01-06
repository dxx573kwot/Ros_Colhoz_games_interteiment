import time
import random

import pygame

pygame.init()
run = True
first = True
part1 = True
part2 = False
part3 = False
part4 = False
part5 = False
part6 = False
part7 = False
a = ""
b = 0
c = 0
SIZE = WIDTH, HEIGHT = 1250, 800
tap = ['Musik/keybord/tap1.wav', 'Musik/keybord/tap2.wav', 'Musik/keybord/tap3.wav', 'Musik/keybord/tap4.wav']
space = ['Musik/keybord/space.wav', 'Musik/keybord/space2.wav']
screen = pygame.display.set_mode(SIZE)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
        a += "Почему какай-то шарик укланяется от пуль?"[b]
        text = font.render(a, True, (255, 255, 255))
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
        if first:
            b = 0
            a = ""
            first = False
        font = pygame.font.Font(None, 35)
        text = font.render("Загадочная личность 1:", True, (255, 255, 255))
        text_x = 60
        text_y = 580
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        if b >= len("И почему это всё происходит под музыку?"):
            part2 = False
            part3 = True
            first = True
            time.sleep(2)
            continue
        a += "И почему это всё происходит под музыку?"[b]
        text = font.render(a, True, (255, 255, 255))
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
        if first:
            b = 0
            a = ""
            first = False
        font = pygame.font.Font(None, 35)
        text = font.render("Загадочная личность 2:", True, (255, 255, 255))
        text_x = 60
        text_y = 580
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        if b >= len("Я не знаю, может мы получим ответ в продолжении?"):
            part3 = False
            part4 = True
            first = True
            time.sleep(2)
            continue
        a += "Я не знаю, может мы получим ответ в продолжении?"[b]
        text = font.render(a, True, (255, 255, 255))
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
        if first:
            b = 0
            a = ""
            first = False
        if b != 0:
            part4 = False
            part5 = True
            first = True
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
        if first:
            b = 0
            a = ""
            first = False
        font = pygame.font.Font(None, 35)
        text = font.render("Oбе загадочные личности:", True, (255, 255, 255))
        text_x = 60
        text_y = 580
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        if b >= len("Но почему?"):
            part5 = False
            part6 = True
            first = True
            time.sleep(2)
            continue
        a += "Но почему?"[b]
        text = font.render(a, True, (255, 255, 255))
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
        if first:
            b = 0
            a = ""
            first = False
        font = pygame.font.Font(None, 35)
        text = font.render("Автор:", True, (255, 255, 255))
        text_x = 60
        text_y = 580
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 30)
        if b >= len("Потому-что..."):
            part6 = False
            part7 = True
            first = True
            time.sleep(2)
            continue
        a += "Потому-что..."[b]
        text = font.render(a, True, (255, 255, 255))
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
        if first:
            b = 0
            a = ""
            first = False
        if b != 0:
            part7 = False
            first = True
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
