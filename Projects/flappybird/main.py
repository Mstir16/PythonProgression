import pygame
import sys
import random

pygame.display.set_caption("FlappyBird | Mstir's Scuffed Version")
pygame_icon = pygame.image.load('assets/favicon.ico')
pygame.display.set_icon(pygame_icon)

def RandomBG():
    BGChoice = random.randint(1,2)
    
    if BGChoice == 1:
        return pygame.image.load("assets/background-day.png").convert()
    else:
        return pygame.image.load("assets/background-night.png").convert()

def RandomBird():
    BirdChoice = random.randint(1,3)

    if BirdChoice == 1:
        return "yellowbird"
    elif BirdChoice == 2:
        return "redbird"
    elif BirdChoice == 3:
        return "bluebird"

def BirdGet(birdvar,animtype):
    if birdvar == "yellowbird":
        if animtype == "mf":
            return pygame.image.load("assets/yellowbird-midflap.png").convert()
        elif animtype == "uf":
            return pygame.image.load("assets/yellowbird-upflap.png").convert()
        elif animtype == "df":
            return pygame.image.load("assets/yellowbird-downflap.png").convert()
    elif birdvar == "redbird":
        if animtype == "mf":
            return pygame.image.load("assets/redbird-midflap.png").convert()
        elif animtype == "uf":
            return pygame.image.load("assets/redbird-upflap.png").convert()
        elif animtype == "df":
            return pygame.image.load("assets/redbird-downflap.png").convert()

    elif birdvar == "bluebird":
        if animtype == "mf":
            return pygame.image.load("assets/bluebird-midflap.png").convert()
        elif animtype == "uf":
            return pygame.image.load("assets/bluebird-upflap.png").convert()
        elif animtype == "df":
            return pygame.image.load("assets/bluebird-downflap.png").convert()

def game_floor():
    screen.blit(floor_base,(floor_x_pos,900))
    screen.blit(floor_base,(floor_x_pos + 576,900))

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            die_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 1000:
        die_sound.play()
        return False
    return True

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midbottom=(700,random_pipe_pos-300))
    bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5

    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe,pipe)

def RandomPipe():
    PipeChoice = random.randint(1,2)
    
    if PipeChoice == 1:
        return pygame.image.load('assets/pipe-green.png')
    else:
        return pygame.image.load('assets/pipe-red.png')

pygame.init()
clock = pygame.time.Clock()

# Settings:

gravity = 0.25
bird_movement = 0


screen = pygame.display.set_mode((576,1024))

RDbrd = RandomBird()

BGSelected = RandomBG()
BG = pygame.transform.scale2x(BGSelected)

BirdMid = BirdGet(RDbrd,"mf")
bird = pygame.transform.scale2x(BirdMid)
bird_rect = bird.get_rect(center=(100,512))


base_png = pygame.image.load("assets/base.png").convert()
floor_base = pygame.transform.scale2x(base_png)
floor_x_pos = 0

msg_png = pygame.image.load("assets/message.png").convert_alpha()
msg = pygame.transform.scale2x(msg_png)
game_over_rect = msg.get_rect(center=(288,512))

pipe_image = RandomPipe()
pipe_surface = pygame.transform.scale2x(pipe_image)

pipe_list = []
pipe_height = [400,600,800]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
die_sound = pygame.mixer.Sound('assets/audio/die.wav')

game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                bird_rect.center = (100,512)
                bird_movement = 0
                pipe_list.clear()
                game_active = True
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
        
    screen.blit(BG,(0,0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        game_active = check_collision(pipe_list)
    else:
        screen.blit(msg, game_over_rect)

    floor_x_pos -= 1
    game_floor()

    if floor_x_pos <= 576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
