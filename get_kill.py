import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
speed = 5

pygame.time.delay(10000)

sound_effect1 = pygame.mixer.Sound('death.wav')
sound_effect1.play()

pygame.mixer.music.load('thriller.wav')
pygame.mixer.music.play(-1, 0.0)

halloween = pygame.image.load('halloween.png')
halloween_coordinate = halloween.get_rect()
halloween_coordinate.center = (400,300)

oldman = pygame.image.load('old-man.png')
oldman_coordinate = oldman.get_rect()
oldman_coordinate.center = (200, 150) 

FPS = 30
clock = pygame.time.Clock()
begin = True
while begin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            begin = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and halloween_coordinate.left>0:
        halloween_coordinate.x -= speed
    elif key[pygame.K_RIGHT] and halloween_coordinate.right<800:
        halloween_coordinate.x += speed
    elif key[pygame.K_UP] and halloween_coordinate.top>0:
        halloween_coordinate.y -= speed
    elif key[pygame.K_DOWN] and halloween_coordinate.bottom<600:
        halloween_coordinate.y += speed
    screen.fill((0,0,0))
    if halloween_coordinate.colliderect(oldman_coordinate):
        print('YOU KILLED!')
        oldman_coordinate.x = random.randint(0, 800-64)
        oldman_coordinate.y = random.randint(0, 600-64)
    screen.blit(halloween, halloween_coordinate)
    screen.blit(oldman, oldman_coordinate)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()