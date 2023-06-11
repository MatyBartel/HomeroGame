import pygame

def colision_circulos(rect_1:pygame.Rect, rect_2:pygame.Rect):
    colision = False
    cateto_x = rect_1.centerx - rect_2.centerx
    cateto_y = rect_1.centery - rect_2.centery
    
    limite = rect_1.width // 2 + rect_2.width // 2

    distancia = (cateto_x ** 2 + cateto_y ** 2) ** 0.5

    if distancia <= limite:
        colision = True

    return colision