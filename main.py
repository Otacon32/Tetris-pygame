# -*- coding: utf-8 -*-
import pygame, time, sys
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
posx=[457,507, 557, 607, 657, 707, 757, 807, 857, 907]
posy = [1028, 978, 928, 878, 828, 778, 728, 678, 628, 578, 528, 478, 428, 378, 328, 278, 228, 178, 128, 78, 28, -22, -72, -122, -172]
#-----------------#Window Options#-----------------
window_size = (1910, 1080)  #1920, 1080
window = pygame.display.set_mode((window_size), pygame.FULLSCREEN)
#ScreenInfo = pygame.display.Info()
#pygame.display.set_mode((ScreenInfo.current_w, ScreenInfo.current_h))
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
        self.grid = []
        grid.gridCount += 1 #falls 2 spieler drinnen sein wird
    def Grid(self):
        pygame.draw.rect(window, white, [(window_size[0]/2-self.x), (window_size[1]-self.y), self.x, self.y], 2)
        txtOnScreen("Next:",20,(window_size[0]/2+5),(window_size[1]-1000), white)

class Block():
    def __init__(self):
        #448 ganz links - 2 wegen 2px großen rand
        #1028 ganz unten
        self.x = 50
        self.y = 50
    def box(self):
        pygame.draw.rect(window, dark_red,(posx[0], posy[0],self.x,self.y)) # Box
        pygame.draw.rect(window, red,(posx[0]+6,posy[0]+6,self.x-12,self.y-12)) # Box
        #pygame.draw.rect(window, green, [457, 1028, self.x, self.y], 2) #Rahmen

class o_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 19
        self.light_color = yellow
        self.dark_color = dark_yellow
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box


class I_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 5
        self.y = 19
        self.light_color = cyan
        self.dark_color = dark_cyan
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

class L_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 7
        self.y = 19
        self.light_color = orange
        self.dark_color = dark_orange
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

class J_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 4
        self.y = 15
        self.light_color = blue
        self.dark_color = dark_blue
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

class S_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 4
        self.y = 11
        self.light_color = green
        self.dark_color = dark_green
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

class Z_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 4
        self.y = 8
        self.light_color = red
        self.dark_color = dark_red
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

class T_piece():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 8
        self.y = 8
        self.light_color = purple
        self.dark_color = dark_purple
    def Draw(self):
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.y -= 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x += 1
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box
        self.x -= 2
        pygame.draw.rect(window, self.dark_color,(posx[self.x], posy[self.y],self.width, self.height)) # Outer_Box
        pygame.draw.rect(window, self.light_color,(posx[self.x]+6,posy[self.y]+6,self.width-12,self.height-12)) # Inner_Box

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
    run_game = True
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
        window.fill(black)
        txtOnScreen("Tetris?", 60,0,0, white)
        pygame.draw.rect(window, red,(0,(1080-54),54,54))
        block1 = o_piece()
        block1.Draw()
        block2 = I_piece()
        block2.Draw()
        block3 = L_piece()
        block3.Draw()
        block4 = J_piece()
        block4.Draw()
        block5 = S_piece()
        block5.Draw()
        block6 = Z_piece()
        block6.Draw()
        block7 = T_piece()
        block7.Draw()
        p1 = grid()
        p1.Grid()
        pygame.display.update()
        clock.tick(fps)



#menu()
main_loop()
