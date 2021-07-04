import pygame
import shunting_yard as sy
pygame.init()


# Color Theme 
bg_clr = (255,255,255)    # color for background
clr1 = (231,235,78)     # color for top row of buttons
clr2 = (242,156,102)    # color for bottom row of buttons
clr3 = (36,5,100)         # color for text
clr4 = (249,236,185)    # color for hover button

win = pygame.display.set_mode((600,600))
win.fill(bg_clr)

class Button:
    def __init__(self, color, x, y, width, height, text, code):
        self.code = code
        self.clr = color
        self.txt_clr = clr3
        self.norm_clr = color
        self.alt_clr =clr3
        self.txt = text
        self.x = x  
        self.y = y
        self.w = width  
        self.h = height
        
    def draw(self, win, outline):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.w+4, self.h+4), 0)

        pygame.draw.rect(win, self.clr, (self.x, self.y, self.w, self.h))

        if(self.txt):
            font = pygame.font.SysFont('corbel',24)
            text = font.render(self.txt, 1, self.txt_clr)
            win.blit(text, (self.x + (self.w/2 - text.get_width()/2), self.y + (self.h/2 - text.get_height()/2)))


    def hover(self, pos):
        if(pos[0] > self.x and pos[0] < (self.x + self.w)):
            if (pos[1] > self.y and pos[1] < (self.y + self.h)):
                return True
        return False 

class TextBox:

    def __init__(self, color, x, y, text):

        self.clr = color
        self.txt = text
        self.x = x
        self.y = y

    def amendTxt(self,text):
        self.txt = text

    def draw(self, win, outline):
       
        if(self.txt):
            font = pygame.font.SysFont('corbel',50)
            text = font.render(self.txt, 1, clr3)
            win.blit(text, (self.x  - text.get_width(), self.y) )


def redraw(btn_list,txt_box):
    win.fill(bg_clr)
    for btn in btn_list:
        btn.draw(win, btn.clr)
    txt_box.draw(win, None)

if __name__ == "__main__":

    buttons = []
    display = ['sqrt', 'square', 'cube',   '^',\
               'log',  'sin',    'cos',    'tan',\
               'ln',   'arcsin', 'arccos', 'arctan',\
               'abs',  '(',      ')',      '!',\
               'e',    'pi',     'DEL',    'AC',\
               '7',    '8',      '9',      '*',\
               '4',    '5',      '6',      '/',\
               '1',    '2',      '3',      '+',\
               '0',    '.',      '=',     '-']

    message = ["l",    "i",      "j",      "^",\
               "n",    "c",      "d",      "e",\
               "o",    "f",      "g",      "h",\
               "p",    "(",      ")",      "q",\
               "b",    "a",      None,     None,\
               "7",    "8",      "9",      "*",\
               "4",    "5",      "6",      "/",\
               "1",    "2",      "3",      "+",\
               "0",    ".",      None,     "-"]

    W = 120
    H = 25
    clr_dif = ((clr1[0]-clr2[0])/8, (clr1[1]-clr2[1])/8, (clr1[2]-clr2[2])/8)
    for i in range(4):
        for j in range(9):
            X = 30 + i*(W + 20)
            Y = 200 + j*(H + 15)
            color = (clr1[0]-clr_dif[0]*j, clr1[1]-clr_dif[1]*j, clr1[2]-clr_dif[2]*j)
            new_btn = Button(color, X, Y, W, H, display[j*4+i], j*4+i)
            buttons.append(new_btn)

    

    run = True
    shown_expr = ""
    cal_expr = ""
    cal = sy.Calculator3()
    tb = TextBox((0,0,0),550,100,"")
    

    while run:
        redraw(buttons,tb)
        pygame.display.update()
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.hover(pos):
                        if(message[btn.code]):
                            shown_expr += display[btn.code]
                            cal_expr += message[btn.code]
                        else:
                            if(btn.code == 18):     #delete
                                shown_expr = shown_expr[:-1]
                                cal_expr = cal_expr[:-1] 
                            elif(btn.code == 19):   #clear
                                shown_expr = ""
                                cal_expr = ""
                            elif(btn.code == 34):   #equate
                                shown_expr = cal.calculate(cal_expr)
                        tb.amendTxt(shown_expr)
                        break
            
            if event.type == pygame.MOUSEMOTION:
                for btn in buttons:
                    if btn.hover(pos):
                        btn.clr = clr4
                    else:
                        btn.clr = btn.norm_clr

                