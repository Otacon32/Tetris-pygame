# -*- coding: utf-8 -*-
import pygame
import db
import main_old

pygame.init()
# -----------------#Window Options#-----------------
ScreenInfo = pygame.display.Info()
window_size2 = ((ScreenInfo.current_w, ScreenInfo.current_h))
window_size = (1920, 1080)  # 1920, 1080
window = pygame.display.set_mode((window_size), pygame.FULLSCREEN)
pygame.display.set_caption("Tetris Party remake")
clock = pygame.time.Clock()

# TODO: Make the window names less confusing before Game Logic


class Button(object):
    """docstring for Button"""
    def __init__(self, txt, size, posx, posy, txt_color = db.color_white, btn_color = db.color_red):
        super(Button, self).__init__()
        self.txt = txt
        self.size = size
        self.posx = posx
        self.posy = posy
        self.txt_color = txt_color
        self.btn_color = btn_color
        self.width = 0
        self.length = 0
        self.font = pygame.font.Font("./Ubuntu-R.ttf", self.size)
        self.text_width, self.text_height = self.font.size(self.txt)

    def draw(self):
        if pygame.mouse.get_pos()[0] in range(self.posx, self.posx+self.text_width) and pygame.mouse.get_pos()[1] in range(self.posy, self.posy+self.text_height):
            x = self.btn_color
            pygame.draw.rect(window, (x[0]-40, x[1], x[2]), (self.posx, self.posy, self.text_width, self.text_height))
        else:
            pygame.draw.rect(window, self.btn_color, (self.posx, self.posy, self.text_width, self.text_height))
        text = self.font.render(self.txt, 1, (self.txt_color))
        window.blit(text, (self.posx, self.posy))

class txtOnScreen(object):
    """docstring for txtOnSc"""
    def __init__(self, txt, x, y ,size = 40, color = db.color_black):
        super(txtOnScreen, self).__init__()
        self.txt = txt
        self.size = size
        self.posx = x
        self.posy = y
        self.color = color
        self.font = pygame.font.Font("./Ubuntu-R.ttf", self.size)

    def draw(self):
        """
        Display some Text on Screen.
        txtOnScreen("My Text", x, y, fontsize(int), color)
        """
        # font = pygame.font.Font("./Ubuntu-R.ttf", self.size)
        text = self.font.render(self.txt, 1, (self.color))
        window.blit(text, (self.posx, self.posy))
        # print(self.font.size(self.txt))

    def draw_simple(txt, x, y ,size = 40, color = db.color_black):
        """
        Display some Text on Screen without it beeing a Class Obj.
        """
        font = pygame.font.Font("./Ubuntu-R.ttf", size)
        text = font.render(txt, 1, (color))
        window.blit(text, (x, y))
    def changeTxt(self, txt):
        self.txt = txt


def menu():
    fps = 30
    run_menu = True
    # Creating Text and Buttons

    label1 = txtOnScreen("Tetris pygame Menu: ", 0, 0, 60, db.color_orange)
    start_btn = Button("Start", 40, 50, 100)
    exit_btn = Button("Exit Game", 40, 50, 150)

    # Mainloop
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
                if event.key is pygame.K_0:
                    run_menu = False
                    main_old.main_loop()

        window.fill(db.color_grey)
        txtOnScreen.draw_simple("Draw simple test", 500, 500, 40, db.color_dark_purple)
        label1.draw()
        start_btn.draw()
        exit_btn.draw()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    menu()