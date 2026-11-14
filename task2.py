import pygame as pg

FPS = 67
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (221, 255, 0)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

spid = 2
a = 50
x = 0
y = WIN_HEIGHT // 4
pg.draw.rect(screen, ORANGE, (x, y, a, a))

pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    if abs(spid) <= 100:
        if x >= WIN_WIDTH - a:  # коснулись правой стенки
            spid = spid * -3 // 2
        if x <= 0:  # коснулись левой стенки
            spid = spid * -3 // 2
    else:
        if spid < -100:
            spid = -100
        elif spid > 100:
            spid = 100
    x += spid

    screen.fill(WHITE)
    pg.draw.rect(screen, ORANGE, (x, y, a, a))

    pg.display.update()
