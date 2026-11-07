import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 500
W_HAND = 200
H_HAND = 50

# цвета выбраны с сайта: https://htmlcolorcodes.com/
PURPLE = (209, 156, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (232, 157, 28)
BLUE = (45, 227, 227)
KOJA = (255, 232, 150)
GREEN = (105, 252, 86)
YELLOW = (255, 255, 0)
GRAY = (135, 127, 127)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLUE)  # заливка фона
pg.display.set_caption("Игра")
Artem = pg.time.Clock()

pg.draw.rect(screen, GREEN, (0, HEIGHT / 2, WIDTH, HEIGHT / 2))
pg.draw.polygon(screen, GRAY, [[WIDTH * 2 / 3, HEIGHT / 2 + 20],
                               [WIDTH * 9 / 10, HEIGHT / 2 + 20],
                               [((WIDTH * 2 / 3) + (WIDTH * 9 / 10)) / 2, HEIGHT * 1 / 7]])

pg.draw.circle(screen, PURPLE, (WIDTH / 2, HEIGHT / 2), 100)
pg.draw.circle(screen, KOJA, (WIDTH / 2, 110), 40)
pg.draw.rect(screen, KOJA, (250, 150, W_HAND, H_HAND))
pg.draw.rect(screen, KOJA, (550, 150, W_HAND, H_HAND))
pg.draw.line(screen, BLACK, [WIDTH / 2 - 50, 340], [HEIGHT / 2 - 50, 450], 10)
pg.draw.line(screen, BLACK, [WIDTH / 2 + 50, 340], [HEIGHT / 2 + 50, 450], 10)
pg.draw.ellipse(screen, ORANGE, (425, 190, 150, 75))
pg.draw.circle(screen, YELLOW, (100, 100), 50)


# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    Artem.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
