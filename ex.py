import pygame

def firstScreen():
    #inicia pygame e pygame.font
    pygame.init()
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 23)
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    

    while(True):
        #pinta o ecra todo com preto
        screen.fill((0,0,0))
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()


        #define uma posicao de x e y do rectangulo, para saber quando o rato passar por cima
        rect1 = pos_x < 550 and pos_x > 450 and pos_y > 240 and pos_y < 270
        #desenha o rectangulo
        pygame.draw.rect(screen, (255,255,0), (450, 240, 100, 30), 2)
        #cria text e imprime o texto
        textRect1 = myFont.render('4x3', True, (255,255,0))
        screen.blit(textRect1,(481,242))
        
        rect2 = pos_x < 550 and pos_x > 450 and pos_y > 280 and pos_y < 310
        pygame.draw.rect(screen, (255,255,0), (450, 280, 100, 30), 2)
        textRect2 = myFont.render('4x4', True, (255,255,0))
        screen.blit(textRect2,(481,282))

        rect3 = pos_x < 550 and pos_x > 450 and pos_y > 320 and pos_y < 350
        pygame.draw.rect(screen, (255,255,0), (450, 320, 100, 30), 2)
        textRect3 = myFont.render('5x4', True, (255,255,0))
        screen.blit(textRect3,(481,322))

        rect4 = pos_x < 550 and pos_x > 450 and pos_y > 360 and pos_y < 390
        pygame.draw.rect(screen, (255,255,0), (450, 360, 100, 30), 2)
        textRect4 = myFont.render('6x5', True, (255,255,0))
        screen.blit(textRect4,(481,362))

        rect5 = pos_x < 550 and pos_x > 450 and pos_y > 400 and pos_y < 430
        pygame.draw.rect(screen, (255,255,0), (450, 400, 100, 30), 2)
        textRect5 = myFont.render('6x6', True, (255,255,0))
        screen.blit(textRect5,(481,402))

        rect6 = pos_x < 550 and pos_x > 450 and pos_y > 460 and pos_y < 490
        pygame.draw.rect(screen, (255,255,0), (450, 460, 100, 30), 2)
        textRect6 = myFont.render('Exit', True, (255,255,0))
        screen.blit(textRect6,(481,462))

        #muda rectangulos e texto de cor quando rato passa por cima
        if (rect1): 
            pygame.draw.rect(screen, (255,255,255), (450, 240, 100, 30), 3)
            textRect1 = myFont.render('4x3', True, (255,255,255))
            screen.blit(textRect1,(481,242))
        if (rect2): 
            pygame.draw.rect(screen, (255,255,255), (450, 280, 100, 30), 3)
            textRect2 = myFont.render('4x4', True, (255,255,255))
            screen.blit(textRect2,(481,282))
        if (rect3): 
            pygame.draw.rect(screen, (255,255,255), (450, 320, 100, 30), 3)
            textRect3 = myFont.render('5x4', True, (255,255,255))
            screen.blit(textRect3,(481,322))
        if (rect4): 
            pygame.draw.rect(screen, (255,255,255), (450, 360, 100, 30), 3)
            textRect4 = myFont.render('6x5', True, (255,255,255))
            screen.blit(textRect4,(481,362))
        if (rect5): 
            pygame.draw.rect(screen, (255,255,255), (450, 400, 100, 30), 3)
            textRect5 = myFont.render('6x6', True, (255,255,255))
            screen.blit(textRect5,(481,402))
        if (rect6): 
            pygame.draw.rect(screen, (255,255,255), (450, 460, 100, 30), 3)
            textRect6 = myFont.render('Exit', True, (255,255,255))
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


def firstButton():
    pygame.init()
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 23)
    screen = pygame.display.set_mode((1000, 600))
    
    while(True):
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()


def main ():
    x = 0

    while (True):
        if (x == 0):
            firstScreen()
        

        if (x == 1):
            firstButton()
    

main()
