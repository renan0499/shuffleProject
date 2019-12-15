import pygame

def firstButton():
    screen = pygame.display.set_mode((1000, 600))
    screen.fill((0,0,0))
    
    while(True):
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()


def main ():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    x = 0
    while(x == 0):
        #desenha ecra
        screen.fill((0,0,0))
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()

        #desenha primeira rectangulo e define lhe uma posicao
        firstRect = pos_x < 550 and pos_x > 450 and pos_y > 240 and pos_y < 270
        pygame.draw.rect(screen, (255,255,0), (450, 240, 100, 30), 3)


        #muda de cor primeiro rectangulo quando rato passa por cima
        if (firstRect):
            pygame.draw.rect(screen, (255,255,255), (450, 240, 100, 30), 3)

            
        #fecha o jogo quando se carrega no X
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (firstRect):
                    x = 1
            
        
        pygame.display.flip()
    
    firstButton()




main()