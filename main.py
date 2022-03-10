import random
import sys
from setting import *
from baslangic_level import *
from cerceve import *
from toplar import *
import pygame.gfxdraw


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super(Game, self).__init__()
        self.gelinen_level=1
        self.kacabilecek_top=5
        pygame.init()
        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.devam=True
        self.font = pygame.font.SysFont("Helvatica", 16)
        self.scor = 0
        self.oyun_bitti=True
        self.toplarin_genisligi=16 #topların en ve boyu aynı olmalı tepside görünecek toplar, çift sayı olmalı
        self.tepsiye_sigacak_top=10 #tek sıra uzunluğu
        self.tepsiye_sigacak_top_satir = 1 #tepsiye kaç satır top sığacağı
        self.yer_cekimi_ivmesi=.1
        self.emilecek_kuvvet=.8
        self.ust_cerceve_yukseklik=50
        self.toplarin_sekme_sayisi=1
        self.tdth = 5  # tepsiye değen topun hassasiyeti
        self.yer_cekimi_sinir = 20 #topların hız sınırı
        self.level_iceri_zaman=0
        self.level_son_zaman=0
        self.kucuk_kareler_grup=[]

        self.sayac_1=0

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.toplar_grup = pygame.sprite.Group()
        self.cerceve_grup = pygame.sprite.Group()
        self.baslangic_grup=pygame.sprite.Group()

        self.cerceve_sol = Cerceve(5, height / 2 + 20, 5, height - 45)
        self.cerceve_asagi = Cerceve(width / 2, height - 5, width - 10, 5)
        self.cerceve_sag = Cerceve(width - 5, height / 2 + 20, 5, height - 45)
        self.cerceve_ust = Cerceve(width / 2, 40, width - 5, 5)

        self.cerceve_grup.add(self.cerceve_sol, self.cerceve_sag, self.cerceve_ust,self.cerceve_asagi)
        self.all_sprites.add(self.cerceve_sol, self.cerceve_asagi, self.cerceve_sag, self.cerceve_ust)
        self.level_1()

    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.draw()
            self.update()
            self.top_uret()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        # tepsiye topların çarpması
        self.carpma = pygame.sprite.spritecollide(self.tepsi, self.toplar_grup, False)
        if self.carpma:
            for i in self.carpma:
                self.scor += 1
                i.tss-=1
                i.yukari()
        # tepsinin yan duvarlara değdiğinde durması
        if tepsi_mod == 1:
            self.tepsi_cerceve_temas = pygame.sprite.spritecollide(self.tepsi, self.cerceve_grup, False)
            if self.tepsi_cerceve_temas:
                for i in self.tepsi_cerceve_temas:
                    if i.rect[0] > 400: self.tepsi.rect.x -= 1
                    if i.rect[0] < 100: self.tepsi.rect.x += 1

        # topların yan duvarlara çarpması
        self.top_duvar_temas = pygame.sprite.groupcollide(self.toplar_grup, self.cerceve_grup, False, False)
        if self.top_duvar_temas:
            for i in self.top_duvar_temas:
                # TopunHangiDuvaraTemasEttiğini bulmak için onun ordinatının boyuna göre karşılaştırma yapıyorum.
                thdte = list(self.top_duvar_temas.values())[0][0].rect
                # Yan DUvar Sağ
                if thdte[3] > 50 and thdte[0] > width / 2:
                    tdigm = i.rect.right - thdte.left  # TopunDuvarınİçineGirmeMiktarı
                    i.rect.x -= tdigm
                    i.yana_sekme *= -1*self.emilecek_kuvvet
                # Yan duvar Sol

                if thdte[3] > 50 and thdte[0] < width / 2:
                    tdigm = (thdte.right - i.rect.left)  # TopunDuvarınİçineGirmeMiktarı
                    i.rect.x += tdigm
                    i.yana_sekme *= -1*self.emilecek_kuvvet
                # Üst Duvar
                if thdte[3] < 50 and thdte[1] < height / 2:
                    tdigm = thdte.bottom - i.rect.top  # TopunDuvarınİçineGirmeMiktarı
                    i.rect.y += tdigm
                    i.yer_cekimi *= -1*self.emilecek_kuvvet
                #Alt Duvar
                if thdte[3]<50 and thdte[1]>height/2:

                    if i.image not in self.istenen_top_sirasi:
                        i.yer_cekimi *= -1*self.emilecek_kuvvet
                       # i.yana_sekme *= -1



        # topların birbirine çarpması
        self.toplar_grup_yeni = self.toplar_grup.copy()
        for j in self.toplar_grup:
            test_grup = pygame.sprite.Group = ([i for i in self.toplar_grup_yeni if i != j])
            carpiasan_toplar = pygame.sprite.spritecollide(j, test_grup, False, collided=pygame.sprite.collide_circle)

            if carpiasan_toplar:
                a = j
                b = carpiasan_toplar[0]
                # if a.rect[0] > b.rect[0]:
                #     iigx = b.rect.right - a.rect.left  # iç içe giren karelerin apsisi / içiçegirenx
                #
                # else:
                #     iigx = a.rect.right - b.rect.left
                # if a.rect[1] > b.rect[1]:
                #     iigy = b.rect.bottom - a.rect.top  # iç içe giren karelerin ordinatı / içiçegireny
                # else:
                #     iigy = a.rect.bottom - b.rect.top
                #
                # # ya x ekseninden ya da y den iki kareyide iç içe girmiş kısımların yarısı kadar ötelediğimizde kesşim ortadan kalkıyor
                #
                # if iigx > iigy:
                #     if a.rect[0] > b.rect[0]:
                #         a.rect.x += iigx / 2
                #         b.rect.x -= iigx / 2
                #
                #     else:
                #         a.rect.x -= iigx / 2
                #         b.rect.x += iigx / 2
                # else:
                #     if a.rect[1] > b.rect[1]:
                #         a.rect.y += iigy / 2
                #         b.rect.y -= iigy / 2
                #     else:
                #         a.rect.y -= iigy / 2
                #         b.rect.y += iigy / 2

                # karelere x ekseninde ve y eksenindeki ötelemeler çarpışma durumunda diğer kareye ektaarılıyor.
                # b cisminin yana sekmesi a cisminin yana sekmesine, ayrıca kütlesi büyük olan cisimden küçüğe daha fazla aktarım
                # küçükten büyüğe  daha az aktarım oluyor
                bys = b.yana_sekme
                byc = b.yer_cekimi
                ays = a.yana_sekme
                ayc = a.yer_cekimi

                a.yana_sekme = bys * (b.cisim_kutle / a.cisim_kutle) ** .1
                a.yer_cekimi = byc * (b.cisim_kutle / a.cisim_kutle) ** .1
                b.yana_sekme = ays * (a.cisim_kutle / b.cisim_kutle) ** .1
                b.yer_cekimi = ayc * (a.cisim_kutle / b.cisim_kutle) ** .1
            self.toplar_grup_yeni.remove(j)


    def draw(self):
        # self.game_screen.fill((0, 0, 0))
        self.game_screen.blit(ap, (0, 0))
        self.game_screen.blit(self.font.render("Kaçırılabilecek Top Sayısı = {}".format(self.kacabilecek_top), 1, (0, 0, 255)), (20, 11))
        self.game_screen.blit(self.font.render("SÜRE : {}".format(int((self.level_iceri_zaman - self.level_giris_zaman) / 1000)), 1, (0, 0, 255)),
                              (350, 11))

        self.cerceve_grup.draw(self.game_screen)
        self.all_sprites.draw(self.game_screen)

    def update(self):
        self.all_sprites.update()
        pygame.display.update()

    def top_uret(self):
        self.son_zaman=pygame.time.get_ticks()
        y=random.randrange(self.top_zaman_aralik-1000,self.top_zaman_aralik,100)
        if self.son_zaman-self.level_iceri_zaman>y and len(self.gelecek_top_sirasi)>len(self.toplar_grup):
            x=random.randrange(25,width-25,5)
            self.toplar = Toplar(self, x,self.gelecek_top_sirasi[self.sayac_1%len(self.gelecek_top_sirasi)])
            self.sayac_1+=1
            self.toplar_grup.add(self.toplar)
            self.all_sprites.add(self.toplar)

            self.level_iceri_zaman=self.son_zaman


    def tusa_basilmasi_bekleniyor(self):
        pygame.display.update()

        for i in self.baslangic_grup:
            if i.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if i.baslik=="Oyna":
                        self.level_giris_zaman = pygame.time.get_ticks()
                        self.run()
                    if i.baslik == "Tekrar Oyna" or i.baslik == "Devam Et":

                        self.level_giris_zaman = pygame.time.get_ticks()
                        self.all_sprites.empty()
                        self.baslangic_grup.empty()
                        if i.baslik == "Devam Et":
                            self.gelinen_level+=1

                        if self.gelinen_level == 2:
                            self.devam: False
                            self.level_2()

                        if self.gelinen_level == 3:
                            self.level_giris_zaman = pygame.time.get_ticks()

                            self.devam: False
                            self.level_3()


                    if i.baslik == "Çıkış":
                        sys.exit()
    def level_1(self):
        self.tus = Tus(self, "Oyna", (width / 2, height / 2))
        self.bilgilendirme = Bilgilendirme(self, "Topları verilen sırada aşağıdaki tablaya yerleştirmeye çalışınız")
        self.istenen_top_sirasi=[k_20,m_20,m_40]
        self.tepsiye_sigacak_top=len(self.istenen_top_sirasi)
        self.level_iceri_zaman=pygame.time.get_ticks()
        self.gelecek_top_sirasi = [k_20,m_30,m_40,m_20]
        self.top_zaman_aralik=5000
        tepsinin_genisligi=(self.toplarin_genisligi+2)*self.tepsiye_sigacak_top+2
        if tepsinin_genisligi<70: tepsinin_genisligi=70
        self.tepsi=Tepsi(self,(tepsinin_genisligi, (self.toplarin_genisligi+2)*self.tepsiye_sigacak_top_satir+2))
        self.all_sprites.add(self.tepsi)
        self.kacabilecek_top=5
        self.yer_cekimi_ivmesi=.1
        self.toplarin_sekme_sayisi=3
        self.emilecek_kuvvet=.8

        self.giris_ekrani()
    def level_2(self):
        self.tepsi.kill()
        self.kucuk_kareler_grup=[]
        self.tus = Tus(self, "Oyna", (width / 2, height / 2))
        self.bilgilendirme = Bilgilendirme(self, "Topları verilen sırada aşağıdaki tablaya yerleştirmeye çalışınız")
        self.istenen_top_sirasi = [s_30,m_40]
        self.tepsiye_sigacak_top=len(self.istenen_top_sirasi)
        self.level_iceri_zaman = pygame.time.get_ticks()
        self.gelecek_top_sirasi = [s_30, s_40, m_40]
        self.top_zaman_aralik = 2000
        self.tepsi = Tepsi(self, ((self.toplarin_genisligi + 2) * self.tepsiye_sigacak_top + 2,
                                  (self.toplarin_genisligi + 2) * self.tepsiye_sigacak_top_satir + 2))
        self.all_sprites.add(self.tepsi)
        self.kacabilecek_top = 5
        self.yer_cekimi_ivmesi = .1
        self.toplarin_sekme_sayisi = 4
        self.emilecek_kuvvet=1

        self.giris_ekrani()
        self.run()
    def level_3(self):
        self.tepsi.kill()
        self.kucuk_kareler_grup=[]
        self.tus = Tus(self, "Oyna", (width / 2, height / 2))
        self.bilgilendirme = Bilgilendirme(self, "Topları verilen sırada aşağıdaki tablaya yerleştirmeye çalışınız")
        self.istenen_top_sirasi = [s_30,m_40,s_20,s_20]
        self.tepsiye_sigacak_top=len(self.istenen_top_sirasi)
        self.level_iceri_zaman = pygame.time.get_ticks()
        self.gelecek_top_sirasi = [s_20, s_30, s_40, s_50, m_30, k_20,m_40]
        self.top_zaman_aralik = 1500
        self.tepsi = Tepsi(self, ((self.toplarin_genisligi + 2) * self.tepsiye_sigacak_top + 2,
                                  (self.toplarin_genisligi + 2) * self.tepsiye_sigacak_top_satir + 2))
        self.all_sprites.add(self.tepsi)
        self.giris_ekrani()
        self.run()
    def giris_ekrani(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        konum = 200  # bilgilendirme toplarının ekranda x ekseninde görüldüğü ilk konum
        self.game_screen.blit(ap,(0,0))

        ############## top sırasının olması gereken görüntüsü  #############################33

        for i in self.istenen_top_sirasi:
            konum += i.get_rect()[3]
            self.top_sirasi = Top_sirasi(self, i, konum,height/4)
            self.top_sirasi_yukari=Top_sirasi(self,i,konum-30,20)

        #####################################################################################
            # Ekrana tuşlar ve bilgilendirme yazısı için gruplar oluşturuluyor

            self.baslangic_grup.add(self.tus, self.bilgilendirme)
            self.baslangic_grup.add(self.top_sirasi)
            self.baslangic_grup.draw(self.game_screen)
            self.all_sprites.add(self.top_sirasi_yukari)

        while self.devam:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.baslangic_grup.draw(self.game_screen)
            pygame.display.update()
            self.tusa_basilmasi_bekleniyor()


    def level_sonu(self):
        #pygame.time.wait(1000)
        self.game_screen.blit(ap,(0,0))
        self.update()
        self.all_sprites.draw(self.game_screen)
        self.baslangic_grup.empty()
        self.toplar_grup.empty()
        self.all_sprites.empty()
        self.update()
        if self.oyun_bitti==False:
            self.tus=Tus(self, "Devam Et", (width / 2, height / 2 - 25))
            self.baslangic_grup.add(self.tus)

            self.tus=Tus(self, "Çıkış", (width / 2, height / 2 + 25))

            self.baslangic_grup.add(self.tus)
        else:
            self.tus=Tus(self, "Tekrar Oyna", (width / 2, height / 2 - 25))
            self.baslangic_grup.add(self.tus)

            self.tus=Tus(self, "Çıkış", (width / 2, height / 2 + 25))
            self.baslangic_grup.add(self.tus)

        while self.devam:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.baslangic_grup.draw(self.game_screen)
            pygame.display.update()
            self.tusa_basilmasi_bekleniyor()




game = Game()
while game.running:
    game.new()
