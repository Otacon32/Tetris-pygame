# -*- coding: utf-8 -*-
import pygame, time, threading
#import pygame.mixer
from random import randint
"""
Tetris Party Deluxe war 20x10 bl�cke gro�; Alles �ber 21 ist gameover

"""

pygame.init()
#Farben in RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red=(150,0,0)
green = (0, 255, 0)
dark_green=(0,150,0)
blue = (0, 0, 255)
dark_blue=(0,0,150)
yellow=(255,255,0)
dark_yellow=(150,150,0)
orange = (255,165,0)
dark_orange=(200,90,0) # alt: 255,140,0
purple=(139,0,139)#dark magenta
dark_purple=(75,0,130)#indigo
cyan=(0,255,255)
dark_cyan=(0,150,150)

#-----------------#Position Array#------------------------
posx=[462,512, 562, 612, 662, 712, 762, 812, 862, 912]# 0 Left; 9 Right
posy = [1032, 982, 932, 882, 832, 782, 732, 682, 632, 582, 532, 482, 432, 382, 332, 282, 232, 182, 132, 82, 32, -18, -68, -118, -168, -218, -268, -318, -368] #19 top; 0 bottom
#-----------------#Window Options#-----------------
ScreenInfo = pygame.display.Info()
window_size2 = ((ScreenInfo.current_w, ScreenInfo.current_h))
window_size = (1920, 1080)  #1920, 1080
window = pygame.display.set_mode((window_size2), pygame.FULLSCREEN)
pygame.display.set_caption("Tetris Party remake")
#pygame.display.set_icon(pygame.image.load("./assets/images/icon.png"))
clock = pygame.time.Clock()
#----------------#classes#---------------------------
class grid(): # Grid is more ore less the Playfield where everything is controled (i hope)
    gridCount = 0
    def __init__(self):
        grid.gridCount += 1 #falls 2 spieler drinnen sein wird
        self.array_x = [10]
        self.array_y = [20]
        #if grid.gridCount == 1:
        self.x = 500 #Breite des Spielbereiches Block = 50 breit
        self.y = 1000 # H�he des Spielbereiches Block = 50 Hoch
        self.BlockAlive = False
        self.BlockArray = [[[0 for _ in range(10)] for _ in range(20)] for _ in range(3)] # z;y;x # z[0] = Ture/False werte; z[1] = color; z[2] = dar_color;
        self.activeBlock = None
        self.Hold = None
        self.swapAction = False
    def Grid(self):
        pygame.draw.rect(window, white, [(window_size[0]/2-self.x), (window_size[1]-self.y), self.x, self.y], 2)
        txtOnScreen("Next:",20,(window_size[0]/2+5),(window_size[1]-1000), white)
    def RandomBlock(self):
        BlockTypes = [o_piece, I_piece, L_piece, J_piece, S_piece, Z_piece, T_piece]#0-6
        if self.BlockAlive == False and self.swapAction == False:
            randBox = randint(0,6)
            self.activeBlock = BlockTypes[randBox]() # currentBlock = BlockTypes[randBox]()
            self.BlockAlive = True

        elif self.BlockAlive == False and self.swapAction == True:
            copy = self.Hold
            self.Hold = self.activeBlock
            self.activeBlock = BlockTypes[copy]
            self.swapAction = False
            self.BlockAlive = True

    def getBlocks(self, array, light, dark):
        for y in range(len(array)):
            self.BlockArray[0][array[y][1]][array[y][0]] = True
            self.BlockArray[1][array[y][1]][array[y][0]] = light
            self.BlockArray[2][array[y][1]][array[y][0]] = dark
    def DrawBlocks(self):
        for x in range(10):
            for y in range(20):
                # for z in range(2):
                if self.BlockArray[0][y][x] == True:
                    pygame.draw.rect(window, self.BlockArray[1][y][x],(posx[x], posy[y],50, 50)) # Outer_Box
                    pygame.draw.rect(window, self.BlockArray[2][y][x],(posx[x]+6,posy[y]+6,50-12,50-12)) # Inner_Box
                else:
                    pass
    def MoveLeft(self, currentBlock):
        #move left
        currentBlock.x -= 1
        checkLoop = True 
        for piece in range(len(currentBlock.Blocks)):
            if currentBlock.Blocks[piece][0] <= 0 and checkLoop == True:
                currentBlock.x += 1 
                checkLoop = False
    def MoveRight(self, currentBlock):
        #move right
        currentBlock.x += 1
        checkLoop = True
        for piece in range(len(currentBlock.Blocks)):
            if currentBlock.Blocks[piece][0] >= 9 and checkLoop == True:
                currentBlock.x -= 1 # If its greater as the Grid it places it back
                checkLoop = False
    def Rotate(self, currentBlock):
        #Rotate
        currentBlock.CompasCount += 1
        if currentBlock.CompasCount > 3:
            currentBlock.CompasCount = 0
    def FallenLeaves(self, currentBlock):
        #move Down
        frameCount = 0
        checkLoop = True
        for down in range(currentBlock.y):
            if checkLoop == False:
                break
            elif checkLoop == True:
                currentBlock.Draw() # Need to do this to update the array
                for piece in range(len(currentBlock.Blocks)): # Check if it hits the ground
                    px = currentBlock.Blocks[piece][0]
                    py = currentBlock.Blocks[piece][1]
                    if self.BlockArray[0][py-1][px] == True:
                        self.getBlocks(currentBlock.Blocks, currentBlock.light_color, currentBlock.dark_color)
                        self.BlockAlive = False
                        checkLoop = False
                        # self.BlockArray[0][py][px] = True
                    elif currentBlock.Blocks[piece][1] == 0:
                        checkLoop = False
                currentBlock.y -= 1
    def HitDetection(self, currentBlock):
        checkLoop = True
        for piece in range(len(currentBlock.Blocks)):
            px = currentBlock.Blocks[piece][0]
            py = currentBlock.Blocks[piece][1]
            if checkLoop == False:
                break
            try:
                if self.BlockArray[0][py-1][px] == True:
                    self.getBlocks(currentBlock.Blocks, currentBlock.light_color, currentBlock.dark_color)
                    self.BlockAlive = False
                    checkLoop = False
            except:
                pass
    def SwapHold(self):
        print(self.activeBlock.__class__.__name__)#
        # Randomblock funktion muss vorher in in grid her
        if self.Hold == None:
            copy = self.activeBlock.__class__.__name__
            if copy == "o_piece":
                self.Hold = 0
            elif copy == "I_piece":
                self.Hold = 1
            elif copy == "L_piece":
                self.Hold = 2
            elif copy == "J_piece":
                self.Hold = 3
            elif copy == "S_piece":
                self.Hold = 4
            elif copy == "Z_piece":
                self.Hold = 5
            elif copy == "T_piece":
                self.Hold = 6
            # self.Hold = type(self.activeBlock.__class__.__name__
            self.BlockAlive = False
        else:
            self.BlockAlive = False
            self.swapAction = True
            self.RandomBlock()

    def CheckRows(self):
        YArray = []
        Ycount = 0
        Xchecker = 0
        Xcount = 0
        for y in range(20):
            for x in range(10):
                if self.BlockArray[0][y][x] == True:
                    Xcount += 1
            if Xcount == 10:
                Xcount = 0
                Ycount += 1
                YArray.append(y)
            Xcount = 0
        if Ycount >= 1:
            Ycount = 0
            for y in range(len(YArray)):
                Yint = YArray[y]
                for x in range(10):
                    self.BlockArray[0][Yint][x] = False
                    for y in range(min(YArray), max(YArray)):
                        offset = y + 1
                        copy = self.BlockArray[0][offset]
                        self.BlockArray[0][y] = copy
                        # copy = self.BlockArray[0][y]
                        # self.BlockArray[0][y+1] = copy
            #Let the Blocks drop down...
            """
            Blöcke/Reihe darf erst runter wen unter ihnen kein einziger block befindet
            Wenn komplett leer --> Reihe darf nach unten
            Es muss von unten nach oben abgearbeitet werden. 
            """
            YArray = []
            Xcount = 0
            for y in range(20):
                for x in range(10):
                    if self.BlockArray[0][y][x] == False:
                        Xcount += 1
                        if Xcount == 10:
                            YArray.append(y)
                if Xcount == 10:
                    Xcount = 0
                    for line in YArray:
                        for yy in range(line, 20):
                            #Get Block above
                            copy_block = self.BlockArray[0][yy+1]
                            copy_color_light = self.BlockArray[1][yy+1]
                            copy_color_dark = self.BlockArray[2][yy+1]
                            #Replace empty line with Copy
                            self.BlockArray[0][yy] = copy_block
                            self.BlockArray[1][yy] = copy_color_light
                            self.BlockArray[2][yy] = copy_color_dark
                #Versuch 1
            # for y in range(20):
            #     for x in range(10):
            #         if self.BlockArray[0][y][x] == False:
            #             Xcount += 1
            #             if Xcount == 10:
            #                 YArray.append(y)
            #     if Xcount == 10:
            #         for yy in range(y, 19): #This still need testing!!
            #             #Get Block above
            #             copy_block = self.BlockArray[0][y+1]
            #             copy_color_light = self.BlockArray[1][y+1]
            #             copy_color_dark = self.BlockArray[2][y+1]
            #             #Replace empty line with Copy
            #             self.BlockArray[0][y] = copy_block
            #             self.BlockArray[1][y] = copy_color_light
            #             self.BlockArray[2][y] = copy_color_dark


