import pygame

##############################################################################
def firstScreen():
    global x
    #define font pygame.font
    myFont = pygame.font.SysFont('Arial', 23)
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    
    while(x == 0):
        #pinta o ecra todo com preto
        screen.fill((0,0,0))
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()


        #define uma posicao de x e y do rectangulo, para saber quando o rato passar por cima
        rect1 = pos_x < 550 and pos_x > 450 and pos_y > 240 and pos_y < 270
        #desenha o rectangulo
        pygame.draw.rect(screen, (yellow), (450, 240, 100, 30), 2)
        #cria text e imprime o texto
        textRect1 = myFont.render('4x3', True, (yellow))
        screen.blit(textRect1,(481,242))
        #2
        rect2 = pos_x < 550 and pos_x > 450 and pos_y > 280 and pos_y < 310
        pygame.draw.rect(screen, (yellow), (450, 280, 100, 30), 2)
        textRect2 = myFont.render('4x4', True, (yellow))
        screen.blit(textRect2,(481,282))
        #3
        rect3 = pos_x < 550 and pos_x > 450 and pos_y > 320 and pos_y < 350
        pygame.draw.rect(screen, (yellow), (450, 320, 100, 30), 2)
        textRect3 = myFont.render('5x4', True, (yellow))
        screen.blit(textRect3,(481,322))
        #4
        rect4 = pos_x < 550 and pos_x > 450 and pos_y > 360 and pos_y < 390
        pygame.draw.rect(screen, (yellow), (450, 360, 100, 30), 2)
        textRect4 = myFont.render('6x5', True, (yellow))
        screen.blit(textRect4,(481,362))
        #5
        rect5 = pos_x < 550 and pos_x > 450 and pos_y > 400 and pos_y < 430
        pygame.draw.rect(screen, (yellow), (450, 400, 100, 30), 2)
        textRect5 = myFont.render('6x6', True, (yellow))
        screen.blit(textRect5,(481,402))
        #6
        rect6 = pos_x < 550 and pos_x > 450 and pos_y > 460 and pos_y < 490
        pygame.draw.rect(screen, (yellow), (450, 460, 100, 30), 2)
        textRect6 = myFont.render('Exit', True, (yellow))
        screen.blit(textRect6,(481,462))

        #muda rectangulos e texto de cor quando rato passa por cima
        if (rect1): 
            pygame.draw.rect(screen, (white), (450, 240, 100, 30), 3)
            textRect1 = myFont.render('4x3', True, (white))
            screen.blit(textRect1,(481,242))
        if (rect2): 
            pygame.draw.rect(screen, (white), (450, 280, 100, 30), 3)
            textRect2 = myFont.render('4x4', True, (white))
            screen.blit(textRect2,(481,282))
        if (rect3): 
            pygame.draw.rect(screen, (white), (450, 320, 100, 30), 3)
            textRect3 = myFont.render('5x4', True, (white))
            screen.blit(textRect3,(481,322))
        if (rect4): 
            pygame.draw.rect(screen, (white), (450, 360, 100, 30), 3)
            textRect4 = myFont.render('6x5', True, (white))
            screen.blit(textRect4,(481,362))
        if (rect5): 
            pygame.draw.rect(screen, (white), (450, 400, 100, 30), 3)
            textRect5 = myFont.render('6x6', True, (white))
            screen.blit(textRect5,(481,402))
        if (rect6): 
            pygame.draw.rect(screen, (white), (450, 460, 100, 30), 3)
            textRect6 = myFont.render('Exit', True, (white))
            screen.blit(textRect6,(481,462))

        #fecha o jogo quando se carregar no X
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect1):
                    x = 1
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect2):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect3):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect4):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect5):
                    pass
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect6):
                    exit()
        
        pygame.display.flip()
##############################################################################
def firstButton():
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))

    possibilidades = {}
    class geoForm:
        def __init__(self, form, color):
            self.form = form
            self.color = color

    redSquare = geoForm('square', 'green')


    while(x == 1):
        screen.fill((0,0,0))
        pos_x, pos_y = pygame.mouse.get_pos()
        print(pos_x, pos_y)
        #define uma posicao de x e y do rectangulo, para saber quando o rato passar por cima
        #desenha o rectangulo
        rect1 = pos_x < 365 and pos_x > 265 and pos_y > 50 and pos_y < 200
        pygame.draw.rect(screen, (green), (265, 50, 100, 150))
        #2
        rect2 = pos_x < 365 and pos_x > 265 and pos_y > 225 and pos_y < 375
        pygame.draw.rect(screen, (green), (265, 225, 100, 150))
        #3
        rect3 = pos_x < 365 and pos_x > 265 and pos_y > 400 and pos_y < 550
        pygame.draw.rect(screen, (green), (265, 400, 100, 150))
        #4
        rect4 = pos_x < 490 and pos_x > 390 and pos_y > 50 and pos_y < 200
        pygame.draw.rect(screen, (green), (390, 50, 100, 150))
        #5
        rect5 = pos_x < 490 and pos_x > 390 and pos_y > 225 and pos_y < 375
        pygame.draw.rect(screen, (green), (390, 225, 100, 150))
        #6
        rect6 = pos_x < 490 and pos_x > 390 and pos_y > 400 and pos_y < 550
        pygame.draw.rect(screen, (green), (390, 400, 100, 150))
        #7
        rect7 = pos_x < 615 and pos_x > 515 and pos_y > 50 and pos_y < 200
        pygame.draw.rect(screen, (green), (515, 50, 100, 150))
        #8
        rect8 = pos_x < 615 and pos_x > 515 and pos_y > 225 and pos_y < 375
        pygame.draw.rect(screen, (green), (515, 225, 100, 150))
        #9
        rect9 = pos_x < 615 and pos_x > 515 and pos_y > 400 and pos_y < 550
        pygame.draw.rect(screen, (green), (515, 400, 100, 150))
        #10
        rect10 = pos_x < 740 and pos_x > 640 and pos_y > 50 and pos_y < 200
        pygame.draw.rect(screen, (green), (640, 50, 100, 150))
        #11
        rect11 = pos_x < 740 and pos_x > 640 and pos_y > 225 and pos_y < 375
        pygame.draw.rect(screen, (green), (640, 225, 100, 150))
        #12
        rect12 = pos_x < 740 and pos_x > 640 and pos_y > 400 and pos_y < 550
        pygame.draw.rect(screen, (green), (640, 400, 100, 150))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        


        pygame.display.flip()

##############################################################################
def main ():
    #pygame
    pygame.init()
    pygame.font.init()
    #variaveis
    global x, yellow, white, green
    yellow, white, green =  (255,255,  0), (255,255,255), (0  , 150, 0) 
    x = 0

    while (True):
        if (x == 0):
            firstScreen()

        if (x == 1):
            firstButton()
##############################################################################
main()
