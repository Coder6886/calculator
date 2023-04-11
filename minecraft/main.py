import pygame
import perlin
import random
import time
import math
class graphicsclass():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([48*19,48*19])
        self.steveimg = pygame.image.load('steve.png')
        self.grassblockimg = pygame.image.load('grass_block.png')
        self.dirtimg = pygame.image.load('dirt.png')
        self.iron_oreimg = pygame.image.load('iron_ore.png')
        self.stoneimg = pygame.image.load('stone.png')
        self.stillwaterimg = pygame.image.load('still_water.png')
        self.flowingwaterimg = pygame.image.load('flowing_water.png')
        self.sandimg = pygame.image.load('sand.png')
        self.coalimg = pygame.image.load('coal_ore.png')
        self.oakimg = pygame.image.load('oak.png')
        self.leavesimg = pygame.image.load('leaves.png')
        self.tallgrassimg = pygame.image.load('tall_grass.png')
        self.poppyimg = pygame.image.load('poppy.png')
        self.dandelionimg = pygame.image.load('dandelion.png')
        self.cornflowerimg = pygame.image.load('cornflower.png')
        self.inventorybackground = pygame.image.load('inventory_background.png')
        self.opencraftimg = pygame.image.load('open_craft.png')
        self.imgs = [pygame.transform.scale(self.steveimg,(48,48)),\
                     pygame.transform.scale(self.grassblockimg,(48,48)),\
                     pygame.transform.scale(self.dirtimg,(48,48)),\
                     pygame.transform.scale(self.iron_oreimg,(48,48)),\
                     pygame.transform.scale(self.stoneimg,(48,48)),\
                     pygame.transform.scale(self.stillwaterimg,(48,48)),\
                     pygame.transform.scale(self.flowingwaterimg,(48,48)),\
                     pygame.transform.scale(self.sandimg,(48,48)),\
                     pygame.transform.scale(self.coalimg,(48,48)),\
                     pygame.transform.scale(self.oakimg,(48,48)),\
                     pygame.transform.scale(self.leavesimg,(48,48)),\
                     pygame.transform.scale(self.tallgrassimg,(48,48)),\
                     pygame.transform.scale(self.poppyimg,(48,48)),\
                     pygame.transform.scale(self.dandelionimg,(48,48)),\
                     pygame.transform.scale(self.cornflowerimg,(48,48)),\
                     pygame.transform.scale(self.inventorybackground,(48,48)),\
                     pygame.transform.scale(self.opencraftimg,(48,48))]
    def paste(self,x,y,imgtype,box = False,boxaround = (0,0,0)):
        self.screen.blit(self.imgs[imgtype],(x*48,y*48))
        if box:
            pygame.draw.rect(self.screen,boxaround,pygame.Rect(x*48,y*48,48,48),2)
    def flip(self):
        pygame.display.flip()
    def fill(self,r=255,g=255,b=255):
        self.screen.fill([r, g, b])
    def gameover(self):
        pass
    def draw_transparent_rect(self,place,color,transparency):
        rectimg = pygame.Surface((48,48))
        rectimg.set_alpha(transparency)
        pygame.draw.rect(rectimg,color,rectimg.get_rect(),48)
        self.screen.blit(rectimg,place)
    def morphtwocolors(self,color1,color2,t):
        return (color1[0]*(1-t)+color2[0]*t,\
                color1[1]*(1-t)+color2[1]*t,\
                color1[2]*(1-t)+color2[2]*t)
    def rendersky(self,gametime):
        #sun render from 5.5 to 19.5