#Default Spawn Position should be x = 4; y = 22
defaultx = 4
defaulty = 19
#For Oriantation
Compas = ["N", "E", "S", "W"]
class o_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = yellow
        self.dark_color = dark_yellow
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        #Upper Left
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.Blocks[0] = ([self.x, self.y])
        #Lower Left
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        self.Blocks[1] = ([self.x, self.y-1])
        #Upper Right
        pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.Blocks[2] = ([self.x+1, self.y])
        #Lower Right
        pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y-1],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        self.Blocks[3] = ([self.x+1, self.y-1])
    def DelArray(self):
        self.Blocks[:] = []

class I_piece():
    def __init__(self):
        #Still Testing how to rotate blocks the easy way
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = cyan
        self.dark_color = dark_cyan
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y])
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y+1])
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y+2])
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+3],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+3]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y+3])
        def East():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x+2, self.y])
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x+1, self.y])
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y])
        if self.CompasCount == 0 or self.CompasCount == 2:
            North()
        elif self.CompasCount == 1 or self.CompasCount == 3 :
            East()

class L_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = orange
        self.dark_color = dark_orange
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y+2])
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y+1])
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y])
        def East():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x+2, self.y])
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x+1, self.y])
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y-1])
        def South():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-2]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y-2])
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y-1])
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y])
        def West():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-2, self.y])
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x-1, self.y])
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y+1])
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class J_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = blue
        self.dark_color = dark_blue
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y+2])
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y+1])
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y])
        def East():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x+2, self.y])
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x+1, self.y])
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y+1])
        def South():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-2]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y-2])
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y-1])
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y])
        def West():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-2, self.y])
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x-1, self.y])
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y-1])
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class S_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = green
        self.dark_color = dark_green
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x+1, self.y])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y-1])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y-1])
        def East():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y-1])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x-1, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y+1])
        def South():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-1, self.y])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y+1])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y+1])
        def West():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y-1])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x-1, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y+2])
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class Z_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = red
        self.dark_color = dark_red
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-1, self.y])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y-1])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y-1])
        def East():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y+1])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x-1, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y-1])
        def South():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x+1, self.y])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y+1])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y+1])
        def West():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y-1])
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x+1, self.y])
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y+1])
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class T_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = purple
        self.dark_color = dark_purple
        self.Blocks = [[1, 1], [1, 1], [1, 1], [1, 1]] #X; Y
    def Draw(self):
        def North():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-1, self.y])
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x+1, self.y])
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y+1])
        def East():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y+1])
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y-1])
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x+1, self.y])
        def South():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x-1, self.y])
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x+1, self.y])
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x, self.y-1])
        def West():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[0] = ([self.x, self.y+1])
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[1] = ([self.x, self.y])
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[2] = ([self.x, self.y-1])
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            self.Blocks[3] = ([self.x-1, self.y])
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class Musicplayer():
    def __init__(self):
        import pygame.mixer
        pygame.mixer.pre_init(44100, -16, 2, 2048)  #setup mixer to avoid sound lag
        import glob
        self.title = None
        self.state = "stop"
        self.volume = 0.2
        self.Tracks = self.getList
        self.LoadTrack = pygame.mixer.Sound(self.Tracks[self.getRandom()])
        self.LoadTrack.set_volume(self.volume)
        self.getList()
    def getList(self):
        a = glob.glob("./music/*.ogg")
        return a
    def getRandom(self):
        b = len(self.Tracks)
        a = randint(range(0,b))
        return a
    def PlayStop(self):
        if self.state =="stop":
            self.LoadTrack.play()
            self.state = "play"
        elif self.state == "play":
            self.LoadTrack.stop()

