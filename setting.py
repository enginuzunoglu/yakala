import os
import pygame
import pygame.gfxdraw

pygame.init()
top_resimleri=[]
os.environ['SDL_VIDEO_WINDOW_POS'] = "433,50"
#tepsi_ivme=0
title="Yakala !"
width=500
height=650
fps=60
#toplarin_genisliği=16 #topların en ve boyu aynı olmalı tepside görünecek toplar, çift sayı olmalı
#tepsiye_sigacak_top=10 #tek sıra uzunluğu
#yer_cekimi_baslangic=0
#yer_cekimi_ivmesi=.1
#emilecek_kuvvet=.8 #bir cisme carptığında geri dönerken ne kadar guc kaybedeceği
#tepsiye_sigacak_top_satir=1
#ust_cerceve_yukseklik=50
tepsi_mod=1 #tepsi mod:1 tepsi duvara değdiğinde durur
#toplarin_sekme_sayisi=3
#tdth=5 #tepsiye değen topun hassasiyeti
#yer_cekimi_sinir=20 #topların hız sınırı



klasor=os.path.dirname(__file__)
resim=os.path.join(klasor,"resim")
# k_20=pygame.image.load(os.path.join(resim,"k_20.png"))
# k_30=pygame.image.load(os.path.join(resim,"k_30.png"))
# k_40=pygame.image.load(os.path.join(resim,"k_40.png"))
# k_50=pygame.image.load(os.path.join(resim,"k_50.png"))
# k_75=pygame.image.load(os.path.join(resim,"k_75.png"))
# k_100=pygame.image.load(os.path.join(resim,"k_100.png"))
# s_20=pygame.image.load(os.path.join(resim,"s_20.png"))
# s_30=pygame.image.load(os.path.join(resim,"s_30.png"))
# s_40=pygame.image.load(os.path.join(resim,"s_40.png"))
# s_50=pygame.image.load(os.path.join(resim,"s_50.png"))
# s_75=pygame.image.load(os.path.join(resim,"s_75.png"))
# s_100=pygame.image.load(os.path.join(resim,"s_100.png"))
# si_20=pygame.image.load(os.path.join(resim,"si_20.png"))
# si_30=pygame.image.load(os.path.join(resim,"si_30.png"))
# si_40=pygame.image.load(os.path.join(resim,"si_40.png"))
# si_50=pygame.image.load(os.path.join(resim,"si_50.png"))
# si_75=pygame.image.load(os.path.join(resim,"si_75.png"))
# si_100=pygame.image.load(os.path.join(resim,"si_100.png"))
# y_20=pygame.image.load(os.path.join(resim,"y_20.png"))
# y_30=pygame.image.load(os.path.join(resim,"y_30.png"))
# y_40=pygame.image.load(os.path.join(resim,"y_40.png"))
# y_50=pygame.image.load(os.path.join(resim,"y_50.png"))
# y_75=pygame.image.load(os.path.join(resim,"y_75.png"))
# y_100=pygame.image.load(os.path.join(resim,"y_100.png"))
# m_20=pygame.image.load(os.path.join(resim,"m_20.png"))
# m_30=pygame.image.load(os.path.join(resim,"m_30.png"))
# m_40=pygame.image.load(os.path.join(resim,"m_40.png"))
# m_50=pygame.image.load(os.path.join(resim,"m_50.png"))
# m_75=pygame.image.load(os.path.join(resim,"m_75.png"))
# m_100=pygame.image.load(os.path.join(resim,"m_100.png"))
def top_uretiliyor(top_yari_cap,renk):
    top = pygame.Surface((top_yari_cap * 2, top_yari_cap * 2), pygame.SRCALPHA)
    pygame.gfxdraw.aacircle(top, top_yari_cap, top_yari_cap, top_yari_cap - 1, renk)
    pygame.gfxdraw.filled_circle(top, top_yari_cap, top_yari_cap, top_yari_cap - 1, renk)
    return top
mavi=(0,0,255)
kirmizi=(255,0,0)
sari=(255,255,0)
siyah=(0,0,0)
beyaz=(255,255,255)
yesil=(0,255,0)

k_20=top_uretiliyor(10,kirmizi)
k_30=top_uretiliyor(15,kirmizi)
k_40=top_uretiliyor(20,kirmizi)
k_50=top_uretiliyor(25,kirmizi)

s_20=top_uretiliyor(10,sari)
s_30=top_uretiliyor(15,sari)
s_40=top_uretiliyor(20,sari)
s_50=top_uretiliyor(25,sari)

si_20=top_uretiliyor(10,siyah)
si_30=top_uretiliyor(15,siyah)
si_40=top_uretiliyor(20,siyah)
si_50=top_uretiliyor(25,siyah)


y_20=top_uretiliyor(10,yesil)
y_30=top_uretiliyor(15,yesil)
y_40=top_uretiliyor(20,yesil)
y_50=top_uretiliyor(25,yesil)

m_20=top_uretiliyor(10,mavi)
m_30=top_uretiliyor(15,mavi)
m_40=top_uretiliyor(20,mavi)
m_50=top_uretiliyor(25,mavi)

ap=pygame.image.load(os.path.join(resim,"background.png"))