##        angle = (gametime-5.5)/(19.5-5.5)*math.pi
##        if 5.5<=gametime < 9:
##            sunposx,sunposy = 0,math.ceil(9-math.tan(angle)*19)*48
##            self.draw_transparent_rect((sunposx,sunposy),(255,255,255),200)
##        elif 16<=gametime < 19.5:
##            sunposx,sunposy = 18*48,math.ceil(19*48-math.tan(angle)*19)*48
##            self.draw_transparent_rect((sunposx,sunposy),(255,255,255),200)
        for i in range(19):
            for j in range(19):
                if gametime < 5.5 or gametime >= 19.5:
                    self.draw_transparent_rect((i*48,j*48),(19,24,98),150)
                if gametime >= 5.5 and gametime < 6:
                    self.draw_transparent_rect((i*48,j*48),self.morphtwocolors((19,24,98),(255,129,0),(gametime-5.5)*2),150)
                if gametime >= 6 and gametime < 6.5:
                    self.draw_transparent_rect((i*48,j*48),self.morphtwocolors((255,129,0),(165,229,255),(gametime-6)*2),150*(6.5-gametime)*2)
                if gametime >= 18.5 and gametime < 19:
                    self.draw_transparent_rect((i*48,j*48),self.morphtwocolors((165,229,255),(255,129,0),(gametime-18.5)*2),150*(19-gametime)*2)
                if gametime >= 19 and gametime < 19.5:
                    self.draw_transparent_rect((i*48,j*48),self.morphtwocolors((255,129,0),(19,24,98),(gametime-19)*2),150)
class playerclass():
    def __init__(self,playerx,playery):
        global landsize, worldheight, landscape,waterscape
        self.playerx = playerx
        self.playery = playery
        self.jump = -1.0
        self.jumppause = -1.0
        self.runforwardcnt = -1.0
        self.runbackwardcnt = -1
        self.waterdrop = 0
        self.inventory = [1,2,4,5,7,9,10,11,12,13]
        self.inventory_selected = 0
        self.crafting = False
    def placeblock(self,blocktype,a,b):
        foreground_blocks = [11,12,13,14]
        if a >= 0 and a < worldheight and b >= 0 and b < landsize:
            if blocktype in foreground_blocks:
                if foreground[a][b] == -1:
                    foreground[a][b] = blocktype
            elif blocktype == 5 and waterscape[a][b] == -1 and landscape[a][b] == -1:
                waterscape[a][b] = 5
            else:
                if landscape[a][b] == -1:
                    landscape[a][b] = blocktype
                    waterscape[a][b] = -1
                    foreground[a][b] = -1
                
    def update(self,keys):
        
        landscape[self.playerx][self.playery] = -1
        if not self.crafting:
            if keys[97]:
                # time.time()-self.runforw/backwardcnt is the run pause
                if self.ok(self.playerx,self.playery-1) and time.time()-self.runforwardcnt > 0.15:
                    self.playery -= 1
                    self.runforwardcnt = time.time()
            else:
                self.runforwardcnt = -1.0
            if keys[100]:
                if self.ok(self.playerx,self.playery+1) and time.time()-self.runbackwardcnt > 0.15:
                    self.playery += 1
                    self.runbackwardcnt = time.time()
            else:
                self.runbackwardcnt = -1.0
        if self.jump > 0 and time.time() - self.jump > 0.3:
            self.jump = -1.0
            self.jumppause = time.time()
        #self.jumppause is the pause between jumps
        if not self.crafting:
            if keys[32] and time.time()-self.jumppause > 0.2 and self.jump < 0\
               and self.ok(self.playerx-1,self.playery) and not self.ok(self.playerx+1,self.playery):
                self.jump = time.time()
                self.playerx -= 1
                if self.ok(self.playerx-1,self.playery):
                    self.playerx -= 1
        self.drop()
        landscape[self.playerx][self.playery] = 0
    def ok(self,x,y):
        if x >= 0 and x < worldheight and y >= 0 and y < landsize and landscape[x][y] == -1:
            return True
        return False
    def click(self,changetype):
        y,x=pygame.mouse.get_pos()
        
        x = x//48
        y = y//48
        
        x -= 9
        y -= 9
        a = x+self.playerx
        b = y+self.playery
        if changetype == 3:#right click
            #placing blocks must have non-player blocks around
            if a >= 0 and a < worldheight and b >= 0 and b <= landsize\
               and (a+1 < worldheight and landscape[a+1][b] > 0 or \
                    a-1 >= 0 and landscape[a-1][b] > 0 or \
                    b+1 < landsize and landscape[a][b+1] > 0 or \
                    b-1 >= 0 and landscape[a][b-1] > 0)\
               and self.crafting == False:
                self.placeblock(self.inventory[self.inventory_selected],a,b)
        elif changetype== 1:#left click
            if x+9 == 18 and y+9>= 4 and y+9 <= 14:
                if y+9-4 < 10:
                    self.inventory_selected=y+9-4
                    #print("aaa")
                else:
                    self.crafting ^= 1
            elif a >= 0 and a < worldheight and b >= 0 and b < landsize:
                if self.crafting == False:
                    if foreground[a][b] != -1:
                        foreground[a][b] = -1
                    elif landscape[a][b] != -1:
                        landscape[a][b] = -1
                    elif waterscape[a][b] != -1:
                        waterscape[a][b] = -1
        elif changetype == 2:#debug
            print(waterscape[a][b],landscape[a][b],foreground[a][b])
    def drop(self):
        if self.waterdrop:
            self.waterdrop-=1
        if self.jump < 0 and self.waterdrop == 0:
            if not waterscape[self.playerx][self.playery]<0:
                self.waterdrop = 5
            if self.ok(self.playerx+2,self.playery) and self.ok(self.playerx+1,self.playery)and waterscape[self.playerx][self.playery]<0:
                self.playerx += 2
            elif self.ok(self.playerx+1,self.playery) :
                self.playerx += 1