#--------------------#Functions#---------------------------

def txtOnScreen(txt,txtsize, x, y, farbe):
    # Display some text
    font = pygame.font.Font("./Ubuntu-R.ttf", txtsize)
    text = font.render(txt, 1, (farbe))
    window.blit(text, (x,y))

def MoveDownTimer(block, Bool):
        Bool = True
        time.sleep(1)
        block.y -= 1
        Bool = False

def menu():
    fps=30
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key is pygame.K_p:
                    main_loop()
        window.fill(white)
        txtOnScreen("Men� Test", 60,(955),(540), blue)
        pygame.display.update()
        clock.tick(fps)

def main_loop():
    p1 = grid()
    fps=60
    frameCount = 0
    run_game = True
    # BlockAlive = False
    Level = 6
    BlockTypes = [o_piece, I_piece, L_piece, J_piece, S_piece, Z_piece, T_piece]#0-6
    #music = Musicplayer()
    while run_game:
        for event in pygame.event.get():
        #print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key is pygame.K_m:
                    music.PlayStop()
                if event.key is pygame.K_d:
                    p1.MoveRight(p1.activeBlock)
                if event.key is pygame.K_a:
                    p1.MoveLeft(p1.activeBlock)
                if event.key is pygame.K_s:
                    p1.FallenLeaves(p1.activeBlock)
                if event.key is pygame.K_w:
                    p1.Rotate(p1.activeBlock)
                if event.key is pygame.K_SPACE:
                    p1.SwapHold()
        window.fill(black)
        txtOnScreen("Tetris?", 60,0,0, white)
        pygame.draw.rect(window, red,(0,(1080-54),54,54))
        if p1.BlockAlive == False:
            p1.RandomBlock()
        frameCount += 1 #1 Second == FPS. If Counter reaches 60 this means time passed 1 Second
        if frameCount == (fps/(Level*0.50)):
            p1.activeBlock.y -= 1
            frameCount = 0
        for y in range(len(p1.activeBlock.Blocks)): # Checks if some of the 4 Blocks hits the ground
            if p1.activeBlock.Blocks[y][1] <= 0:
                p1.getBlocks(p1.activeBlock.Blocks, p1.activeBlock.light_color, p1.activeBlock.dark_color)
                p1.BlockAlive = False
        p1.activeBlock.Draw()
        p1.DrawBlocks()
        p1.Grid()
        p1.HitDetection(p1.activeBlock)
        p1.CheckRows()
        pygame.display.update()
        clock.tick(fps)


#menu()
# main_loop()

if __name__ == '__main__':
    main_loop()

"""
List = [(True/False, color, posx, posy)]
"""
