# -*- coding: utf-8 -*-
import pygame
import db

pygame.init()
# -----------------#Window Options#-----------------
ScreenInfo = pygame.display.Info()
window_size2 = ((ScreenInfo.current_w, ScreenInfo.current_h))
window_size = (1920, 1080)  # 1920, 1080
window = pygame.display.set_mode((window_size), pygame.FULLSCREEN)
pygame.display.set_caption("Tetris Party remake")
clock = pygame.time.Clock()

# TODO: Make the window names less confusing before Game Logic

class GameWindow(object):
    """docstring for GameWindow"""

    def __init__(self):
        super(GameWindow, self).__init__()
        self.menu()

    def txtOnScreen(self, txt, txtsize, x, y, color):
        """
        Display some Text on Screen.
        txtOnScreen("My Text", fontsize(int), x, y, color)
        """
        font = pygame.font.Font("./Ubuntu-R.ttf", txtsize)
        text = font.render(txt, 1, (color))
        window.blit(text, (x, y))

    def Button(self, txt, txt_color, bg):
        pygame.draw.rect(window, db.color_dark_green, (300, 300, 30, 30))

    def menu(self):
        fps = 30
        run_menu = True
        while run_menu:
            for event in pygame.event.get():
                # print (event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key is pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            window.fill(db.color_white)
            self.txtOnScreen("Menu Test", 60, (0), (0), db.color_blue)
            self.txtOnScreen("Another Test", 40, (0), (50), db.color_dark_purple)
            self.Button1 = self.Button("Testbtn", db.color_black, db.color_green)
            pygame.display.update()
            clock.tick(fps)


GameMainWindow = GameWindow()