def watersim():
    global landsize, worldheight, landscape,waterscape
    for i in range(worldheight):
        for j in range(landsize):
            waterscapeold[i][j] = waterscape[i][j]
    for i in range(worldheight-1,-1,-1):
        for j in range(landsize):
            if waterscape[i][j] >= 0 :
                if i+1 < worldheight and landscape[i+1][j] <0 and waterscape[i+1][j] != 5:
                    waterscape[i+1][j] = 6
                else:
                    if j+1 < landsize and waterscapeold[i][j+1] < 0 and landscape[i][j+1] < 0:
                        waterscape[i][j+1] = 6
                    elif j-1 >= 0 and waterscapeold[i][j-1] < 0 and landscape[i][j-1] < 0:
                        waterscape[i][j-1] = 6
                    else:
                        waterscape[i][j] = 5
Graphics = graphicsclass()
noiseperlin = perlin.perlin(0.18,1,2,5,10)
worldheight = 255
landsize = len(noiseperlin)
landscape = []#blocks
waterscape = []#water
waterscapeold = []
foreground = []#shrubs,grass,flowers etc.
def worldgeneration():
    sealevel = 105
    coallevel = 5
    ironlevel = 10
    coalprob = 0.1
    ironprob = 0.05
    treeprob = 0.08
    grassprob = 0.09
    poppyprob = 0.08
    cornflowerprob = 0.1
    dandelionprob = 0.1
    for i in range(worldheight):
        landscape.append([])
        waterscape.append([])
        waterscapeold.append([])
        foreground.append([])
        for j in range(landsize):
            # make rough landscape and water
            waterscape[i].append(-1)
            waterscapeold[i].append(-1)
            foreground[i].append(-1)
            perlinvalue = math.ceil(noiseperlin[j]*100)
            if i < perlinvalue:
                landscape[i].append(-1)
                if i > sealevel:
                    waterscape[i][j]=5
                    waterscapeold[i][j]=5 
            elif i -1 < perlinvalue:
                landscape[i].append(1)
            elif i-3<perlinvalue:
                landscape[i].append(2)
            else:
                landscape[i].append(4)
            # generate ore
            if i > perlinvalue+coallevel and random.random() < coalprob:
                landscape[i][j] = 8
            if i > perlinvalue+ironlevel and random.random() < ironprob:
                landscape[i][j] = 3
    for i in range(sealevel+1,worldheight):
        for j in range(landsize):
            # make sand
            if landscape[i][j] != -1:
                if j+2 < landsize and waterscape[i][j+2] == 5:
                    landscape[i][j] = 7
                elif j+1 < landsize and waterscape[i][j+1] == 5:
                    landscape[i][j] = 7
                elif j-1 >= 0 and waterscape[i][j-1] == 5:
                    landscape[i][j] = 7
                elif j-2 >= 0 and waterscape[i][j-2] == 5:
                    landscape[i][j] = 7
                elif waterscape[i-1][j] == 5:
                    landscape[i][j] = 7
    for i in range(landsize):
        perlinvalue = math.ceil(noiseperlin[i]*100)
        if landscape[perlinvalue][i] == 1 and random.random() < treeprob and perlinvalue-7 >= 0:
            def placeifnothing(x,y,thing):
                if x >= 0 and x < worldheight and y >= 0 and y < landsize and landscape[x][y]==-1:
                    landscape[x][y] = thing
            # make trees(with random noise)
            landscape[perlinvalue][i] = 2
            placeifnothing(perlinvalue-1,i,9)
            placeifnothing(perlinvalue-2,i,9)
            placeifnothing(perlinvalue-3,i,9)
            placeifnothing(perlinvalue-4,i,9)
            placeifnothing(perlinvalue-4,i-1,10)
            placeifnothing(perlinvalue-4,i+1,10)
            if random.random() > 0.5:
                placeifnothing(perlinvalue-4,i-2,10)
            if random.random() > 0.5:
                placeifnothing(perlinvalue-4,i+2,10)
            placeifnothing(perlinvalue-5,i,10)
            placeifnothing(perlinvalue-5,i+1,10)
            placeifnothing(perlinvalue-5,i-1,10)
            placeifnothing(perlinvalue-5,i+2,10)
            placeifnothing(perlinvalue-5,i-2,10)
            placeifnothing(perlinvalue-6,i,10)
            placeifnothing(perlinvalue-6,i+1,10)
            placeifnothing(perlinvalue-6,i-1,10)
            placeifnothing(perlinvalue-6,i+2,10)
            placeifnothing(perlinvalue-6,i-2,10)
            placeifnothing(perlinvalue-7,i,10)
            placeifnothing(perlinvalue-7,i-1,10)
            placeifnothing(perlinvalue-7,i+1,10)
            if random.random() > 0.5:
                placeifnothing(perlinvalue-7,i-2,10)
            if random.random() > 0.5:
                placeifnothing(perlinvalue-7,i+2,10)
    #create flowers,grasses
    for i in range(landsize):
        perlinvalue = math.ceil(noiseperlin[i]*100)
        if perlinvalue-1 >= 0 and landscape[perlinvalue-1][i] == -1 and landscape[perlinvalue][i] == 1:
            if random.random() < grassprob:
                foreground[perlinvalue-1][i] = 11
            elif random.random()<poppyprob:
                foreground[perlinvalue-1][i] = 12
            elif random.random()<dandelionprob:
                foreground[perlinvalue-1][i] = 13
            elif random.random()<cornflowerprob:
                foreground[perlinvalue-1][i] = 14
