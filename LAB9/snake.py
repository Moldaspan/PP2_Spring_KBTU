import pygame
from random import randrange
pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 7 
cell = 40  

#Colors
WHITE = (255, 255, 255)
GREY = (68, 75, 82)
RED = (252, 108, 133)
GREEN = (0, 168, 107)
BLACK = (0, 0, 0)
BLUE = (121, 160, 193)
BC = (240, 255, 240)


font = pygame.font.SysFont("Copperplate Gothic Bold", 30)
font1 = pygame.font.SysFont("Copperplate Gothic Bold", 75)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')


level = 1
SCORE = 0
sp = 20
finished = False
lose = False

time_delay = 6000
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell)) 
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

class Snake:
    def __init__(self):
        self.speed = sp
        self.body = [[80, 80],[1000,1000],[1040,1040],[1080,1080],[1120,1120],[1160, 1160]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN
    
    def move(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT and self.destination != 'right': 
                    self.dx = -self.speed 
                    self.dy = 0
                    self.destination = 'left'
                
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
                    
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        
        
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    
   
    def collide_food(self, f:Food):
        global SCORE
        global level
        global FPS
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            SCORE += 1
            if SCORE % 3 == 0:
                level += 1
                FPS += 2
            if (SCORE + 1) % 5 == 0:
                SCORE += randrange(2, 4)
            self.body.append([1000, 1000])
    
    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:
            lose = True

    
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()

s = Snake() 
f = Food()
clock = pygame.time.Clock() 
   
while not finished:
    clock.tick(FPS) 
    screen.fill(GREY) 

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        if event.type == timer_event:
            f.redraw()

    
    s.draw() 
    s.move()
    f.draw() 
    s.collide_food(f) 
    s.collide_self() 
    
    f.draw()
    s.draw()
    s.move()
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)



    game_over = font1.render(f'GAME OVER', False, BLACK)
    game_over_score = font1.render(f'SCORE: {SCORE} ', False, GREEN) 
    text = font.render(f"LEVEL: {level}", False, WHITE)
    screen.blit(text,(25, 20))  
    text1 = font.render(f"SCORE: {SCORE}", False, WHITE)
    screen.blit(text1,(25, 40)) 
    
    
    while lose:
        pygame.draw.rect(screen, WHITE, (100, 75, 600, 400)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False

            
            text = font.render(f"LEVEL: {level}", False, BLACK)
            text1 = font.render(f"SCORE: {SCORE}", False, BLACK)
            screen.blit(game_over, (240,200))
            screen.blit(text,(350, 270))
            screen.blit(text1,(350, 300))

            pygame.display.flip() 
    pygame.display.flip()  
pygame.quit() 