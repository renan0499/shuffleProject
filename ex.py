import pygame
from button import *
from variables import *

##############################################################################
def firstScreen():
    global x
    #define font pygame.font
    myFont = pygame.font.SysFont('Arial', 23)
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    #load da imagem
    image = pygame.image.load("shuffle.png")
    


    while(x == 0):
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()
        #pinta o ecra todo com preto
        screen.fill((0,0,0))
        screen.blit(image, (100, 0))
        
        # class button = color, colorOver, maxX, minX, minY, maxY, x, y, xlenght, ylenght, hasText, textInput   #
        #criar os rectangulos
        rect1 = Button(False, False, yellow, white, 550, 450, 240, 270, 450, 240, 100, 30, True, '4x3')
        rect2 = Button(False, False, yellow, white, 550, 450, 280, 310, 450, 280, 100, 30, True, '4x4')
        rect3 = Button(False, False, yellow, white, 550, 450, 320, 350, 450, 320, 100, 30, True, '5x4')
        rect4 = Button(False, False, yellow, white, 550, 450, 360, 390, 450, 360, 100, 30, True, '6x5')
        rect5 = Button(False, False, yellow, white, 550, 450, 400, 430, 450, 400, 100, 30, True, '6x6')
        rectExit = Button(False, False, yellow, white, 550, 450, 460, 490, 450, 460, 100, 30, True, 'Exit')
        


        #fecha o jogo quando se carregar no X
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect1.pos):
                    x = 1
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect2.pos):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect3.pos):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect4.pos):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect5.pos):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rectExit.pos):
                    exit()

        pygame.display.flip()
##############################################################################
def firstButton():
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.SysFont('Arial', 23)

    possibilidades = {}
    class geoForm:
        def __init__(self, form, color):
            self.form = form
            self.color = color

    global x, white, green

    redSquare = geoForm('square', 'green')


    while(x == 1):
        screen.fill((0,0,0))
        pos_x, pos_y = pygame.mouse.get_pos()

        #define uma posicao de x e y do rectangulo, para saber quando o rato passar por cima
        #desenha o rectangulo
        
        rect11 = Button(True, False, green, white, 365, 265, 50, 200, 265, 50, 100, 150, False, '')
        rect21 = Button(True, False, green, white, 365, 265, 225, 375, 265, 225, 100, 150, False, '')
        rect31 = Button(True, False, green, white, 365, 265, 400, 550, 265, 400, 100, 150, False, '')
        rect12 = Button(True, False, green, white, 490, 390, 50, 200, 390, 50, 100, 150, False, '')
        rect22 = Button(True, False, green, white, 490, 390, 225, 375, 390, 225, 100, 150, False, '')
        rect32 = Button(True, False, green, white, 490, 390, 400, 550, 390, 400, 100, 150, False, '')
        rect13 = Button(True, False, green, white, 615, 515, 50, 200, 515, 50, 100, 150, False, '')
        rect23 = Button(True, False, green, white, 615, 515, 225, 375, 515, 225, 100, 150, False, '')
        rect33 = Button(True, False, green, white, 615, 515, 400, 550, 515, 400, 100, 150, False, '')
        rect14 = Button(True, False, green, white, 740, 640, 50, 200, 640, 50, 100, 150, False, '')
        rect24 = Button(True, False, green, white, 740, 640, 225, 375, 640, 225, 100, 150, False, '')
        rect34 = Button(True, False, green, white, 740, 640, 400, 550, 640, 400, 100, 150, False, '')


        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect11):
                    rect11.isClicked = True
            


        pygame.display.flip()

##############################################################################
def main ():
    #pygame
    pygame.init()
    pygame.font.init()
    global x, yellow, white, green, pos_x, pos_y, screen, myFont

    x = 0

    while (True):

        if (x == 0):
            firstScreen()

        if (x == 1):
            firstButton()
##############################################################################
main()