worldgeneration()
Player =playerclass(0,5)
for i in range(255):
    Player.drop()
#Player.playerx = 254
running = True
watersimtime = -1
gameticks = 9
while running:
    Graphics.fill(165,229,255)
    if time.time()-watersimtime > 0.1:
        watersim()
        watersimtime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Player.click(event.button)
            #print(pygame.key.get_pressed())
    Player.update(pygame.key.get_pressed())
    cursory,cursorx=pygame.mouse.get_pos()
    cursorx = cursorx//48
    cursory = cursory//48
    for i in range(max(0,Player.playery-9),min(Player.playery+10,landsize)):
        for j in range(max(0,Player.playerx-9),min(Player.playerx+10,worldheight)):
            boxFlag = False
            if cursorx == 9-Player.playerx+j and cursory == i-Player.playery+9:
                boxFlag = True
            if waterscape[j][i] != -1:
                Graphics.paste(i-Player.playery+9,9-Player.playerx+j,waterscape[j][i],box=boxFlag)
            if landscape[j][i] != -1:
                Graphics.paste(i-Player.playery+9,9-Player.playerx+j,landscape[j][i],box=boxFlag)
            if foreground[j][i] != -1:
                Graphics.paste(i-Player.playery+9,9-Player.playerx+j,foreground[j][i],box=boxFlag)
    for i in range(4,14):
        Graphics.paste(i,18,15)
        if Player.inventory[i-4] != -1:
            if Player.inventory_selected==i-4:
                Graphics.paste(i,18,Player.inventory[i-4],box=True)
            else:
                Graphics.paste(i,18,Player.inventory[i-4],box=False)
    pygame.draw.rect(Graphics.screen,(202,164,114),pygame.Rect(4*48-1,18*48-1,48*10+1,48+1),2)
    Graphics.paste(14,18,16)
    gameticks += 0.001
    if gameticks >= 24:
        gameticks -= 24
    #Graphics.rendersky(gameticks)
    for i in range(4,14):
        if Player.inventory[i-4] != -1:
            Graphics.flip()
    pygame.time.delay(50)
pygame.quit()
