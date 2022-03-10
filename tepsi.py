import pygame

from setting import *


class Tepsi(pygame.sprite.Sprite):
    def __init__(self,game,boyut):
        super(Tepsi, self).__init__()
        self.game=game
        self.kucukkaresayisi=0
        self.tepsi_ivme = 0
        self.carpan = 1
        self.image = pygame.Surface(boyut)

        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height- 30)  # tepsiyi en alttan biraz yukarı ve yatayda ekranın ortası olarak ayarladım

    def update(self, *args) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            if self.tepsi_ivme < 5:  # yön tuşlarına basıldığında ivme artıyor, basılmadığında 0 a doğru azalıyor.
                self.tepsi_ivme += 0.5
        else:
            if self.tepsi_ivme > 0:
                self.tepsi_ivme -= 0.5
                if self.tepsi_ivme<0:self.tepsi_ivme=0
        if keys[pygame.K_RIGHT]:  # hangi yön tuşuna basılırsa ona göre seçim yapılıp rect in azalıp
            # artırılması sağlanıyor.
            self.carpan = 1
        if keys[pygame.K_LEFT]:
            self.carpan = -1



        if tepsi_mod==1:
            if self.game.tepsi_cerceve_temas==[]:
                self.rect.x += round(self.tepsi_ivme) * self.carpan
        if tepsi_mod==2:
            if self.rect.left>width:
                self.rect.right=-self.image.get_rect()[3]
            if self.rect.right<0-self.image.get_rect()[3]:
                self.rect.left=width
            self.rect.x += round(self.tepsi_ivme) * self.carpan


