# -*- coding: utf-8 -*-
import pygame, time, sys, threading
#import pygame.mixer
from random import randint
"""
Tetris Party Deluxe war 20x10 blöcke groß; Alles über 21 ist gameover

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
posy = [1032, 982, 932, 882, 832, 782, 732, 682, 632, 582, 532, 482, 432, 382, 332, 282, 232, 182, 132, 82, 32, -18, -68, -118, -168] #19 top; 0 bottom
#-----------------#Window Options#-----------------
ScreenInfo = pygame.display.Info()
window_size2 = ((ScreenInfo.current_w, ScreenInfo.current_h))
window_size = (1920, 1080)  #1920, 1080
window = pygame.display.set_mode((window_size), pygame.FULLSCREEN)
pygame.display.set_caption("Tetris Party remake")
#pygame.display.set_icon(pygame.image.load("./assets/images/icon.png"))
clock = pygame.time.Clock()
#----------------#classes#---------------------------
class grid():
    gridCount = 0
    def __init__(self):
        grid.gridCount += 1 #falls 2 spieler drinnen sein wird
        self.array_x = [10]
        self.array_y = [20]
        #if grid.gridCount == 1:
        self.x = 500 #Breite des Spielbereiches Block = 50 breit
        self.y = 1000 # Höhe des Spielbereiches Block = 50 Hoch
        #self.Blockarray = [(False, color=None, x = None, y = None)]
        grid.gridCount += 1 #falls 2 spieler drinnen sein wird
    def Grid(self):
        pygame.draw.rect(window, white, [(window_size[0]/2-self.x), (window_size[1]-self.y), self.x, self.y], 2)
        txtOnScreen("Next:",20,(window_size[0]/2+5),(window_size[1]-1000), white)

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
    def Draw(self):
        #Upper Left
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        #Lower Left
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        #Upper Right
        pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        #Lower Right
        pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y-1],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box


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
    def Draw(self):
        def North():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+3],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+3]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x+3], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+3]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x-2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x-3], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-3]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Top
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-3],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-3]+6,self.width-12,self.height-12)) # Inner_Box
            #3rd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-2]+6,self.width-12,self.height-12)) # Inner_Box
            #2nd Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #1st Level
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        if self.CompasCount == 0:
            North()
        elif self.CompasCount == 1:
            East()
        elif self.CompasCount == 2:
            South()
        elif self.CompasCount == 3:
            West()

class L_piece():
    def __init__(self):
        self.CompasCount = 0
        self.width = 50
        self.height = 50
        self.x = defaultx
        self.y = defaulty
        self.light_color = orange
        self.dark_color = dark_orange
    def Draw(self):
        def North():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-2]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
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
    def Draw(self):
        def North():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+2]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-2],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-2]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-2], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-2]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Mid Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right == Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
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
    def Draw(self):
        def North():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Top Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
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
    def Draw(self):
        def North():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Top Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid = Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
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
    def Draw(self):
        def North():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
        def East():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        def South():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x+1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x+1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
        def West():
            #Low Left
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y+1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y+1]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Mid = Rotation Center
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
            #Low Right
            pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y-1],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y-1]+6,self.width-12,self.height-12)) # Inner_Box
            #Top Mid
            pygame.draw.rect(window, self.dark_color,(posx[self.x-1], posy[self.y],self.width, self.height)) # Outer_Box
            pygame.draw.rect(window, self.light_color,(posx[self.x-1]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
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
        txtOnScreen("Menü Test", 60,(955),(540), blue)
        pygame.display.update()
        clock.tick(fps)

def main_loop():
    p1 = grid()
    fps=60
    frameCount = 0
    run_game = True
    BlockAlive = False
    Level = 4
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
                    #move right
                    currentBlock.x += 1
                    if currentBlock.x >= 9:
                        currentBlock.x = 9
                if event.key is pygame.K_a:
                    #move left
                    currentBlock.x -= 1
                    if currentBlock.x <= 0:
                        currentBlock.x = 0
                if event.key is pygame.K_s:
                    #move Down
                    currentBlock.y = 0
                if event.key is pygame.K_w:
                    #Rotate
                    currentBlock.CompasCount += 1
                    if currentBlock.CompasCount > 3:
                        currentBlock.CompasCount = 0
        window.fill(black)
        txtOnScreen("Tetris?", 60,0,0, white)
        pygame.draw.rect(window, red,(0,(1080-54),54,54))
        if BlockAlive == False:
            randBox = randint(0,6)
            currentBlock = BlockTypes[randBox]()
            BlockAlive = True
        else:
            pass
        frameCount += 1 #1 Second == FPS. If Counter reaches 60 this means time passed 1 Second
        if frameCount == (fps/(Level*0.50)):
            currentBlock.y -= 1
            frameCount = 0
        if currentBlock.y <= 1:
            BlockAlive = False
        currentBlock.Draw()
        p1 = grid()
        p1.Grid()
        pygame.display.update()
        clock.tick(fps)


#menu()
main_loop()


"""
List = [(True/False, color, posx, posy)]
"""