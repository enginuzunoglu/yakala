import pygame.gfxdraw

from setting import *
from tepsi import *


class Toplar(pygame.sprite.Sprite):
    def __init__(self, game, cikis_noktasi_x=width / 2,resim=None):
        super(Toplar, self).__init__()

        # top = pygame.Surface((top_yari_cap * 2, top_yari_cap * 2), pygame.SRCALPHA)
        # pygame.gfxdraw.aacircle(top, top_yari_cap, top_yari_cap, top_yari_cap - 1, renk)
        # pygame.gfxdraw.filled_circle(top, top_yari_cap, top_yari_cap, top_yari_cap - 1, renk)


        self.yer_cekimi = 0
        self.game = game
        self.image=resim
        #self.image=pygame.transform.scale(self.image,(boyut_x,boyut_y))
        #self.orjinal_image=self.image
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius=int(self.rect.width*.5)
        #self.top=pygame.draw.circle(self.image,self.top_renk,self.rect.center,self.radius)
        self.cisim_kutle=self.rect[2]*self.rect[3]/100
        self.rect.center = (cikis_noktasi_x, self.game.ust_cerceve_yukseklik+50)
        self.sekme_sayisi=0
        self.yana_sekme=0
        self.tss=self.game.toplarin_sekme_sayisi
    def update(self, *args):
        #topun üzerinde yazan sayı
        if self.image.get_rect()[3]==20:
            yazi_konum=(2,5);yazi="-S";boyut=15
        if self.image.get_rect()[3]==30:
            yazi_konum=(3,7);yazi="-M";boyut=21
        if self.image.get_rect()[3]==40:
            yazi_konum=(6,10);yazi="-L";boyut=30
        if self.image.get_rect()[3]==50:
            yazi_konum=(3,14);yazi="-XL";boyut=30

        self.game.game_screen.blit(pygame.font.SysFont("Helvatica",boyut).render(str(self.tss)+yazi, 0, (0, 125, 255)),(self.rect.x+yazi_konum[0],self.rect.y+yazi_konum[1]))


        #pygame.draw.line(self.image,(0,0,255),(0,0),(self.image.get_rect()[2]/2,0),10)
        if self.yer_cekimi > self.game.yer_cekimi_sinir: self.yer_cekimi = self.game.yer_cekimi_sinir
        if self.yer_cekimi < -self.game.yer_cekimi_sinir: self.yer_cekimi = -self.game.yer_cekimi_sinir

        self.yer_cekimi += self.game.yer_cekimi_ivmesi
        self.rect.x+=self.yana_sekme
        self.rect.y += self.yer_cekimi
        #self.dondurme()
        if self.rect.y>height: self.kill();self.game.kacabilecek_top-=1


    def yukari(self):
        #bu kodu update in içine yazdığımda olmadı, mecbur ayrı bir fonksiyon yazdım.
        # topun tepsinin orta noktasına uzaklığı
        ttonu=self.rect[0]+self.rect[2]/2-self.game.tepsi.rect[0]-self.game.tepsi.rect[2]/2
        self.yana_sekme=int(ttonu/(self.game.tepsi.rect[2]/2)*self.game.tdth) #TepsiyeDeğenTopunHassasiyeti
        # çarpan topun y ekseninde hem ters yöne dönmesini hemde enerjisinin azalmasını sağlıyor.

        if self.yer_cekimi > self.game.yer_cekimi_sinir: self.yer_cekimi=self.game.yer_cekimi_sinir
        if self.yer_cekimi<-self.game.yer_cekimi_sinir: self.yer_cekimi=-self.game.yer_cekimi_sinir
        self.yer_cekimi *= -self.game.emilecek_kuvvet
        self.rect.y -= (
        self.rect.bottom - self.game.tepsi.rect.top)  # çıkşmadan sonraki döngüde tekrar çakışmaması için yukardan gelenin alt noktası ile aşağdakinin üst noktasının çakıştığı bölge sonraki harekete eklenerek bir çakışma olması engelleniyor

        self.sekme_sayisi+=1

        #Oyunun bitip bitmemesi araştırılıyor.

        if self.sekme_sayisi==self.game.toplarin_sekme_sayisi:
            self.kill()
            self.kucukkareler=KucukToplar(self, self.game, self.game.tepsi.kucukkaresayisi)
            self.game.all_sprites.add(self.kucukkareler)


            #tepside oluşan toplarla, istenen topların karşılaştıtılması yapılıyor


            self.game.kucuk_kareler_grup.append(self.image)
            if len(self.game.kucuk_kareler_grup)==len(self.game.istenen_top_sirasi) or self.game.kacabilecek_top==0:
                if self.game.kucuk_kareler_grup==self.game.istenen_top_sirasi:
                    self.game.oyun_bitti=False
                    self.game.level_sonu()
                if self.game.kacabilecek_top==0 or self.game.kucuk_kareler_grup!=self.game.istenen_top_sirasi:
                    self.game.oyun_bitti=True
                    self.game.level_sonu()

            self.game.tepsi.kucukkaresayisi+=1  #bunu tepsiden almamın nedeni sayacı bu bölgeye koyduğumda sadecee o sprite için geçerli oluyor. tepsi yok olmadığı için sayaç aynı kalıyor.
    #def dondurme(self):

            # self.aci += 5
            # self.new_image = pygame.transform.rotate(self.orjinal_image, self.aci)
            # old_center=self.rect.center
            # self.image=self.new_image
            # self.rect=self.image.get_rect()
            # self.rect.center=old_center
class KucukToplar(pygame.sprite.Sprite):
    def __init__(self,toplar,game,kks):
        super(KucukToplar, self).__init__()
        self.kks=kks
        self.toplar=toplar
        self.game=game
        self.image = self.toplar.image
        self.image=pygame.transform.scale(self.image,(15,15))
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(-10,-10)

    def update(self, *args):
        # topun merkezi ile tepsinin köşesi çakışıyor, onun için /2 yapıp +2 ekedik,topların genişliği ve +2 birim mesafe bırakmak için, her top eklendiğinde onunla çarpacak alt satıra geçtiğinde baştan başlamak için kalanı buluyor
        x = self.toplar.game.tepsi.rect[0] + self.game.toplarin_genisligi / 2 + 2 + (self.game.toplarin_genisligi + 2) * (
                    self.kks % self.game.tepsiye_sigacak_top)
        y = self.toplar.game.tepsi.rect[1] + self.game.toplarin_genisligi / 2 + 2 + int(
            self.kks / self.game.tepsiye_sigacak_top) * (self.game.toplarin_genisligi+2)
        self.rect.center = (x, y)

