import random
import pygame as pg

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# Параметры круга
x, y = WIDTH / 2, HEIGHT / 2
r = 30
cvet = ORANGE
speed = 3
cnt = 0

screen.fill(MINT)
pg.draw.circle(screen, cvet, (x, y), r)
pg.display.update()

flag_play = True
while flag_play:
    cnt += 1
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break


    # Движение по диагонали
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= speed
    if keys[pg.K_RIGHT]:
        x += speed
    if keys[pg.K_UP]:
        y -= speed
    if keys[pg.K_DOWN]:
        y += speed
    if keys[pg.K_SPACE]:
        if cnt >= FPS / 2:
            num = random.randint(1, 255)
            num2 = random.randint(1, 255)
            num3 = random.randint(1, 255)
            cvet = (num, num2, num3)
            cnt = 0

    if x < r:
        x = r
    elif x > WIDTH - r:
        x = WIDTH - r

    if y < r:
        y = r
    elif y > HEIGHT - r:
        y = HEIGHT - r

    # Отрисовка
    screen.fill(MINT)
    pg.draw.circle(screen, cvet, (x, y), r)
    pg.display.update()
