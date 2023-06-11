#$python -m venv env se crea un entorno
#source env/Scripts/activate    entramos al entorno y ejecuta el script activate
#si usamos el pip list, solo muestra las caracteristicas del entorno env

import pygame, sys
from functions import *
from config import *
import random
from donas import *

pygame.init()   #para iniciarlo

screen = pygame.display.set_mode((WIDTH, HEIGHT))  #display es la pantalla
pygame.display.set_caption("Donuts War")

icono = pygame.image.load("images\dona.png")
icono = pygame.transform.scale(icono.convert_alpha(), SIZE_ICON)
pygame.display.set_icon(icono)

fondo = pygame.image.load("images\\background.jpg").convert()
fondo = pygame.transform.scale(fondo.convert(), SIZE)


fuente = pygame.font.SysFont("rage", 48)
texto = fuente.render("PUM", False, VERDE)

homero_l = pygame.image.load("images\homer_left.png")
homero_l = pygame.transform.scale(homero_l.convert_alpha(), HOMERO_SIZE)
rect_homero = homero_l.get_rect()
rect_homero.midbottom = (CENTER_X, DISPLAY_BOTTOM)
homero = homero_l
homero_r = pygame.image.load("images\homer_right.png")
homero_r = pygame.transform.scale(homero_r.convert_alpha(), HOMERO_SIZE)

rect_boca = pygame.Rect(0, 0, 50, 10)

donas = []

for i in range(10):
    x = random.randrange(30, WIDTH - 30)
    y= random.randrange(-1000, 0)

    dona = Dona(DONUT_SIZE, (x,y), "images\dona.png")
    # dona = pygame.image.load("D:\Desktop\Juego Clase\images\dona.png")
    # dona = pygame.transform.scale(dona.convert_alpha(), DONUT_SIZE)
    
    donas.append(dona)
    # dona.get_rect().center = (random.randrange(30, WIDTH - 30),random.randrange(-1000, 0))

    

rect_boca.x = rect_homero.x + 25
rect_boca.y = rect_homero.y + 190

pygame.mixer_music.load("sounds\ouch.mp3")
flag_sound = True

font = pygame.font.Font("fonts\simpsons.ttf")
score = 0
while True:

    clock.tick(FPS)
    screen.blit(fondo, ORIGIN)

    for evento in pygame.event.get():   #Actualizacion de eventos constante.
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if rect_homero.left > DISPLAY_LEFT:
            rect_homero.x -= HOMERO_SPEED
            rect_boca.x = rect_homero.x + 25
            rect_boca.y = rect_homero.y + 190
            homero = homero_l
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if rect_homero.right < DISPLAY_RIGHT:
            rect_homero.x += HOMERO_SPEED
            rect_boca.x = rect_homero.x + 65
            rect_boca.y = rect_homero.y + 190
            homero = homero_r

    
    
    screen.blit(homero, rect_homero)
    
    for dona in donas:
        if dona.rect.bottom < DISPLAY_BOTTOM:
            flag_dona = True
            flag_sound = True
            if dona.activate:
                dona.update()
            else:
                dona.rect.y = 0

            if rect_boca.colliderect(dona.rect):
                dona.activate = False
                if flag_sound:
                    score += 1
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_pos(0.3)
                    flag_sound = False
                else:
                    flag_sound = True
            
            if dona.activate:
                screen.blit(dona.image, dona.rect)

    
    texto = font.render(f"Score: {score}", True, AMARILLO)
    screen.blit(texto, DISPLAY_SCORE)
    pygame.display.flip()   #actualiza la pantalla