#see programm teeb space invaders mängu

import pygame
pygame.init()

aken = pygame.display.set_mode((800, 600)) #teeb aknakese
pygame.display.set_caption("Space Invaders") #paneb aknale nime
laev = pygame.image.load("laev.png") #võtab välimuseks pildi laevast
muusika = pygame.mixer.music.load("spaceinvaders1.wav")
tulistamine = pygame.mixer.Sound("shoot.wav")

pygame.mixer.music.play(-1)

#VÄRVID
VALGE = (255, 255, 255)

#MÄNGIJA
class mangija(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6

#KUULID
class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 12
    def draw(self,aken):
        pygame.draw.circle(aken, self.color, (self.x,self.y), self.radius)
        
#MAJA
class klots():
    majaterve = (pygame.image.load("1.png"))
    majakatki1 = (pygame.image.load("2.png"))
    majakatki2 = (pygame.image.load("3.png"))
    majakatki3 = (pygame.image.load("4.png"))
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.eluCount = 0
        self.hitbox = (self.x, self.y,25,25)
        self.nahtav = True

    def draw(self,aken):
        if self.nahtav == True:
            self.hitbox = (self.x, self.y,25,25)
            if self.eluCount == 0:
                aken.blit(self.majaterve, (self.x, self.y))
            else:
                if self.eluCount == 1:
                    aken.blit(self.majakatki1, (self.x,self.y))
                elif self.eluCount == 2:
                    aken.blit(self.majakatki2, (self.x,self.y))
                elif self.eluCount == 3:
                    aken.blit(self.majakatki3, (self.x,self.y))
            #pygame.draw.rect(aken, (255,0,0), self.hitbox,2)
        
    def sainpihta(self):
        if self.eluCount < 4:
            self.eluCount += 1
        else:
            self.nahtav = False

#VASAK NURK
class nurkvasak():
    nurkterve = (pygame.image.load("kolmnurkv1.png"))
    nurkkatki1 = (pygame.image.load("kolmnurkv2.png"))
    nurkkatki2 = (pygame.image.load("kolmnurkv3.png"))
    nurkkatki3 = (pygame.image.load("kolmnurkv4.png"))
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.eluCount = 0
        self.hitbox = (self.x, self.y,24,24)
        
    def draw(self,aken):
        if self.eluCount == 0:
            aken.blit(self.nurkterve, (self.x, self.y))
        else:
            if self.eluCount == 1:
                aken.blit(self.nurkkatki1, (self.x,self.y))
            elif self.eluCount == 2:
                aken.blit(self.nurkkatki2, (self.x,self.y))
            elif self.eluCount == 3:
                aken.blit(self.nurkkatki3, (self.x,self.y))
        self.hitbox = (self.x, self.y,24,24)
        #pygame.draw.rect(aken, (255,0,0), self.hitbox,2)
        
    def sainpihta(self):
        self.eluCount += 1

#PAREMNURK
class nurkparem():
    nurkterve = (pygame.image.load("kolmnurkp1.png"))
    nurkkatki1 = (pygame.image.load("kolmnurkp2.png"))
    nurkkatki2 = (pygame.image.load("kolmnurkp3.png"))
    nurkkatki3 = (pygame.image.load("kolmnurkp4.png"))
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.eluCount = 0
        self.hitbox = (self.x, self.y,24,24)
        
    def draw(self,aken):
        if self.eluCount == 0:
            aken.blit(self.nurkterve, (self.x, self.y))
        else:
            if self.eluCount == 1:
                aken.blit(self.nurkkatki1, (self.x,self.y))
            elif self.eluCount == 2:
                aken.blit(self.nurkkatki2, (self.x,self.y))
            elif self.eluCount == 3:
                aken.blit(self.nurkkatki3, (self.x,self.y))
        self.hitbox = (self.x, self.y,24,24)
        #pygame.draw.rect(aken, (255,0,0), self.hitbox,2)
        
    def sainpihta(self):
        self.eluCount += 1

#MAJAD
def joonistamajad():
    maja1_1.draw(aken)
    maja1_2.draw(aken)
    maja1_3.draw(aken)
    maja1_4.draw(aken)
    maja1_5.draw(aken)
    maja1_6.draw(aken)
    maja1_7.draw(aken)
    maja1_8.draw(aken)
    nurkvasak1.draw(aken)
    nurkparem1.draw(aken)
    maja2_1.draw(aken)
    maja2_2.draw(aken)
    maja2_3.draw(aken)
    maja2_4.draw(aken)
    maja2_5.draw(aken)
    maja2_6.draw(aken)
    maja2_7.draw(aken)
    maja2_8.draw(aken)
    nurkvasak2.draw(aken)
    nurkparem2.draw(aken)
    maja3_1.draw(aken)
    maja3_2.draw(aken)
    maja3_3.draw(aken)
    maja3_4.draw(aken)
    maja3_5.draw(aken)
    maja3_6.draw(aken)
    maja3_7.draw(aken)
    maja3_8.draw(aken)
    nurkvasak3.draw(aken)
    nurkparem3.draw(aken)
    maja4_1.draw(aken)
    maja4_2.draw(aken)
    maja4_3.draw(aken)
    maja4_4.draw(aken)
    maja4_5.draw(aken)
    maja4_6.draw(aken)
    maja4_7.draw(aken)
    maja4_8.draw(aken)
    nurkvasak4.draw(aken)
    nurkparem4.draw(aken)
            

#NÄHTAV OSA MÄNGUST
def joonista():
    aken.fill((0,0,0)) #et tal saba järgi ei jääks
    aken.blit(laev, (roheline.x, roheline.y))
    joonistamajad()
    for bullet in bullets:
        bullet.draw(aken) #joonista kuul aknale
    
    pygame.display.update()

#MAINLOOP
roheline = mangija(400, 500, 64, 64)
maja1_1 = klots(50,450,25,25)
maja1_2 = klots(50,425,25,25)
maja1_3 = klots(50,400,25,25)
maja1_4 = klots(75,400,25,25)
maja1_5 = klots(100,400,25,25)
maja1_6 = klots(125,400,25,25)
maja1_7 = klots(125,425,25,25)
maja1_8 = klots(125,450,25,25)
nurkvasak1 = nurkvasak(75,425,25,25)
nurkparem1 = nurkparem(100,425,25,25)

maja2_1 = klots(250,450,25,25)
maja2_2 = klots(250,425,25,25)
maja2_3 = klots(250,400,25,25)
maja2_4 = klots(275,400,25,25)
maja2_5 = klots(300,400,25,25)
maja2_6 = klots(325,400,25,25)
maja2_7 = klots(325,425,25,25)
maja2_8 = klots(325,450,25,25)
nurkvasak2 = nurkvasak(275,425,25,25)
nurkparem2 = nurkparem(300,425,25,25)

maja3_1 = klots(450,450,25,25)
maja3_2 = klots(450,425,25,25)
maja3_3 = klots(450,400,25,25)
maja3_4 = klots(475,400,25,25)
maja3_5 = klots(500,400,25,25)
maja3_6 = klots(525,400,25,25)
maja3_7 = klots(525,425,25,25)
maja3_8 = klots(525,450,25,25)
nurkvasak3 = nurkvasak(475,425,25,25)
nurkparem3 = nurkparem(500,425,25,25)

maja4_1 = klots(650,450,25,25)
maja4_2 = klots(650,425,25,25)
maja4_3 = klots(650,400,25,25)
maja4_4 = klots(675,400,25,25)
maja4_5 = klots(700,400,25,25)
maja4_6 = klots(725,400,25,25)
maja4_7 = klots(725,425,25,25)
maja4_8 = klots(725,450,25,25)
nurkvasak4 = nurkvasak(675,425,25,25)
nurkparem4 = nurkparem(700,425,25,25)

bullets = []

run = True #alustab loopi
while run: #kui loop käib:
    pygame.time.delay(20) #et liiga kiiresti ei liiguks
    #python hakkab vaatama kas mingi event toimub
    for event in pygame.event.get(): #võtab kõik asjad mis juhtuvad ja hakkab vaatama kas need juhtuvad
        if event.type == pygame.QUIT: #kui vajutatakse risti:
            run = False #loop läheb kinni, see skript lõpeb
             
    #TULISTAMINE
    for bullet in bullets:
        #kui lastava bloki eluCount on väiksem kui 4(ehk ta on veel elus) JA kuul
        #puudutab bloki hitboxi, siis saab blokk pihta ja kuul läheb katki
        #1 maja
        if maja1_1.eluCount < 4 and bullet.y - bullet.radius < maja1_1.hitbox[1] + maja1_1.hitbox[3] and bullet.y + bullet.radius > maja1_1.hitbox[1]:
            if bullet.x + bullet.radius > maja1_1.hitbox[0] and bullet.x - bullet.radius < maja1_1.hitbox[0] + maja1_1.hitbox[2]:
                maja1_1.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_2.eluCount < 4 and bullet.y - bullet.radius < maja1_2.hitbox[1] + maja1_2.hitbox[3] and bullet.y + bullet.radius > maja1_2.hitbox[1]:
            if bullet.x + bullet.radius > maja1_2.hitbox[0] and bullet.x - bullet.radius < maja1_2.hitbox[0] + maja1_2.hitbox[2]:
                maja1_2.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_3.eluCount < 4 and bullet.y - bullet.radius < maja1_3.hitbox[1] + maja1_3.hitbox[3] and bullet.y + bullet.radius > maja1_3.hitbox[1]:
            if bullet.x + bullet.radius > maja1_3.hitbox[0] and bullet.x - bullet.radius < maja1_3.hitbox[0] + maja1_3.hitbox[2]:
                maja1_3.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_4.eluCount < 4 and bullet.y - bullet.radius < maja1_4.hitbox[1] + maja1_4.hitbox[3] and bullet.y + bullet.radius > maja1_4.hitbox[1]:
            if bullet.x + bullet.radius > maja1_4.hitbox[0] and bullet.x - bullet.radius < maja1_4.hitbox[0] + maja1_4.hitbox[2]:
                maja1_4.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_5.eluCount < 4 and bullet.y - bullet.radius < maja1_5.hitbox[1] + maja1_5.hitbox[3] and bullet.y + bullet.radius > maja1_5.hitbox[1]:
            if bullet.x + bullet.radius > maja1_5.hitbox[0] and bullet.x - bullet.radius < maja1_5.hitbox[0] + maja1_5.hitbox[2]:
                maja1_5.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_6.eluCount < 4 and bullet.y - bullet.radius < maja1_6.hitbox[1] + maja1_6.hitbox[3] and bullet.y + bullet.radius > maja1_6.hitbox[1]:
            if bullet.x + bullet.radius > maja1_6.hitbox[0] and bullet.x - bullet.radius < maja1_6.hitbox[0] + maja1_6.hitbox[2]:
                maja1_6.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_7.eluCount < 4 and bullet.y - bullet.radius < maja1_7.hitbox[1] + maja1_7.hitbox[3] and bullet.y + bullet.radius > maja1_7.hitbox[1]:
            if bullet.x + bullet.radius > maja1_7.hitbox[0] and bullet.x - bullet.radius < maja1_7.hitbox[0] + maja1_7.hitbox[2]:
                maja1_7.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja1_8.eluCount < 4 and bullet.y - bullet.radius < maja1_8.hitbox[1] + maja1_8.hitbox[3] and bullet.y + bullet.radius > maja1_8.hitbox[1]:
            if bullet.x + bullet.radius > maja1_8.hitbox[0] and bullet.x - bullet.radius < maja1_8.hitbox[0] + maja1_8.hitbox[2]:
                maja1_8.sainpihta()
                bullets.pop(bullets.index(bullet))
        #2 maja
        if maja2_1.eluCount < 4 and bullet.y - bullet.radius < maja2_1.hitbox[1] + maja2_1.hitbox[3] and bullet.y + bullet.radius > maja2_1.hitbox[1]:
            if bullet.x + bullet.radius > maja2_1.hitbox[0] and bullet.x - bullet.radius < maja2_1.hitbox[0] + maja2_1.hitbox[2]:
                maja2_1.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_2.eluCount < 4 and bullet.y - bullet.radius < maja2_2.hitbox[1] + maja2_2.hitbox[3] and bullet.y + bullet.radius > maja2_2.hitbox[1]:
            if bullet.x + bullet.radius > maja2_2.hitbox[0] and bullet.x - bullet.radius < maja2_2.hitbox[0] + maja2_2.hitbox[2]:
                maja2_2.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_3.eluCount < 4 and bullet.y - bullet.radius < maja2_3.hitbox[1] + maja2_3.hitbox[3] and bullet.y + bullet.radius > maja2_3.hitbox[1]:
            if bullet.x + bullet.radius > maja2_3.hitbox[0] and bullet.x - bullet.radius < maja2_3.hitbox[0] + maja2_3.hitbox[2]:
                maja2_3.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_4.eluCount < 4 and bullet.y - bullet.radius < maja2_4.hitbox[1] + maja2_4.hitbox[3] and bullet.y + bullet.radius > maja2_4.hitbox[1]:
            if bullet.x + bullet.radius > maja2_4.hitbox[0] and bullet.x - bullet.radius < maja2_4.hitbox[0] + maja2_4.hitbox[2]:
                maja2_4.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_5.eluCount < 4 and bullet.y - bullet.radius < maja2_5.hitbox[1] + maja2_5.hitbox[3] and bullet.y + bullet.radius > maja2_5.hitbox[1]:
            if bullet.x + bullet.radius > maja2_5.hitbox[0] and bullet.x - bullet.radius < maja2_5.hitbox[0] + maja2_5.hitbox[2]:
                maja2_5.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_6.eluCount < 4 and bullet.y - bullet.radius < maja2_6.hitbox[1] + maja2_6.hitbox[3] and bullet.y + bullet.radius > maja2_6.hitbox[1]:
            if bullet.x + bullet.radius > maja2_6.hitbox[0] and bullet.x - bullet.radius < maja2_6.hitbox[0] + maja2_6.hitbox[2]:
                maja2_6.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_7.eluCount < 4 and bullet.y - bullet.radius < maja2_7.hitbox[1] + maja2_7.hitbox[3] and bullet.y + bullet.radius > maja2_7.hitbox[1]:
            if bullet.x + bullet.radius > maja2_7.hitbox[0] and bullet.x - bullet.radius < maja2_7.hitbox[0] + maja2_7.hitbox[2]:
                maja2_7.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja2_8.eluCount < 4 and bullet.y - bullet.radius < maja2_8.hitbox[1] + maja2_8.hitbox[3] and bullet.y + bullet.radius > maja2_8.hitbox[1]:
            if bullet.x + bullet.radius > maja2_8.hitbox[0] and bullet.x - bullet.radius < maja2_8.hitbox[0] + maja2_8.hitbox[2]:
                maja2_8.sainpihta()
                bullets.pop(bullets.index(bullet))
                
        #3 maja
        if maja3_1.eluCount < 4 and bullet.y - bullet.radius < maja3_1.hitbox[1] + maja3_1.hitbox[3] and bullet.y + bullet.radius > maja3_1.hitbox[1]:
            if bullet.x + bullet.radius > maja3_1.hitbox[0] and bullet.x - bullet.radius < maja3_1.hitbox[0] + maja3_1.hitbox[2]:
                maja3_1.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_2.eluCount < 4 and bullet.y - bullet.radius < maja3_2.hitbox[1] + maja3_2.hitbox[3] and bullet.y + bullet.radius > maja3_2.hitbox[1]:
            if bullet.x + bullet.radius > maja3_2.hitbox[0] and bullet.x - bullet.radius < maja3_2.hitbox[0] + maja3_2.hitbox[2]:
                maja3_2.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_3.eluCount < 4 and bullet.y - bullet.radius < maja3_3.hitbox[1] + maja3_3.hitbox[3] and bullet.y + bullet.radius > maja3_3.hitbox[1]:
            if bullet.x + bullet.radius > maja3_3.hitbox[0] and bullet.x - bullet.radius < maja3_3.hitbox[0] + maja3_3.hitbox[2]:
                maja3_3.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_4.eluCount < 4 and bullet.y - bullet.radius < maja3_4.hitbox[1] + maja3_4.hitbox[3] and bullet.y + bullet.radius > maja3_4.hitbox[1]:
            if bullet.x + bullet.radius > maja3_4.hitbox[0] and bullet.x - bullet.radius < maja3_4.hitbox[0] + maja3_4.hitbox[2]:
                maja3_4.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_5.eluCount < 4 and bullet.y - bullet.radius < maja3_5.hitbox[1] + maja3_5.hitbox[3] and bullet.y + bullet.radius > maja3_5.hitbox[1]:
            if bullet.x + bullet.radius > maja3_5.hitbox[0] and bullet.x - bullet.radius < maja3_5.hitbox[0] + maja3_5.hitbox[2]:
                maja3_5.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_6.eluCount < 4 and bullet.y - bullet.radius < maja3_6.hitbox[1] + maja3_6.hitbox[3] and bullet.y + bullet.radius > maja3_6.hitbox[1]:
            if bullet.x + bullet.radius > maja3_6.hitbox[0] and bullet.x - bullet.radius < maja3_6.hitbox[0] + maja3_6.hitbox[2]:
                maja3_6.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_7.eluCount < 4 and bullet.y - bullet.radius < maja3_7.hitbox[1] + maja3_7.hitbox[3] and bullet.y + bullet.radius > maja3_7.hitbox[1]:
            if bullet.x + bullet.radius > maja3_7.hitbox[0] and bullet.x - bullet.radius < maja3_7.hitbox[0] + maja3_7.hitbox[2]:
                maja3_7.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja3_8.eluCount < 4 and bullet.y - bullet.radius < maja3_8.hitbox[1] + maja3_8.hitbox[3] and bullet.y + bullet.radius > maja3_8.hitbox[1]:
            if bullet.x + bullet.radius > maja3_8.hitbox[0] and bullet.x - bullet.radius < maja3_8.hitbox[0] + maja3_8.hitbox[2]:
                maja3_8.sainpihta()
                bullets.pop(bullets.index(bullet))
                
        #4 maja
        if maja4_1.eluCount < 4 and bullet.y - bullet.radius < maja4_1.hitbox[1] + maja4_1.hitbox[3] and bullet.y + bullet.radius > maja4_1.hitbox[1]:
            if bullet.x + bullet.radius > maja4_1.hitbox[0] and bullet.x - bullet.radius < maja4_1.hitbox[0] + maja4_1.hitbox[2]:
                maja4_1.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_2.eluCount < 4 and bullet.y - bullet.radius < maja4_2.hitbox[1] + maja4_2.hitbox[3] and bullet.y + bullet.radius > maja4_2.hitbox[1]:
            if bullet.x + bullet.radius > maja4_2.hitbox[0] and bullet.x - bullet.radius < maja4_2.hitbox[0] + maja4_2.hitbox[2]:
                maja4_2.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_3.eluCount < 4 and bullet.y - bullet.radius < maja4_3.hitbox[1] + maja4_3.hitbox[3] and bullet.y + bullet.radius > maja4_3.hitbox[1]:
            if bullet.x + bullet.radius > maja4_3.hitbox[0] and bullet.x - bullet.radius < maja4_3.hitbox[0] + maja4_3.hitbox[2]:
                maja4_3.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_4.eluCount < 4 and bullet.y - bullet.radius < maja4_4.hitbox[1] + maja4_4.hitbox[3] and bullet.y + bullet.radius > maja4_4.hitbox[1]:
            if bullet.x + bullet.radius > maja4_4.hitbox[0] and bullet.x - bullet.radius < maja4_4.hitbox[0] + maja4_4.hitbox[2]:
                maja4_4.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_5.eluCount < 4 and bullet.y - bullet.radius < maja4_5.hitbox[1] + maja4_5.hitbox[3] and bullet.y + bullet.radius > maja4_5.hitbox[1]:
            if bullet.x + bullet.radius > maja4_5.hitbox[0] and bullet.x - bullet.radius < maja4_5.hitbox[0] + maja4_5.hitbox[2]:
                maja4_5.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_6.eluCount < 4 and bullet.y - bullet.radius < maja4_6.hitbox[1] + maja4_6.hitbox[3] and bullet.y + bullet.radius > maja4_6.hitbox[1]:
            if bullet.x + bullet.radius > maja4_6.hitbox[0] and bullet.x - bullet.radius < maja4_6.hitbox[0] + maja4_6.hitbox[2]:
                maja4_6.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_7.eluCount < 4 and bullet.y - bullet.radius < maja4_7.hitbox[1] + maja4_7.hitbox[3] and bullet.y + bullet.radius > maja4_7.hitbox[1]:
            if bullet.x + bullet.radius > maja4_7.hitbox[0] and bullet.x - bullet.radius < maja4_7.hitbox[0] + maja4_7.hitbox[2]:
                maja4_7.sainpihta()
                bullets.pop(bullets.index(bullet))
        if maja4_8.eluCount < 4 and bullet.y - bullet.radius < maja4_8.hitbox[1] + maja4_8.hitbox[3] and bullet.y + bullet.radius > maja4_8.hitbox[1]:
            if bullet.x + bullet.radius > maja4_8.hitbox[0] and bullet.x - bullet.radius < maja4_8.hitbox[0] + maja4_8.hitbox[2]:
                maja4_8.sainpihta()
                bullets.pop(bullets.index(bullet))
                
        
        #esimese maja nurgad     
        if nurkvasak1.eluCount < 4 and bullet.y - bullet.radius < nurkvasak1.hitbox[1] + nurkvasak1.hitbox[3] and bullet.y + bullet.radius > nurkvasak1.hitbox[1]:
            if bullet.x + bullet.radius > nurkvasak1.hitbox[0] and bullet.x - bullet.radius < nurkvasak1.hitbox[0] + nurkvasak1.hitbox[2]:
                nurkvasak1.sainpihta()
        if nurkparem1.eluCount < 4 and bullet.y - bullet.radius < nurkparem1.hitbox[1] + nurkparem1.hitbox[3] and bullet.y + bullet.radius > nurkparem1.hitbox[1]:
            if bullet.x + bullet.radius > nurkparem1.hitbox[0] and bullet.x - bullet.radius < nurkparem1.hitbox[0] + nurkparem1.hitbox[2]:
                nurkparem1.sainpihta()
                bullets.pop(bullets.index(bullet))
        #teise maja nurgad     
        if nurkvasak2.eluCount < 4 and bullet.y - bullet.radius < nurkvasak2.hitbox[1] + nurkvasak2.hitbox[3] and bullet.y + bullet.radius > nurkvasak2.hitbox[1]:
            if bullet.x + bullet.radius > nurkvasak2.hitbox[0] and bullet.x - bullet.radius < nurkvasak2.hitbox[0] + nurkvasak2.hitbox[2]:
                nurkvasak2.sainpihta()
                bullets.pop(bullets.index(bullet))
        if nurkparem2.eluCount < 4 and bullet.y - bullet.radius < nurkparem2.hitbox[1] + nurkparem2.hitbox[3] and bullet.y + bullet.radius > nurkparem2.hitbox[1]:
            if bullet.x + bullet.radius > nurkparem2.hitbox[0] and bullet.x - bullet.radius < nurkparem2.hitbox[0] + nurkparem2.hitbox[2]:
                nurkparem2.sainpihta()
                bullets.pop(bullets.index(bullet))
        #kolmanda maja nurgad
        if nurkvasak3.eluCount < 4 and bullet.y - bullet.radius < nurkvasak3.hitbox[1] + nurkvasak3.hitbox[3] and bullet.y + bullet.radius > nurkvasak3.hitbox[1]:
            if bullet.x + bullet.radius > nurkvasak3.hitbox[0] and bullet.x - bullet.radius < nurkvasak3.hitbox[0] + nurkvasak3.hitbox[2]:
                nurkvasak3.sainpihta()
                bullets.pop(bullets.index(bullet))       
        if nurkparem3.eluCount < 4 and bullet.y - bullet.radius < nurkparem3.hitbox[1] + nurkparem3.hitbox[3] and bullet.y + bullet.radius > nurkparem3.hitbox[1]:
            if bullet.x + bullet.radius > nurkparem3.hitbox[0] and bullet.x - bullet.radius < nurkparem3.hitbox[0] + nurkparem3.hitbox[2]:
                nurkparem3.sainpihta()
                bullets.pop(bullets.index(bullet))
        #neljanda maja nurgad
        if nurkvasak4.eluCount < 4 and bullet.y - bullet.radius < nurkvasak4.hitbox[1] + nurkvasak4.hitbox[3] and bullet.y + bullet.radius > nurkvasak4.hitbox[1]:
            if bullet.x + bullet.radius > nurkvasak4.hitbox[0] and bullet.x - bullet.radius < nurkvasak4.hitbox[0] + nurkvasak4.hitbox[2]:
                nurkvasak4.sainpihta()
                bullets.pop(bullets.index(bullet))
        if nurkparem4.eluCount < 4 and bullet.y - bullet.radius < nurkparem4.hitbox[1] + nurkparem4.hitbox[3] and bullet.y + bullet.radius > nurkparem4.hitbox[1]:
            if bullet.x + bullet.radius > nurkparem4.hitbox[0] and bullet.x - bullet.radius < nurkparem4.hitbox[0] + nurkparem4.hitbox[2]:
                nurkparem4.sainpihta()
                bullets.pop(bullets.index(bullet))
                
        
        if bullet.y < 600 and bullet.y > 0: #kui kuuli y on vähem kui 600 aga rohkem kui 0 (ehk ta ei ole aknast väljas) siis:
            #kuul liigub
            bullet.y -= bullet.vel
        else: #kui kuul on aknast väljas, kaob kuul
            bullets.pop(bullets.index(bullet))
            
    #LIIKUMINE
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and roheline.x > roheline.vel: #kui vajutatakse vasakut noolt:
        roheline.x -= roheline.vel #lahutatakse x-kordinaadilt vel muutuja ja laev liigub vasakule
    if keys[pygame.K_RIGHT] and roheline.x < 720:
        roheline.x += roheline.vel #liidetakse x-kordinaadile vel muutuja ja laev liigub paremale

    if keys[pygame.K_SPACE]: #kui vajutatakse tühikut:
        if len(bullets) == 0: #kui ekraanil on 0 kuuli (see on selleks, et ekraanil oleks alati ainult 1 kuul)
            bullets.append(projectile(round(roheline.x + roheline.width //2), round(roheline.y + roheline.height//2 -20), 5, (VALGE)))
            tulistamine.play()
    
    joonista() #joonistab mängu
    
pygame.quit() #paneb akna kinni (kui risti vajutatakse)