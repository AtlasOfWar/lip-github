import pygame
import button
import math

pygame.font.init()
textfont= pygame.font.SysFont('monospace', 50)
gold = 0
multi = 1
#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
startt_img = pygame.image.load("start.png").convert_alpha()
exitt_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
startt_button = button.Button(304, 125, start_img, 0.8)
exitt_button = button.Button(320, 250, exit_img, 0.8)

game_paused = False
#game loop
run = True
while run:

    screen.fill((202, 228, 241))
    if startt_button.draw(screen):
        game_paused = True
    if exitt_button.draw(screen):
        run = False
    if game_paused:
        screen.fill((202, 228, 241))
        textTBD = textfont.render("Gold: "+ str(round(gold)),1,(255,255,255))
        screen.blit(textTBD,(100,100))
        if start_button.draw(screen):
            gold += 1 * multi
        if exit_button.draw(screen) and gold >= 10:
            gold = gold - 10
            multi = multi + .1

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()