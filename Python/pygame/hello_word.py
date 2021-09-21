import pygame
import sys

from pygame import draw

pygame.init()
width= 500
height = 500
myWindow=pygame.display.set_mode((width,height))
pygame.display.set_caption("NUMBER RICE")

#COLORES RGB
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(255,255,255)

#figuras
rectangulo = pygame.Rect(10,10,15,15)
rectangulo2 = pygame.Rect(25,25,10,10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    
    myWindow.fill(red)
    pygame.draw.rect(myWindow,white,rectangulo)
    pygame.draw.circle(myWindow,white,(50,50),100)
    pygame.display.update()