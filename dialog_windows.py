import pygame


def da(pos):
    if 83 > pos[0] > 42 and 267 > pos[1] > 245:
        return True
    return False


def net(pos):
    if 349 > pos[0] > 311 and 267 > pos[1] > 245:
        return True
    return False


pygame.init()
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
                print(0)
            if net(pos):
                print(1)
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
