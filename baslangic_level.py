


from setting import *
class Tus(pygame.sprite.Sprite):
    def __init__(self,game,baslik,konum):
        super(Tus, self).__init__()
        self.baslik=baslik
        self.game=game
        self.image=pygame.Surface((300,40))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=konum
        self.image.blit(pygame.font.SysFont("Helvatica",60).render(baslik,1,(0,255,0)),(0,0))
class Bilgilendirme(pygame.sprite.Sprite):
    def __init__(self,game,bilgi_yazi):
        super(Bilgilendirme, self).__init__()
        self.game=game
        self.image=pygame.Surface((400,40))
        self.rect=self.image.get_rect()
        self.rect.center=(width/2,height/3)
        self.image.blit(pygame.font.SysFont("Helvatica",20).render(bilgi_yazi,1,(0,255,0)),(0,0))
class Top_sirasi(pygame.sprite.Sprite):
    def __init__(self,game,top,genislik,yukseklik):
        super(Top_sirasi, self).__init__()
        self.game=game
        self.image=pygame.transform.scale(top,(top.get_rect().width*.6,top.get_rect().height/2))


        self.rect=self.image.get_rect()

        self.rect.center=(genislik,yukseklik)
        if top.get_rect()[3]==20:
            self.image.blit(pygame.font.SysFont("Helvatica",(12)).render("S",1,(0,50,0)),(3,1))
        if top.get_rect()[3]==30:
            self.image.blit(pygame.font.SysFont("Helvatica",(18)).render("M",1,(0,50,0)),(3,2))
        if top.get_rect()[3]==40:
            self.image.blit(pygame.font.SysFont("Helvatica",(25)).render("L",1,(0,50,0)),(5,2))
        if top.get_rect()[3]==50:
            self.image.blit(pygame.font.SysFont("Helvatica",(27)).render("XL",1,(0,50,0)),(5,3))




