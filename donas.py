import pygame

class Dona:
    def __init__(self, size, coordenate, path_image):
        self.coordenate = coordenate
        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordenate
        self.activate = True
    
    def update(self):
        self.rect.y += 5
        