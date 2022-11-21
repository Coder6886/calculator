import pygame
import perlin
import time
import math
class graphicsclass():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([16*19,16*19])
        self.steveimg = pygame.image.load('steve.png')
        self.grassimg = pygame.image.load('grass.png')
        self.dirtimg = pygame.image.load('dirt.png')
        self.iron_oreimg = pygame.image.load('iron_ore.png')
        self.cobblestoneimg = pygame.image.load('cobblestone.png')
        self.imgs = [self.steveimg,self.grassimg,self.dirtimg,self.iron_oreimg,self.cobblestoneimg]
    def paste(self,x,y,imgtype):
        self.screen.blit(self.imgs[imgtype],(x*16,y*16))
    def flip(self):
        pygame.display.flip()
    def fill(self):
        self.screen.fill([255, 255, 255])
    
            
    def gameover(self):
        pass
class playerclass():
    def __init__(self,playerx,playery):
        global landsize, worldheight, landscape
        self.playerx = playerx
        self.playery = playery
        self.jump = -1.0
    def update(self,keys):
        
        landscape[self.playerx][self.playery] = -1
        if self.jump > 0 and time.time() - self.jump > 0.3:
            self.jump = -1.0
        if keys[32]  and self.jump < 0 and self.ok(self.playerx-1,self.playery) and not self.ok(self.playerx+1,self.playery):
            self.jump = time.time()
            self.playerx -= 1
            if self.ok(self.playerx-1,self.playery):
                self.playerx -= 1
        if keys[97] and self.ok(self.playerx,self.playery-1):
            self.playery -= 1
        if keys[100] and self.ok(self.playerx,self.playery+1):
            self.playery += 1
        self.drop()
        landscape[self.playerx][self.playery] = 0
    def ok(self,x,y):
        if x >= 0 and x < worldheight and y >= 0 and y < landsize and landscape[x][y] == -1:
            return True
        return False
    def change(self,changetype):
        y,x=pygame.mouse.get_pos()
        
        x = x//16
        y = y//16
        
        x -= 9
        y -= 9
        a = x+self.playerx
        b = y+self.playery
        if changetype == 3 and self.ok(a,b):#put blocks
            landscape[a][b] = 1
        elif changetype== 1 and a >= 0 and a < worldheight and b >= 0 and b < landsize and landscape[a][b] != -1:#get blocks
            landscape[a][b] = -1
    def drop(self):
        if self.jump < 0:
            if self.ok(self.playerx+2,self.playery) and self.ok(self.playerx+1,self.playery):
                self.playerx += 2
            elif self.ok(self.playerx+1,self.playery):
                self.playerx += 1
Graphics = graphicsclass()
noiseperlin = perlin.perlin(0.2,1,2,5,10)
worldheight = 255
landsize = len(noiseperlin)
landscape = []
for i in range(worldheight):
    landscape.append([])
    for j in range(landsize):
        if i < math.ceil(noiseperlin[j]*100):
            landscape[i].append(-1)
        elif i -1 < math.ceil(noiseperlin[j]*100) :
            landscape[i].append(1)
        elif i-3<math.ceil(noiseperlin[j]*100):
            landscape[i].append(2)
        else:
            landscape[i].append(4)
Player =playerclass(0,5)
running = True
while running:
    
    Graphics.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Player.change(event.button)
                
            #print(pygame.key.get_pressed())
    Player.update(pygame.key.get_pressed())
    for i in range(max(0,Player.playery-9),min(Player.playery+10,landsize)):
        for j in range(max(0,Player.playerx-9),min(Player.playerx+10,worldheight)):
            if landscape[j][i] != -1:
                Graphics.paste(i-Player.playery+9,9-Player.playerx+j,landscape[j][i])
    Graphics.flip()
    pygame.time.delay(100)
pygame.quit()
