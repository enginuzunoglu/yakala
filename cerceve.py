import pygame
from setting import *
class Cerceve(pygame.sprite.Sprite):
    def __init__(self,baslangic_x,baslangic_y,genislik,yukseklik):
        super(Cerceve, self).__init__()
        self.image=pygame.Surface((genislik,yukseklik))
        self.image.fill((255,255,0))
        self.rect=self.image.get_rect()
        self.rect.center=(baslangic_x,baslangic_y)