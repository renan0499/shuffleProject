import pygame

pygame.init()
pygame.font.init()

#variaveis globais
global x, yellow, white, green, pos_x, pos_y, screen, myFont

yellow, white, green =  (255,255,  0), (255,255,255), (0  , 150, 0) 

screen = pygame.display.set_mode((1000, 600))

myFont = pygame.font.SysFont('Arial', 23)