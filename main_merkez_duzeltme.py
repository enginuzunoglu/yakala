import pygame,random
import sys
from tepsi import *
from toplar import *
from cerceve import *
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super(Game, self).__init__()
        pygame.init()
        self.game_screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        self.clock=pygame.time.Clock()
        self.running=True
        self.giris_zaman=0
        self.toplar=Toplar(self,5,5)
        self.font=pygame.font.SysFont("Helvatica",30)
        self.scor=0
    def new(self):
        self.all_sprites=pygame.sprite.Group()
        self.toplar_grup=pygame.sprite.Group()
        self.cerceve_grup=pygame.sprite.Group()
        self.tepsi = Tepsi(self)
        self.cerceve_sol=Cerceve(5,height/2+20,5,height-45)
        self.cerceve_asagi=Cerceve(width/2,height-5,width-10,5)
        self.cerceve_sag=Cerceve(width-5,height/2+20,5,height-45)
        self.cerceve_ust=Cerceve(width/2,40,width-5,5)
        self.cerceve_grup.add(self.cerceve_sol,self.cerceve_sag,self.cerceve_ust)

        self.all_sprites.add(self.tepsi)
        self.all_sprites.add(self.cerceve_sol,self.cerceve_asagi,self.cerceve_sag,self.cerceve_ust)

        self.run()
    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.draw()
            self.update()
            self.yeniler()
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:sys.exit()
        #tepsiye topların çarpması
        self.carpma = pygame.sprite.spritecollide(self.tepsi, self.toplar_grup, False)
        if self.carpma:
            for i in self.carpma:
                self.scor+=1
                i.yukari()
        #tepsinin yan duvarlara değdiğinde durması
        if tepsi_mod==1:
            self.tepsi_cerceve_temas=pygame.sprite.spritecollide(self.tepsi,self.cerceve_grup,False)
            if self.tepsi_cerceve_temas:
                for i in self.tepsi_cerceve_temas:
                    if i.rect[0]>400:self.tepsi.rect.x-=1
                    if i.rect[0]<100:self.tepsi.rect.x+=1

        #topların yan duvarlara çarpması
        self.top_yan_duvar_temas=pygame.sprite.groupcollide(self.toplar_grup,self.cerceve_grup,False,False)
        if self.top_yan_duvar_temas:
            print(list(self.top_yan_duvar_temas.values())[0][0].rect)
            for i in self.top_yan_duvar_temas:
                #çarpan topun x ekseninde yön değişmesini sağlıyor
                if list(self.top_yan_duvar_temas.values())[0][0].rect[3]>50:
                    i.yana_sekme*=-1
                    print(i.rect)
                if list(self.top_yan_duvar_temas.values())[0][0].rect[3]<50:
                    i.yer_cekimi*=-1
                    i.yana_sekme*=-1

        #topların birbirine çarpması
        self.toplar_grup_yeni=self.toplar_grup.copy()
        for j in self.toplar_grup:
            test_grup=pygame.sprite.Group=([i for i in self.toplar_grup_yeni if i !=j])
            carpiasan_toplar=pygame.sprite.spritecollide(j,test_grup,False)
            if carpiasan_toplar:
                #Topların merkezi bulunuyor, a ve b yi kullanmamın nedeni önceden yazdığım bir kodu tekarardan yazmaya üşendim
                a=j
                b=carpiasan_toplar[0]
                bsm = a.rect[0] + a.rect[2] / 2, a.rect[1] + a.rect[3] / 2  # çarpışan toplardan birinci spriteın merkezi
                ism = b.rect[0] + b.rect[2] / 2, b.rect[1] + b.rect[3] / 2 #çarpışan toplardan ikinci spriteın merkezi



                if a.rect[0]>b.rect[0]:
                    a.rect.x+= (a.rect[2]-(bsm[0]-ism[0]))/2
                    b.rect.x-=(b.rect[2]-(bsm[0]-ism[0]))/2
                else:
                    a.rect.x-=(a.rect[2]-(ism[0] - bsm[0]))/2
                    b.rect.x+=(b.rect[2]-(ism[0] - bsm[0]))/2
                # if bsm[1]>ism[1]:
                #     a.rect.y+=(a.rect[2]- (bsm[1]-ism[1]))/2
                #     b.rect.y-=(b.rect[2]-(bsm[1]-ism[1]))/2
                # else:
                #     a.rect.y-=(a.rect[2]-(ism[1] - bsm[1]))/2
                #     b.rect.y+= (b.rect[2]-(ism[1] - bsm[1]))/2


                bys=b.yana_sekme
                byc=b.yer_cekimi
                ays=a.yana_sekme
                ayc=a.yer_cekimi
                print("ayc = ",ayc )
                print("byc = ",byc)

                a.yana_sekme = bys*(b.cisim_kutle/a.cisim_kutle)**.1
                a.yer_cekimi = byc*(b.cisim_kutle/a.cisim_kutle)**.1
                b.yana_sekme = ays*(a.cisim_kutle/b.cisim_kutle)**.1
                b.yer_cekimi = ayc*(a.cisim_kutle/b.cisim_kutle)**.1
            self.toplar_grup_yeni.remove(j)






    def draw(self):
        self.game_screen.fill((0,0,0))
        self.game_screen.blit(self.font.render("SKOR = {}".format(self.scor),1,(0,0,255)),(20,11))

        self.all_sprites.draw(self.game_screen)

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
    def yeniler(self):
        self.cikis_zaman = pygame.time.get_ticks()
        if 90<self.cikis_zaman%toplarin_gelme_suresi<100:
            x = random.randint(25, width - 25)
            y = random.randint(-50, 0)
            self.toplar = Toplar(self, x, y,30,30)
            self.toplar_grup.add(self.toplar)
            self.all_sprites.add(self.toplar)

        # if 90<self.cikis_zaman%5000<100:
        #     x = random.randint(25, width - 25)
        #     y = random.randint(-50, 0)
        #     self.toplar = Toplar(self, x, y,30,30)
        #     self.toplar_grup.add(self.toplar)
        #     self.all_sprites.add(self.toplar)




game=Game()
while game.running:
    game.new()
