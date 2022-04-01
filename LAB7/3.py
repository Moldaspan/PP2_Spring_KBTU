import pygame as pg

pg.init()
pg.display.set_caption("Ball moving")

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

step = 10

x, y = WIDTH//2, HEIGHT//2
RAD=25

done = True
while done:
    clock.tick(FPS)

    keys=pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False

    screen.fill(WHITE)

    if keys[pg.K_RIGHT] and x + RAD < WIDTH:
        x += step
    if keys[pg.K_LEFT] and x - RAD > 0:
        x -= step
    if keys[pg.K_DOWN] and y + RAD < HEIGHT:
        y += step
    if keys[pg.K_UP] and y - RAD > 0:
        y -= step
            
        
    pg.draw.circle(screen, RED, (x, y), RAD)


    pg.display.flip()
pg.quit()
