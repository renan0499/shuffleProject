import pygame
from variables import *



class Button:
    def __init__ (self, card, isClicked, color, colorOver, maxX, minX, minY, maxY, x, y, xlenght, ylenght, hasText, textInput):
        pos_x, pos_y = pygame.mouse.get_pos()
        #define posição do rectangulo
        self.pos = (pos_x < maxX and pos_x > minX and pos_y > minY and pos_y < maxY)
        self.card = card
        self.isClicked = isClicked
        
        if (self.card):
            #muda cor quando a posicao é True
            if (self.pos):
            #desenha rectangulo
                pygame.draw.rect(screen, colorOver, (x, y, xlenght, ylenght))
        
            else:
                pygame.draw.rect(screen, color, (x, y, xlenght, ylenght))
        
        else:
            #muda cor quando a posicao é True
            c = color
            if (self.pos):
                c = colorOver
            #desenha rectangulo
            pygame.draw.rect(screen, c, (x, y, xlenght, ylenght), 2)
            #define texto e cor
            self.hasText = hasText
            self.text = myFont.render(textInput, True, c)
            self.writeText = screen.blit(self.text,(x+32.5,y+3.5))

        
            

