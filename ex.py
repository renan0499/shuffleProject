import pygame

'''
def firstButton():
    screen = pygame.display.set_mode((1000, 600))
    screen.fill((0,0,0))
    
    while(True):
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
'''

def main ():
    pygame.init()
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    x = 0
    while(x == 0):
        #pinta o ecra todo com preto
        screen.fill((0,0,0))
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()


        #define uma posicao de x e y do rectangulo, para saber quando o rato passar por cima
        rect1 = pos_x < 550 and pos_x > 450 and pos_y > 240 and pos_y < 270
        #desenha o rectangulo
        pygame.draw.rect(screen, (255,255,0), (450, 240, 100, 30), 3)
        
        rect2 = pos_x < 550 and pos_x > 450 and pos_y > 280 and pos_y < 310
        pygame.draw.rect(screen, (255,255,0), (450, 280, 100, 30), 3)

        rect3 = pos_x < 550 and pos_x > 450 and pos_y > 320 and pos_y < 350
        pygame.draw.rect(screen, (255,255,0), (450, 320, 100, 30), 3)

        rect4 = pos_x < 550 and pos_x > 450 and pos_y > 360 and pos_y < 390
        pygame.draw.rect(screen, (255,255,0), (450, 360, 100, 30), 3)

        rect5 = pos_x < 550 and pos_x > 450 and pos_y > 400 and pos_y < 430
        pygame.draw.rect(screen, (255,255,0), (450, 400, 100, 30), 3)

        rect6 = pos_x < 550 and pos_x > 450 and pos_y > 460 and pos_y < 490
        pygame.draw.rect(screen, (255,255,0), (450, 460, 100, 30), 3)


        #muda de rectangulos de cor quando rato passa por cima
        if (rect1): pygame.draw.rect(screen, (255,255,255), (450, 240, 100, 30), 3)   
        if (rect2): pygame.draw.rect(screen, (255,255,255), (450, 280, 100, 30), 3)
        if (rect3): pygame.draw.rect(screen, (255,255,255), (450, 320, 100, 30), 3)
        if (rect4): pygame.draw.rect(screen, (255,255,255), (450, 360, 100, 30), 3)
        if (rect5): pygame.draw.rect(screen, (255,255,255), (450, 400, 100, 30), 3)
        if (rect6): pygame.draw.rect(screen, (255,255,255), (450, 460, 100, 30), 3)


            
        #fecha o jogo quando se carrega no X
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect1):
                    exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect2):
                    exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect3):
                    exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect4):
                    exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect5):
                    exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (rect6):
                    exit()
        
        pygame.display.flip()
    
    




main()
