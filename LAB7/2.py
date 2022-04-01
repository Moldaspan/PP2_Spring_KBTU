import pygame as pg
pg.init()
pg.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 50

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE=(0,0,225)

musiclist = ["./music/1.mp3","./music/2.mp3","./music/3.mp3", "./music/4.mp3"]
i = 0
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

pg.mixer.music.load(musiclist[i])
pg.mixer.music.play(1)
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    #keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key ==pg.K_SPACE:
                pg.mixer.music.pause()
            if event.key ==pg.K_z:
                pg.mixer.music.unpause()
            if event.key ==pg.K_RIGHT:
                pg.mixer.music.stop()
                i += 1
                pg.mixer.music.load(musiclist[i])
                pg.mixer.music.play(1)    
            if event.key ==pg.K_LEFT:
                pg.mixer.music.stop
                i -= 1
                pg.mixer.music.load(musiclist[i])
                pg.mixer.music.play(1) 
    pg.mixer.music.queue(musiclist[(i+1) % len(musiclist)])
    pg.display.flip()
pg.quit()