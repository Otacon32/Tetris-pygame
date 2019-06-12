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